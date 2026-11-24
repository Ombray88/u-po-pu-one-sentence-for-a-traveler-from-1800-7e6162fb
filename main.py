"""An endless web of fine wires linking every library and home, so any book
or message reaches your hand in an instant — an image a traveler from 1800 can hold."""

import os

def main():
    sentence = "Imagine an endless web of fine wires linking every library and home on earth, where any book or message is brought to your hand in an instant."
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(sentence)

if __name__ == "__main__":
    main()
