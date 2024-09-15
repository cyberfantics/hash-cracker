## Hash Cracking Tool

A Python script to crack hashes from a `.hex` file using a wordlist. The script supports MD5, SHA1, and SHA256 algorithms.

## Features

- Supports **MD5**, **SHA1**, and **SHA256**.
- Reads hex-encoded hashes from a file.
- Attempts to crack the hash using a wordlist.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/cyberfantics/hash-cracker.git
   ```
2. Install dependencies:
   ```bash
   pip install colorama
   ```

## Usage

1. Run the script:
   ```bash
   python3 main.py
   ```
2. Follow the prompts to input:
   - Hex file path
   - Wordlist file path
   - Hash algorithm (MD5/SHA1/SHA256)

## Example

```bash
### Hash Cracking Tool ###
Enter the path to the hex file: inputfile.hex
Enter the path to the wordlist file: wordlist.txt
Select the hash algorithm (1/2/3): 3
[Success] The correct word is: password123
```

## Developer

Created by **Mansoor Bukhari**.
