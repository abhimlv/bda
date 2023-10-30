from functools import reduce
data = [
    "Hello, world!",
    "This is a simple word count example.",
    "Word count is a common data processing task.",
    "In MapReduce, we map and then reduce.",
    "MapReduce is used for large-scale data processing.",
]
def map_function(text):
    words = text.split()
    word_count = [(word, 1) for word in words]
    return word_count
def reduce_function(word_count1, word_count2):
    merged_word_count = {}
    
    for word, count in word_count1:
        merged_word_count[word] = merged_word_count.get(word, 0) + count
    
    for word, count in word_count2:
        merged_word_count[word] = merged_word_count.get(word, 0) + count
    
    return [(word, count) for word, count in merged_word_count.items()]

mapped_data = list(map(map_function, data))
word_counts = reduce(reduce_function, mapped_data)

# Step 4: Display the word count results
for word, count in word_counts:
    print(f"{word}: {count}")