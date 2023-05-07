import random

with open("index.bin", "ab") as f:
        aa = random.randint(10,99)
        f.write(aa)
