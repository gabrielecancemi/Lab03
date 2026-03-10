import time

import multiDictionary as md


class SpellChecker:

    def __init__(self):
        pass

    def handleSentence(self, txtIn, language):
        multi = md.MultiDictionary()
        words = replaceChars(txtIn.lower()).split(" ")


        start_time = time.perf_counter()
        phrase = multi.searchWord(words, language)
        end_time = time.perf_counter()
        start_time_l = time.perf_counter()
        phrase = multi.searchWordLinear(words, language)
        end_time_l = time.perf_counter()
        start_time_d = time.perf_counter()
        phrase = multi.searchWordDichotomic(words, language)
        end_time_d = time.perf_counter()


        i = 0
        for w in phrase:
            if not w.corretta:
                print(w)
                i = i + 1
        print(i)
        print(f"Normal: + {end_time-start_time}")
        print(f"Linear: + {end_time_l-start_time_l}")
        print(f"Dichotomic: + {end_time_d-start_time_d}")



    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
 chars = "\\`*_{}[]()>#+-.!$%^;,=_~"
 for c in chars:
    text = text.replace(c, "")
 return text