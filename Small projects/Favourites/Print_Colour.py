from colorama import init, Fore
import os
import time
import sys

# Initialize colorama for Windows
init(autoreset=True)

# -----------------------------
# Utility Functions
# -----------------------------
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def slow_print(text, delay=0.05, color=None):
    """Print text slowly character by character, optionally with color."""
    for char in text:
        if color:
            sys.stdout.write(color + char + Fore.RESET)
        else:
            sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Test output
slow_print("This is normal text.")
slow_print("This is yellow dialogue.", color=Fore.YELLOW)
slow_print("This is red warning!", color=Fore.RED)
