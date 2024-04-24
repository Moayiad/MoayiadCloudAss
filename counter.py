from collections import Counter

def count_word_frequency_from_file(file_path):
    with open(file_path, 'r') as file:
        # Read the entire file content
        text = file.read()
        
        # Split the text into words
        words = text.split()
        
        # Count the frequency of each word
        word_counts = Counter(words)
        
        return word_counts

# Path to the text file
file_path = '/app/cleaned_text.txt'

# Count word frequency from the file
word_frequency = count_word_frequency_from_file(file_path)

# Print the word frequency
for word, count in word_frequency.items():
    print(f"{word}: {count}")
