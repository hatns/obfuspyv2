import random
def obf(target, output, bin = "bin.b"):
    seed = random.randint(0, int("1" + "0"*99))
    random.seed(seed)
    z = open(target)
    s = z.read()
    z.close()
    chars = []
    for char in s:
        chars.append(chr(ord(char) + random.randint(0, 50000)))
    chars = "".join(chars)
    b = chars.encode()
    with open(bin, "wb") as f:
        f.write(b)
    code = f'''import random
from time import time as rseed
with open("{bin}", "rb") as f:
    s = f.read()
x = s.decode("utf-8")
random.seed({seed})
chars = []
for char in x:
    chars.append(chr(ord(char) - random.randint(0, 50000)))
random.seed(rseed())
exec("".join(chars))'''
    with open(output, "w") as f:
        f.write(code)
