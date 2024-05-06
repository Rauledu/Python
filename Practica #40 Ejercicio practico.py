#string invertido#

string = input("Introduce un string para invertilo: ")
string_reverse =""

for element in string:
    string_reverse = element + string_reverse

print(f"String invertido: {string_reverse}")
