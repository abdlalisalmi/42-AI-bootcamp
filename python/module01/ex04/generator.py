from random import randint


def generator(text, sep, option=None):
    '''Option is an optional arg, sep is mandatory'''

    if not isinstance(text, str) or not option in ['shuffle', 'unique', 'ordered', None]:
        return ["ERROR"]

    text = text.split(sep)
    if option == 'shuffle':
        for i in range(len(text)):
            index = randint(0, len(text) - 1)
            target = randint(0, len(text) - 1)
            text[index], text[target] = text[target], text[index]

    elif option == 'unique':
        result = []
        for word in text:
            if word not in result:
                result.append(word)
        text = result

    elif option == 'ordered':
        while True:
            sort = False
            for i in range(len(text) - 1):
                if text[i] > text[i + 1]:
                    text[i], text[i + 1] = text[i + 1], text[i]
                    sort = True
            if not sort:
                break
            
    return text





if __name__ == '__main__':
    text = "Le Lorem Ipsum est simplement du faux texte."
    for word in generator(text, sep=" ", option="ordered"):
        print(word)