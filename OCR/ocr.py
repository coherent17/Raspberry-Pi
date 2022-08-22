import pytesseract
import shutil
import os
import random
from PIL import Image

extractedInformation = pytesseract.image_to_string(Image.open(filename), lang='chi_tra+chi_tra_vert+eng')
print(extractedInformation)