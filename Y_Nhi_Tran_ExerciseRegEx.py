# Y Nhi Tran
# Exercise Web Scraping

import re

# Open the file
file_name = "Index.html"
mode = "r"

with open(file_name, mode) as fp:
    contents = fp.read()

regex = re.compile(r'<li>(.*?)</li>')

output = regex.findall(contents)
out = "\n".join([str(planet) for planet in output])
print(out)


"""
OUTPUT
Pluto
Charon
Eris
Makemake
Ceres
"""