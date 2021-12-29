import pytesseract
from pdf2image import convert_from_path
import glob

#pdfs = glob.glob("katalog/*.pdf")

def pdf2text(pdf_path):
    print(pdf_path)
    all_text = ""
    pages = convert_from_path(pdf_path, 200)

    for pageNum, imgBlob in enumerate(pages):
        text = pytesseract.image_to_string(imgBlob,lang='tur')
        all_text += ' '.join(text.split())

    return all_text
    

all_text = ""
for i in range(1, 635):
    try:
        pdf_path = "katalog/" + str(i) + ".pdf"
        all_text += pdf2text(pdf_path) + "\n"
    except:
        print("Error on page " + str(i))
        
with open('text.txt', 'w') as the_file:
    the_file.write(all_text)
