import dictionary as d
import richWord as rw


class MultiDictionary:

    def __init__(self):
        self.dictionaries = dict()
        self.dictionaries["italian"] = d.Dictionary()
        self.dictionaries["english"] = d.Dictionary()
        self.dictionaries["spanish"] = d.Dictionary()
        self.dictionaries["italian"].loadDictionary("resources/Italian.txt")
        self.dictionaries["english"].loadDictionary("resources/English.txt")
        self.dictionaries["spanish"].loadDictionary("resources/Spanish.txt")

    def printDic(self, language):
        self.dictionaries[language].printAll()

    def searchWord(self, words, language):
        phrase = list()
        for word in words:
            w = rw.RichWord(word)
            phrase.append(w)
            if word in self.dictionaries[language].dict:
                w.corretta = True
            else:
                w.corretta = False
        return phrase

    def searchWordLinear(self, words, language):
        phrase = list()
        for word in words:
            w = rw.RichWord(word)
            phrase.append(w)
            w.corretta = False
            for k in self.dictionaries[language].dict:
                if k == word:
                    w.corretta = True
                    break
        return phrase


    def searchWordDichotomic(self, words, language):
        phrase = list()
        dict1 = self.dictionaries[language].dict
        for word in words:
            dict = dict1
            w = rw.RichWord(word)
            phrase.append(w)
            w.corretta = False
            l = 2
            while (not w.corretta) and (l > 1):
                l = int(len(dict) / 2)
                if dict[l] == word:
                    w.corretta = True
                    break
                elif word > dict[l]:
                    dict = dict[(l+1):]
                else:
                    dict = dict[:(l-1)]


        return phrase


    @classmethod
    def replaceChars(text):
        chars = "\\`*_{}[]()>#+-.!$%^;,=_~"
        for c in chars:
            text = text.replace(c, "")
        return text


