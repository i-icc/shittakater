from random import randint

class Markov:
    def __init__(self):
        self.START = "start_code"
        self.END = "end_code"
        self.model = {self.START:{"count":0,"words":[]}}

    def reset(self):
        self.model = {self.START:{"count":0,"words":[]}}

    def lean(self,texts):
        for text in texts:
            pre_word = self.START
            for word in text:
                if pre_word in self.model:
                    self.model[pre_word]["count"] += 1
                    self.model[pre_word]["words"].append(word)
                else:
                    self.model[pre_word] = {"count":1,"words":[word]}
                pre_word = word
            if pre_word in self.model:
                self.model[pre_word]["count"] += 1
                self.model[pre_word]["words"].append(self.END)
            else:
                self.model[pre_word] = {"count":1,"words":[self.END]}

    def make(self):
        pre_word = self.model[self.START]["words"][randint(0,self.model[self.START]["count"] - 1)]
        result = pre_word
        for i in range(280): 
            pre_word = self.model[pre_word]["words"][randint(0,self.model[pre_word]["count"] - 1)]
            if pre_word == self.END: break
            result += pre_word
        return result

class Markov_2:
    def __init__(self):
        self.START = "start_code"
        self.END = "end_code"
        self.model = {self.START:{"count":0,"words":[]}}

    def reset(self):
        self.model = {self.START:{"count":0,"words":[]}}

    def lean(self,texts):
        for text in texts:
            pre_word = self.START
            key = pre_word
            for word in text:
                if key in self.model:
                    self.model[key]["count"] += 1
                    self.model[key]["words"].append(word)
                else:
                    self.model[key] = {"count":1,"words":[word]} 
                key = (pre_word,word)
                pre_word = word
            if key in self.model:
                self.model[key]["count"] += 1
                self.model[key]["words"].append(self.END)
            else:
                self.model[key] = {"count":1,"words":[self.END]}

    def make(self):
        word = self.model[self.START]["words"][randint(0,self.model[self.START]["count"] - 1)]
        result = word
        key = (self.START,word)
        pre_word = word
        for i in range(280): 
            word = self.model[key]["words"][randint(0,self.model[key]["count"] - 1)]
            if word == self.END: break
            key = (pre_word,word)
            pre_word = word
            result += word
        return result

def main():
    mar = Markov_2()
    mar.lean([['とりあえず', 'あと', '2', '回', 'は', '寿司', '行く', '予定', 'が', 'ある', 'から', '、', '、', '待っ', 'て', 'ろ', '寿司', 'モル', 'カー']])
    print(mar.model)
    print(mar.make())

if __name__ == "__main__":
    main()