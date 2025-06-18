from pylibdmtx.pylibdmtx import decode
from PIL import Image

image_path = "barcode.jpg"
image = Image.open(image_path)

results = decode(image)

if results:
    for result in results:
        print("Decoded Data:", result.data.decode('utf-8'))
        print("Bounding Box:", result.rect)
else:
    print("No data matrix found in the image.")
