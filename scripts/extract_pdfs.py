#!/usr/bin/env python3
from pdfminer.high_level import extract_text
import sys

if len(sys.argv) < 2:
    print('Usage: extract_pdfs.py <file1.pdf> [file2.pdf ...]')
    sys.exit(1)

for path in sys.argv[1:]:
    try:
        print('---FILE:', path)
        text = extract_text(path)
        print(text)
    except Exception as e:
        print('ERROR reading', path, e)
