import string
from nltk.tokenize import word_tokenize
from collections import Counter

text = " From Gongwer OH Report, sounds like leadership still considering library cuts, not considering tax increases. #saveohiolibraries"
lower_case = text.lower()
cleaned_text = lower_case.translate(
    str.maketrans('', '', string.punctuation))
cleaned_text = cleaned_text.strip()

print(cleaned_text)
