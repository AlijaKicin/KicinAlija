import re

string = str(input("Unesite neki string: "))
string = string.lower()

regex = r"^m.*[0-5]+.*\s.*k$"

result = re.findall(regex, string)

if result:
    print("Podudaranje")
else:
    print("Nema podudaranja")
