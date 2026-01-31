text=input("Enter a string: ")
vowels = ['a', 'e', 'i', 'o', 'u']
count=0
for char in text.lower():
    if char in vowels:
        count=count+1
print(f"{text} has {count} vowels")