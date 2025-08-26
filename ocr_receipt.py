#!/usr/bin/env python3
import cv2
import pytesseract

# Hardcoded file path
image_path = "receipt.jpg"

# Read image
image = cv2.imread(image_path)

if image is None:
    print(f"Error: could not read {image_path}")
    exit(1)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# OCR with Tesseract
text = pytesseract.image_to_string(gray)

# Print extracted text
print("=== OCR Output ===")
print(text.strip())
