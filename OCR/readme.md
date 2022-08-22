# OCR (Optical Character Recognition)

All content are availiable in my github repo:

https://github.com/coherent17/Raspberry-Pi/tree/main/OCR

## download and install

```bash
sudo apt install tesseract-ocr
pip install pytesseract

#get the pre-trained weight in English
wget https://github.com/tesseract-ocr/tessdata_best/raw/main/eng.traineddata

#get the pre-trained weight in Traditional Chinese
wget https://github.com/tesseract-ocr/tessdata_best/raw/main/chi_tra.traineddata

#fix the space problem in Traditional Chinese
#(https://github.com/tesseract-ocr/tesseract/issues/991)
wget https://github.com/tesseract-ocr/tessdata_best/raw/main/chi_tra_vert.traineddata

#move pretrained-weight into correct folder
mv -v eng.traineddata /usr/share/tesseract-ocr/4.00/tessdata/
mv -v chi_tra.traineddata /usr/share/tesseract-ocr/4.00/tessdata/
mv -v chi_tra_vert.traineddata /usr/share/tesseract-ocr/4.00/tessdata/
```

## Using python simulate the package
```python=
import pytesseract
import shutil
import os
import random
from PIL import Image

extractedInformation = pytesseract.image_to_string(Image.open(filename), lang='chi_tra+chi_tra_vert+eng')
print(extractedInformation)
```

## result:
*    1
    ![](https://i.imgur.com/nn4V0np.png)
    ![](https://i.imgur.com/n1SDlOw.png)

*    2
    ![](https://i.imgur.com/MmA6Kwp.png)
    ![](https://i.imgur.com/2da8oPE.png)

## Conclusion:
Result highly depend on the quality of the original picture, therefore, I think we need to do some image processing first, for example using cv2 to sharp the image. After that, I think we might get a better result.