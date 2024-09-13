import hashlib
import os
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

# Function to read the hex file and convert it into a hash
def read_hex_file(hex_file):
    try:
        with open(hex_file, 'r') as file:
            hex_data = file.read().strip()
            # Convert the hex to binary
            binary_data = bytes.fromhex(hex_data)
            return binary_data
    except Exception as e:
        print(Fore.RED + f"[Error] Unable to read hex file: {e}")
        return None

# Function to hash a word from the wordlist
def hash_word(word, hash_algorithm):
    # Hash the word using the chosen algorithm
    h = hash_algorithm()
    h.update(word.encode('utf-8'))
    return h.hexdigest()

# Function to crack the hash using the wordlist
def crack_hash(hex_file, wordlist_file, hash_algorithm):
    # Read the binary data from the hex file
    hash_from_file = read_hex_file(hex_file)
    if hash_from_file is None:
        print(Fore.RED + "[Error] Unable to process the hex file.")
        return

    # Convert binary data to hash (e.g., sha256)
    file_hash = hash_algorithm(hash_from_file).hexdigest()

    print(Fore.GREEN + f"[Info] Hash extracted from file: {file_hash}")

    # Read the wordlist and try each word
    try:
        with open(wordlist_file, 'r') as wordlist:
            for word in wordlist:
                word = word.strip()
                # Generate hash for the current word
                word_hash = hash_word(word, hash_algorithm)

                print(Fore.YELLOW + f"Trying word: {word}, Hash: {word_hash}")

                # Check if the generated hash matches the file hash
                if word_hash == file_hash:
                    print(Fore.GREEN + f"[Success] The correct word is: {Fore.CYAN + word}")
                    return word

    except FileNotFoundError:
        print(Fore.RED + "[Error] Wordlist file not found.")
        return

    print(Fore.RED + "[Info] No match found in the wordlist.")
    return None

def get_user_input():
    # Ask user for file paths and validate
    while True:
        hex_file = input(Fore.CYAN + "Enter the path to the hex file: ")
        if not os.path.isfile(hex_file):
            print(Fore.RED + "[Error] The file does not exist. Please try again.")
        else:
            break

    while True:
        wordlist_file = input(Fore.CYAN + "Enter the path to the wordlist file: ")
        if not os.path.isfile(wordlist_file):
            print(Fore.RED + "[Error] The file does not exist. Please try again.")
        else:
            break

    return hex_file, wordlist_file

if __name__ == "__main__":
    print(Style.BRIGHT + Fore.BLUE + "### Hash Cracking Tool ###" + Style.RESET_ALL)

    # Get user inputs for hex file and wordlist
    hex_file, wordlist_file = get_user_input()

    # Let the user choose the hash algorithm
    print(Style.BRIGHT + Fore.MAGENTA + "\nSelect the hash algorithm:")
    print(Fore.YELLOW + "[1] MD5")
    print(Fore.YELLOW + "[2] SHA1")
    print(Fore.YELLOW + "[3] SHA256")

    while True:
        choice = input(Fore.CYAN + "Enter your choice (1/2/3): ")
        if choice == "1":
            hash_algorithm = hashlib.md5
            break
        elif choice == "2":
            hash_algorithm = hashlib.sha1
            break
        elif choice == "3":
            hash_algorithm = hashlib.sha256
            break
        else:
            print(Fore.RED + "[Error] Invalid choice, please select again.")

    # Start cracking
    crack_hash(hex_file, wordlist_file, hash_algorithm)
