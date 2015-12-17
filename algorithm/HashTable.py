# _*_ encoding:utf-8 _*_

class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put_data_in_slot(self, key, data, slot):
        if (self.slots[slot] == None):
            self.slots[slot] = key
            self.data[slot] = data
            return True
        else:
            if self.slots[slot] == key:
                self.datap[slot] = data  # replace
                return True
            else:
                return False
        pass

    def put(self, key, data):
        slot = self.hash_function(key, self.size)
        result = self.put_data_in_slot(key, data, slot)

        while not result:
            slot = self.rehash(slot, self.size)
            result = self.put_data_in_slot(key, data, slot)

    def hash_function(self, key, size):
        return key % size

    def rehash(self, old_hash, size):
        return (old_hash + 1) % size

    def get(self, key):
        start_slot = self.hash_function(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = start_slot

        while self.slots[position] != None and not found and not stop:
            if (self.slots[position] == key):
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if (position == start_slot):
                    stop = True  # 又回来了
            return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)


table = HashTable()
table[54] = 'cat'
table[26] = 'dog'
table[93] = 'lion'
table[17] = "tiger"
table[77] = "bird"
table[44] = "goat"
table[55] = "pig"
table[20] = "chicken"
table[31] = "a"
table[42] = "b"

# 超过了HashTable的长度
# table[53] = "c"
# table[64] = "d"
# table[75] = "e"

print table.slots
print table.data
