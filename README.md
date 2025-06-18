# 📦 Data Matrix Barcode Reader

This Python-based tool uses `pylibdmtx` and `Pillow` to decode **Data Matrix barcodes** from zoomed-in warehouse images. Built as part of my internship at Dockware AI.

## 🛠️ Features

- Reads barcodes using `pylibdmtx`
- Outputs decoded data and bounding box
- Easy to set up with Python 3.11

## 🧪 Example Output

Decoded Data: great job you did it!
Bounding Box: Rect(left=8, top=11, width=72, height=71)


## 🚀 How to Use

1. Clone the repo:
git clone https://github.com/afnanrahmannn/data-matrix-reader.git
cd data-matrix-reader


2. Set up a virtual environment:
ython3.11 -m venv venv
source venv/bin/activate


3. Install dependencies:
pip install -r requirements.txt


4. Add your `barcode.jpg` file

5. Run the script:

python3 read_barcode.py


## 📦 Dependencies

- pylibdmtx
- pillow
- opencv-python (optional for preprocessing)

## 👨‍💻 Author

**Afnan Rahman**  
[LinkedIn](https://www.linkedin.com/in/afnanrahmanprofile/)  
[afnanrahmanbusiness@gmail.com](mailto:afnanrahmanbusiness@gmail.com)

---

Once you save the file, back in Terminal:

```bash
git add README.md
git commit -m "Add project README"
git push

