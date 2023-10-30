class BloomFilter:
    def __init__(self, size, hash_functions):
        self.size = size
        self.hash_functions = hash_functions
        self.bit_array = [0] * size

    def custom_hash(self, element, seed):
        # Custom hash function for demonstration
        value = hash(element + str(seed)) % self.size
        return value

    def add(self, element):
        for i in range(self.hash_functions):
            index = self.custom_hash(element, i)
            self.bit_array[index] = 1

    def contains(self, element):
        for i in range(self.hash_functions):
            index = self.custom_hash(element, i)
            if self.bit_array[index] == 0:
                return False
        return True

# Example usage
bloom_filter = BloomFilter(1000, 3)  # Bloom Filter with size 1000 and 3 hash functions

elements_to_add = ["apple", "banana", "cherry", "date"]
for element in elements_to_add:
    bloom_filter.add(element)

elements_to_check = ["apple", "banana", "grape", "fig"]
for element in elements_to_check:
    if bloom_filter.contains(element):
        print(f"'{element}' is probably in the set.")
    else:
        print(f"'{element}' is definitely not in the set.")
