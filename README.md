# ocr
Extract specific text from scanned pdf documents

You have to install tesseract on your system to run the script in addition to the requirements.txt file

You have to give 3 arguments to run the script
a)Filename of the pdf document
b)filename of the text file where all the text in the pdf is stored
c)Filename of the text file where all the specific text will get extracted

For eg. python ocr.py Assignment-1.pdf out_txt1.txt output1.txt

Major Steps followed for ocr

1)Coverting all the pages in the pdf document to images
2)Used Gaussian blur and Otsu's thresholding algorithm for image preprocessing
3)Used pytesseract to extract the text from the processed images
4)Used python scripting to extract the required content.
