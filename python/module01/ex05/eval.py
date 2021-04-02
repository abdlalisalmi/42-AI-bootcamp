



class Evaluator:

    @staticmethod
    def zip_evaluate(coefs, words):
        if len(coefs) != len(words):
            return (-1)

        sum = 0
        for c, w in zip(coefs, words):
            sum += c * len(w)
        return sum

    @staticmethod
    def enumerate_evaluate(coefs, words):
        if len(coefs) != len(words):
            return (-1)
        
        sum = 0
        for i, w in enumerate(words, 0):
            sum += coefs[i] * len(w)
        return sum


if __name__ == '__main__':
    words = ["Le", "Lorem", "Ipsum", "est", "simple"]
    coefs = [1.0, 2.0, 1.0, 4.0, 0.5]

    val = Evaluator.zip_evaluate(coefs, words)
    print(val)
    val = Evaluator.enumerate_evaluate(coefs, words)
    print(val)