path = "books/frankenstein.txt"
def main():
    text = read_text(path)
    word_count = count_words(text)
    character_count = count_characters(text)
    alphabetic_sort = sort_alpha(character_count)
    frequency_sort = sort_freq(character_count)
    print(f"--- Begin report of {path} ---")
    generate_report(word_count, alphabetic_sort)
    generate_report(word_count, frequency_sort)
    print("--- End report ---")

def read_text(path):
    with open(path) as f:
        return f.read().split()

def count_words(text):
    return len(text)

def count_characters(text):
    lowercase = [words.lower() for words in text]
    count = {}
    for lower in lowercase:
        for alphabet in lower:
            if alphabet in count:
                count[alphabet] += 1
            else:
                count[alphabet] = 1
    return count

def sort_alpha(dict):
    return sorted(dict.items(), key=lambda x: x[0])

def sort_freq(dict):
    return sorted(dict.items(), reverse=True, key=lambda x: x[1])

def generate_report(words, characters):
    print(f"{words} words found in the document")
    for character in characters:
        if character[0].isalpha():
            print(f"The '{character[0]}' character was found {character[1]} times")

main()



