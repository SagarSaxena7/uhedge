number = input("phone: ")
dictionary = {
    "1": "one"
    "2": "two"
    "3": "three"
    "4": "four"
}
for ch in number:
    output += dictionary.get(ch)
print(output)