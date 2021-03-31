from string import punctuation


def text_analyzer(*text):
    if len(text) > 1:
        print("ERROR")
        return
    elif len(text) == 1:
        text = list(text)[0]
    elif len(text) == 0:
        text = input("What is the text to analyse?\n>> ")

    values = {
        'uppers': 0,
        'lowers': 0,
        'marks': 0,
        'spaces': 0
    }

    for c in text:
        if c.isupper():
            values['uppers'] += 1
        elif c.islower():
            values['lowers'] += 1
        elif c in punctuation:
            values['marks'] += 1
        elif c == ' ':
            values['spaces'] += 1
    
    print(f"""
The text contains {len(text)} characters:
- {values.get('uppers')} upper letters
- {values.get('lowers')} lower letters
- {values.get('marks')} punctuation marks
- {values.get('spaces')} space
""")
