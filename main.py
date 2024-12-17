import cv2

from extraction import skew_correct, extract_text
import spacy
spacy.prefer_gpu()
model = spacy.load('en_core_web_trf')

image = cv2.imread("data/Sample-Job-Biodata-Format-724x1024.jpg")
processed_image = skew_correct(image)
text = extract_text(processed_image)
print("\n")
words = []
for i in text:
    words.append(i[1])
ocr_string = " ".join(words)
doc = model(ocr_string)
for entity in doc.ents:
    print(entity.text) if entity.label_ == "PERSON" else None
