def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print("--- Begin report of books/frankenstein.txt ---\n")
    word_count = get_word_count(text)
    print(f"{word_count} words in this document\n")
    letter_occurences = get_letter_occurence_to_dict(text)
    print(formatted_letter_report(letter_occurences))
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_word_count(text):
    return len(text.split())

def get_letter_occurence_to_dict(text):
    letter_occurence = {}
    lowered_string = text.lower()
    for letter in lowered_string:
        if letter.isalpha() == False:
            continue
        if letter in letter_occurence:
            letter_occurence[letter] += 1
        else:
            letter_occurence[letter] = 1
    return letter_occurence

def formatted_letter_report(letter_occurence):
    report = ""
    letter_occurence = dict(sorted(letter_occurence.items()))
    for letter, count in letter_occurence.items():
        report += f"The '{letter}' character was found {count} times\n"
    return report


main()