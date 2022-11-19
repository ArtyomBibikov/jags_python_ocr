import glob
import os
import cv2
from pdf2image import convert_from_path
import pytesseract
from PIL import Image, ImageEnhance
import numpy as np

if not os.path.exists('output_images/'):
    os.makedirs('output_images/')
for f in glob.glob('output_images/*'):
    os.remove(f)
filename = input("Insert the exact filename in the 'input_pdf' folder: ")
pdfs = r"C:\Users\JAG\PycharmProjects\text_recognition\input_pdf\{}".format(filename)
pages = convert_from_path(pdfs, 350, poppler_path=r"utils")
i = 1
for page in pages:
    image_name = "output_images/Page_" + str(i) + ".jpg"
    page.save(image_name, "JPEG")
    i = i + 1

indir = r"C:/Users/JAG/PycharmProjects/text_recognition/output_images/"
for root, dirs, filenames in os.walk(indir):
    for filename in filenames:
        print('~~~~~' + filename + '~~~~')
        img = Image.open(indir + filename)
        #new_size = tuple(2 * x for x in img.size)
        #img = img.resize(new_size, Image.Resampling.LANCZOS)
        #contrast_enhancer = ImageEnhance.Contrast(img)
        #pil_enhanced_image = contrast_enhancer.enhance(2)
        #enhanced_image = np.asarray(pil_enhanced_image)
        #r, g, b = cv2.split(enhanced_image)
        #enhanced_image = cv2.merge([b, g, r])
        text = pytesseract.image_to_string(img, lang='rus')
        print(text)
