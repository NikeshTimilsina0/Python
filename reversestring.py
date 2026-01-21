text = input("Enter a string: ")
reversed_text = ""

# Start at the last index, end at 0, move by -1 each time
for i in range(len(text)-1, -1 , -1):
    reversed_text = reversed_text + text[i]

print(f"The reversed string is: {reversed_text}")