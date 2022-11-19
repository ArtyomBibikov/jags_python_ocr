import glob
import os
from pdf2image import convert_from_path


def get_images():
    if not os.path.exists('output_images/'):
        os.makedirs('output_images/')
    for f in glob.glob('output_images/*'):
        os.remove(f)
    filename = input("Insert the exact filename in the 'input_pdf' folder: ")
    pdfs = r"input_pdf\{}".format(filename)
    pages = convert_from_path(pdfs, 350, poppler_path=r"utils")
    i = 1
    for page in pages:
        image_name = "output_images/Page_" + str(i) + ".jpg"
        page.save(image_name, "JPEG")
        i = i + 1
