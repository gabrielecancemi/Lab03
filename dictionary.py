class Dictionary:
    def __init__(self):
        self._dict = list()

    def loadDictionary(self,path):
        f = open(path, 'r', encoding="utf8").readlines()
        for l in f:
            self._dict.append(l.strip())

    def printAll(self):
        for w in self.dict:
            print(w)



    @property
    def dict(self):
        return self._dict

