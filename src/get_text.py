import cv2
import pytesseract
from PIL import Image, ImageEnhance
import numpy as np


def get_text():
    indir = r"output_images/"
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
