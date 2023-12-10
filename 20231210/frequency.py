from collections import defaultdict
text = """
The Python defaultdict type is a dictionary-like class available in Python's collections module. 
Unlike standard Python dictionaries, defaultdict lets you specify a default value type at the 
time of its creation. When you try to access or modify keys in the defaultdict that do not exist,
instead of a KeyError, you get a default value of the type you specified during creation. 
The defaultdict type is useful in situations where you want to avoid unnecessary KeyError exceptions 
and make your code more readable and clean. It's especially handy when working with collections of 
data where some keys might not exist.
"""

word_freq = defaultdict(int)

# Normalize the text
normalized_text = text.lower().split()

# Count the frequency of each word
for word in normalized_text:
    word_freq[word] += 1

for word, freq in word_freq.items():
    print(f'Word: {word}, Frequency: {freq}')
