from abc import ABC


class Count(ABC):
    def __init__(self, address):
        self.address = address

    def calculateFreqs(self, address):
        pass


class ListCount(Count):
    def __init__(self, address):
        Count.__init__(self, address)

    def calculateFreqs(self, address):
        f = open(address)
        x = f.readline()
        x = x.split()
        x2 = []
        for i in x:
            if i not in x2:
                x2.append(i)
        for i in range(0, len(x2)):
            print("Frequency of ", x2[i], "is :", x.count(x2[i]))


class DictCount(Count):
    def __init__(self, address):
        Count.__init__(self, address)

    def calculateFreqs(self, address):
        f = open(address)
        x = f.readline()
        words_dict = {}
        for word in x.split():
            words_dict[word] = words_dict.get(word, 0) + 1
        for key in words_dict:
            print("{} : {}".format(key, words_dict[key]))


address1 = r"C:\Users\C605\Desktop\strange.txt"
f1=ListCount(address1)
f1.calculateFreqs(address1)

f2 = DictCount(address1)
f2.calculateFreqs(address1)
