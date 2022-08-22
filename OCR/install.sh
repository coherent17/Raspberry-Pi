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