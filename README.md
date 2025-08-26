# Tabs

## Receipt OCR Script

A simple Python script to extract text from receipt images using EasyOCR.

### Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the script:
```bash
python ocr_receipt.py receipt.jpg
```

### Usage

```bash
# Single image
python ocr_receipt.py receipt.jpg

# Multiple images
python ocr_receipt.py receipt1.jpg receipt2.png

# Custom separator between images
python ocr_receipt.py receipt1.jpg receipt2.jpg --separator "\n---\n"
```

### Features

- Uses EasyOCR for text extraction
- Supports multiple image formats (JPG, PNG, BMP, TIFF)
- Filters low-confidence results (confidence > 0.5)
- Simple command-line interface
- Error handling for invalid files

## Coding Pattern Preferences

### Core Principles
- **Prefer simple solutions**; avoid unnecessary abstractions
- **Eliminate duplication**; reuse helpers across modules
- **Consider environments** (dev/test/prod) in config and logging
- **Only implement what's requested**; don't introduce new patterns or tech unless needed
- **Keep the codebase tidy and organized**

### Code Organization
- **Keep modules under ~200–300 LOC**; split into smaller modules when bigger
- **Avoid one-off scripts** living in random files
- **If refactors are introduced**, remove obsolete code to avoid duplicate logic

### Data & Configuration
- **Mocking data is ONLY for tests**; never ship fake/stub data in dev/prod
- **Never overwrite .env automatically**—read values, don't write them
