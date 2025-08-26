import cv2
import easyocr

image_path = "receipt.jpg"

# Read image
image = cv2.imread(image_path)

if image is None:
    print(f"Error: could not read {image_path}")
    exit(1)

# Convert to grayscale
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


reader = easyocr.Reader(['en'], gpu=True)
results = reader.readtext(image)

print("=== OCR Output ===")
for (bbox, text, prob) in results:
    print(f"Text: {text} (Confidence: {prob:.2f})")
