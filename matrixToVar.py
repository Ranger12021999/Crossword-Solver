try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

rows, cols = (5, 5)
arr = [[' '] * cols] * rows

testImage = Image.open("box2.jpg")
print(pytesseract.image_to_boxes(testImage))

# Get verbose data including boxes, confidences, line and page numbers
print(pytesseract.image_to_data(Image.open("box2.jpg")))

# Get information about orientation and script detection
print(pytesseract.image_to_osd(Image.open("box2.jpg")))
