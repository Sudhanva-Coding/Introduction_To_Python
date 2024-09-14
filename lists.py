abc = ["Sudhanva", 14, "Coding", 10.26, True, ["Hello", "World"]]
print(abc)
print(type(abc))
import random

wer = ["art", "Maths", "History", "Science", "Computing", "Geography"]
qwe = ["football", "Netball", "cricket", "baseball", "basketball"]
dsa = ["french", "spanish", "German", "portugese", "Cantonese", "Mandarin"]

ads = random.choice(wer)
zcx = random.choice(wer)
fdg = random.choice(dsa)
ghj = random.choice(dsa)
dfj = random.choice(qwe)
fcv = random.choice(qwe)
print("{}, {}, {}, {}, {}, {} is a good combination to be taught in schoool".format(ads, zcx, fdg, ghj, dfj, fcv))