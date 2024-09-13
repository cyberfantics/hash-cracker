import hashlib
import os
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

# Function to read the hash from a file
def read_hash_file(hash_file):
    try:
        with open(hash_file, 'r') as file:
            return file.read().strip()
    except Exception as e:
        print(Fore.RED + f"[Error] Unable to read hash file: {e}")
        return None

# Function to hash a word from the wordlist
def hash_word(word, hash_algorithm):
    # Hash the word using the chosen algorithm
    h = hash_algorithm()
    h.update(word.encode('utf-8'))
    return h.hexdigest()

# Function to crack the hash using the wordlist
def crack_hash(hash_value, wordlist_file, hash_algorithm):
    print(Fore.GREEN + f"[Info] Target hash: {hash_value}")

    # Read the wordlist and try each word
    try:
        with open(wordlist_file, 'r') as wordlist:
            for word in wordlist:
                word = word.strip()
                # Generate hash for the current word
                word_hash = hash_word(word, hash_algorithm)

                print(Fore.YELLOW + f"Trying word: {word}, Hash: {word_hash}")

                # Check if the generated hash matches the target hash
                if word_hash == hash_value:
                    print(Fore.GREEN + f"[Success] The correct word is: {Fore.CYAN + word}")
                    return word

    except FileNotFoundError:
        print(Fore.RED + "[Error] Wordlist file not found.")
        return

    print(Fore.RED + "[Info] No match found in the wordlist.")
    return None

def get_user_input():
    # Ask user for hash source and validate
    hash_source = input(Fore.CYAN + "Do you have the hash in a file or directly? (file/direct): ").strip().lower()
    
    if hash_source == 'file':
        while True:
            hash_file = input(Fore.CYAN + "Enter the path to the hash file: ")
            if not os.path.isfile(hash_file):
                print(Fore.RED + "[Error] The file does not exist. Please try again.")
            else:
                hash_value = read_hash_file(hash_file)
                if hash_value:
                    break
                else:
                    print(Fore.RED + "[Error] Could not read the hash from the file.")
    elif hash_source == 'direct':
        hash_value = input(Fore.CYAN + "Enter the hash value directly: ").strip()
    else:
        print(Fore.RED + "[Error] Invalid option. Please start again.")
        return None, None

    while True:
        wordlist_file = input(Fore.CYAN + "Enter the path to the wordlist file: ")
        if not os.path.isfile(wordlist_file):
            print(Fore.RED + "[Error] The file does not exist. Please try again.")
        else:
            break

    return hash_value, wordlist_file

if __name__ == "__main__":
    print(Style.BRIGHT + Fore.BLUE + "### Hash Cracking Tool ###" + Style.RESET_ALL)

    # Get user inputs for hash and wordlist
    hash_value, wordlist_file = get_user_input()
    
    if hash_value is None:
        print(Fore.RED + "[Error] Exiting due to invalid input.")
        exit()

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
    crack_hash(hash_value, wordlist_file, hash_algorithm)
