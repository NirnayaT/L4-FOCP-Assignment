from collections import Counter

def analyze_frequency(text):
    letter_counts = Counter(char.lower() for char in text if char.isalpha())
    
    #top 6 most common letters
    most_common = letter_counts.most_common(6)
    
    # Print results
    print("The six most common letters are:")
    for letter, count in most_common:
        print(f"'{letter}': {count} times")

# Test
sample_text = "This is a sample text to analyze frequency of letters in English language"
analyze_frequency(sample_text)
