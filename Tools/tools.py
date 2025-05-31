def print_dict_vertical(d: dict, title: str = None) -> None:
    """
    Prints a dictionary in vertical key-value format.
    
    Args:
        d (dict): The dictionary to print.
        title (str): Optional title to display before printing.
    """
    if title:
        print(f"\n🧾 {title}\n" + "-" * (len(title) + 4))
    for k, v in d.items():
        print(f"{k.title():<15}: {v}")
    print()

def print_section(title: str) -> None:
    """
    Prints a visual divider with a title.
    
    Args:
        title (str): The title to display.
    """
    print("\n" + "=" * 50)
    print(f"🧠 {title.upper()}")
    print("=" * 50 + "\n")

from datetime import datetime

def log(message: str) -> None:
    """
    Prints a timestamped log message.
    
    Args:
        message (str): The message to log.
    """
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{now}] {message}")

import time

class Timer:
    def __init__(self, label="Timer"):
        self.label = label
        self.start = None

    def __enter__(self):
        self.start = time.time()
        print(f"⏳ {self.label} started...")
        return self

    def __exit__(self, *args):
        elapsed = time.time() - self.start
        print(f"✅ {self.label} finished in {elapsed:.4f} seconds.\n")


def safe_int_input(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ Invalid input. Please enter a valid integer.")

def percent(value: float, total: float, round_to: int = 2) -> str:
    if total == 0:
        return "0%"
    return f"{round((value / total) * 100, round_to)}%"


import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


import sys
import time

def progress_bar(iterable, prefix="", size=60):
    total = len(iterable)

    def show(j):
        x = int(size * j / total)
        sys.stdout.write(f"\r{prefix}[{'█' * x}{'.' * (size - x)}] {j}/{total}")
        sys.stdout.flush()

    show(0)
    for i, item in enumerate(iterable):
        yield item
        show(i + 1)
    print()
