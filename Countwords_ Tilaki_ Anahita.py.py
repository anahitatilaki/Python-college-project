
# Program Description: This program reads the contents of a text file, counts the occurrences of each unique word, and displays the results. 
#                      It uses dictionaries and handles specific exceptions as instructed.
# Name: Anahita Tilaki
# Date: 11.17.2024

import string

def get_file_name():
    """Prompt the user to enter the file name."""
    file_name = input("Enter the name of the input file: ")
    return file_name

def read_file(file_name):
    """Read the file, clean up punctuation at the end of each word, and return a list of words."""
    try:
        with open(file_name, 'r') as file:
            text = file.read()
            # Remove punctuation at the end of each word
            words = [word.strip(string.punctuation) for word in text.split()]
        return words
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        raise
    except Exception as e:
        print(f"An error occurred: {e}")
        raise

def setup_word_dictionary(words):
    """Create a dictionary with each unique word as a key and initialize the value as 0."""
    word_counter = {word.lower(): 0 for word in words}
    return word_counter

def count_words(words, word_counter):
    """Count the occurrence of each word and update the dictionary values."""
    for word in words:
        key = word.lower()
        if key in word_counter:
            word_counter[key] += 1
        else:
            print(f"Warning: Key '{key}' not found in dictionary (unexpected behavior).")
            raise KeyError(key)

def display_results(word_counter):
    """Display each word with its occurrence count."""
    print("\nWords and Occurrences")
    print("-" * 50)
    for word, count in word_counter.items():
        print(f"{word}: {count}")

def main():
    """Main function to orchestrate the program flow."""
    try:
        file_name = get_file_name()
        words = read_file(file_name)
        word_counter = setup_word_dictionary(words)
        count_words(words, word_counter)
        display_results(word_counter)
    except FileNotFoundError:
        print("Please check the file name and try again.")
    except KeyError as ke:
        print(f"Unexpected key error with word: {ke}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
    input("Press Enter to Exit")
