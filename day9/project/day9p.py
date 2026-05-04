import os
import re
from datetime import datetime
import time
import math

root = "Mi_Gran_Directorio"

pattern = r"N[a-zA-Z]{3}-\d{5}"

found = []

start_time = time.time()

for folder, subfolders, files in os.walk(root):
    for file in files:
        if file.endswith(".txt"):
            file_path = os.path.join(folder, file)

            with open(file_path, "r") as f:
                text = f.read()

                match = re.search(pattern, text)
                if match:
                    found.append((file, match.group()))

end_time = time.time()

duration = math.ceil(end_time - start_time)

today = datetime.now().strftime("%d/%m/%y")

print("----------------------------------------------------")
print(f"Search date: {today}\n")

print("FILE\t\tSERIAL NUMBER")
print("-------\t\t-------------")

for file, serial in found:
    print(f"{file}\t{serial}")

print(f"\nTotal found: {len(found)}")
print(f"Search duration: {duration} seconds")
print("----------------------------------------------------")