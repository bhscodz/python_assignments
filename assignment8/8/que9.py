import re
punctuations = r'[.,!?;:()]'
date = r'\d{1,2}[-/]\d{1,2}[-/]\d{3,4}|\d{3,4}[-/]\d{1,2}[-/]\d{1,2}[-/]'
urls = r'https?://[^$\s/.?#].[^\s]'
email = r'[a-zA-Z0-9]+@[a-zA-Z0-9]+.[a-zA-Z]{2,}'
number = r'(\d{1,3}(?:,\d{3})*(?:.\d{1,2})?)'
social_ids = r'@[a-zA-Z0-9_]+'
gujarati_text = r'[\u0900-\u097F]+'
pattern = [punctuations,date,urls,email,number,social_ids,gujarati_text]
combined_pattern = '|'.join(pattern)
def tokenizer(text):
    tokens = []
    for patterns in pattern:
        matches = re.findall(patterns,text)
        tokens.extend(matches)
    return tokens
text = '''भारत को 15/08/1947 में आजादी मिली'''
tokens = tokenizer(text)
print(tokens)