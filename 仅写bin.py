import random

with open("index.bin", "ab") as f:
        random_data = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))
        f.write(random_data)
