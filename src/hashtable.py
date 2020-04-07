# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.blocks = 0


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value, copying=False):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        index = self._hash_mod(key)

        pair = self.storage[index]

        if pair is not None:
            while pair is not None:
                if pair.key == key:
                    pair.value = value
                    return
                if pair.next == None:
                    pair.next = LinkedPair(key, value)
                    self.blocks += 1
                    if not copying:
                        self.check_usage()
                    return
                pair = pair.next
            
        else:
            self.storage[index] = LinkedPair(key, value)
            self.blocks += 1
            if not copying:
                self.check_usage()



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        pair = self.storage[index]

        if pair is not None:
            if pair.key == key:
                if pair.next is not None:
                    self.storage[index] = pair.next
                    self.blocks -= 1
                    self.check_usage()
                    return
                else:
                    self.storage[index] = None
                    self.blocks -= 1
                    self.check_usage()
                    return
            while pair.next is not None:
                if pair.next.key == key:
                    if pair.next.next is not None:
                        pair.next = pair.next.next
                        self.blocks -= 1
                        self.check_usage()
                        return
                    else:
                        pair.next = None
                        self.blocks -= 1
                        self.check_usage()
                        return
                pair = pair.next

        print('key does not exist')


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        pair = self.storage[index]

        if pair is not None:
            while pair.next is not None:
                if pair.key == key:
                    return pair.value
                pair = pair.next
            if pair.key == key:
                    return pair.value

        print('key does not exist')


    def resize(self, mod=2):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        import math
        newTable = HashTable(math.floor(self.capacity * mod))
        
        for i in self.storage:
            pair = i
            while pair is not None:
                newTable.insert(pair.key, pair.value, True)
                pair = pair.next
        self.capacity = newTable.capacity
        self.storage = newTable.storage

    def check_usage(self):
        usage = self.blocks / self.capacity
        print(usage)
        if usage > .7:
            self.resize()
            return
        elif usage < .2:
            self.resize(.5)
            return
        # pass



# if __name__ == "__main__":
#     ht = HashTable(2)

#     ht.insert("line_1", "Tiny hash table")
#     ht.insert("line_2", "Filled beyond capacity")
#     ht.insert("line_3", "Linked list saves the day!")

#     print("")

#     # Test storing beyond capacity
#     print(ht.retrieve("line_1"))
#     print(ht.retrieve("line_2"))
#     print(ht.retrieve("line_3"))

#     # Test resizing
#     old_capacity = len(ht.storage)
#     ht.resize()
#     new_capacity = len(ht.storage)

#     print(f"\nResized from {old_capacity} to {new_capacity}.\n")

#     # Test if data intact after resizing
#     print(ht.retrieve("line_1"))
#     print(ht.retrieve("line_2"))
#     print(ht.retrieve("line_3"))

#     print("")
