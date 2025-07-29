#!/usr/bin/env python3
"""
test - Main module
"""
from datetime import datetime
import platform


def main():
    """Main function"""
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Hello from test! Current time: {current_time}")
    print(f"Python version: {__import__('sys').version.split()[0]}")
    print(f"Operating System: {platform.system()}")


if __name__ == "__main__":
    main()
