import base64
import sys

with open(sys.argv[1], 'r') as file:
    data = file.read()

for i in range (0, 50):
    data = base64.b64decode(data)
print(data)
file.close()        