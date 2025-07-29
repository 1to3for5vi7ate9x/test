#!/usr/bin/env python3
"""
test - Main module
"""
from datetime import datetime


def main():
    """Main function"""
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Hello from test! Current time: {current_time}")


if __name__ == "__main__":
    main()
