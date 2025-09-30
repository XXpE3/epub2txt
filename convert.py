#!/usr/bin/env python3
import sys
from pathlib import Path
from epub2txt import epub2text


def main():
    if len(sys.argv) != 2:
        print("Usage: python convert.py <epub_file_path>")
        sys.exit(1)

    epub_path = sys.argv[1]

    if not Path(epub_path).exists():
        print(f"Error: File not found: {epub_path}")
        sys.exit(1)

    if not epub_path.lower().endswith('.epub'):
        print("Error: Input file must be an EPUB file")
        sys.exit(1)

    # Convert EPUB to text
    print(f"Converting {epub_path}...")
    text = epub2text(epub_path)

    # Generate output filename
    output_path = Path(epub_path).with_suffix('.txt')

    # Write to file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(text)

    print(f"✓ Conversion complete: {output_path}")


if __name__ == '__main__':
    main()