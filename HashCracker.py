import hashlib

# ANSI color codes
YELLOW = '\033[93m'
BOLD = '\033[1m'
RESET = '\033[0m'

def crack_hash(target_hash, dictionary_file, algorithm='md5'):
    with open(dictionary_file, 'r') as file:
        for line in file:
            password = line.strip()
            hashed_password = hashlib.new(algorithm, password.encode()).hexdigest()

            if hashed_password == target_hash:
                return f"{BOLD}{YELLOW}Password found: {password}{RESET}"

    return f"{BOLD}{YELLOW}Password not found in the dictionary.{RESET}"

if __name__ == "__main__":
    print(f"{BOLD}{YELLOW}Welcome To Hash Cracker{RESET}")

    target_hash = input("Enter the hash to crack: ")
    dictionary_file = input("Enter the path to the dictionary file: ")

    result = crack_hash(target_hash, dictionary_file)

    print(result)
