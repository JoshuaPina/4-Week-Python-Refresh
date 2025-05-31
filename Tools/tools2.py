#load json file

import json

def load_json(filename: str) -> dict:
    """
    Load JSON data from a file and return it as a dictionary.
    """
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("❌ File not found.")
        return {}
    except json.JSONDecodeError:
        print("❌ Invalid JSON format.")
        return {}

#save json file

def save_json(data: dict, filename: str) -> None:
    """
    Save a dictionary or list as a JSON file.
    """
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
        print(f"✅ Data saved to {filename}")

#read lines from a text file

def read_lines(filename: str) -> list:
    """
    Reads all lines from a text file into a list.
    """
    try:
        with open(filename, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        print("❌ File not found.")
        return []

#write lines to a text file

def write_lines(lines: list, filename: str) -> None:
    """
    Writes a list of strings to a file, each on a new line.
    """
    with open(filename, "w") as file:
        file.writelines(lines)
        print(f"✅ Lines written to {filename}")


#random password generator

import string
import random

def generate_password(length: int = 12) -> str:
    """
    Generates a secure random password.
    """
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

#random username generator

def generate_username(prefix: str = "user") -> str:
    """
    Generates a random username with a prefix.
    """
    return f"{prefix}_{random.randint(1000, 9999)}"
