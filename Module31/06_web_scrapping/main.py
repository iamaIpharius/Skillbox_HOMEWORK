import re
import requests

url = 'http://www.columbia.edu/~fdc/sample.html'

r = requests.get(url)

pattern = r'>.+h3'

list_of_h3 = re.findall(pattern, r.text)

names_of_h3 = []
for elem in list_of_h3:
    names_of_h3.append(elem[1:-4])
print(names_of_h3)
