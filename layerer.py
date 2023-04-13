import random
import string
from main import obf
import os

start_file = "example.py"
output_file = "processed.py"
layer_count = 500
signature = ".obf"
working_directory = "."

os.chdir(working_directory)
accuracy = 1 + round(layer_count / 10**len(str(layer_count))) + len(str(layer_count))
n = [f"part{_}.py" for _ in range(layer_count)]
current = n.pop(0)
print("obfuscating", start_file, "to", current)
obf(start_file, current, "".join(random.choices(string.ascii_letters, k=accuracy))+signature)
for file in n:
    print("obfuscating", current, "to", file)
    obf(current, file, "".join(random.choices(string.ascii_letters, k=accuracy))+signature)
    os.remove(current)
    print("cleaning up", current)
    current = file
print("renaming", current, "to", output_file)
os.rename(current, output_file)
