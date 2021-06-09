from janome.tokenizer import Tokenizer

t = Tokenizer()

def morphological_analysis(texts):
    result = [[token.surface for token in t.tokenize(text)] for text in texts]
    return result

def main():
    print(morphological_analysis(["私は猫です","すもももももももものうち"]))

if __name__ == "__main__":
    main()