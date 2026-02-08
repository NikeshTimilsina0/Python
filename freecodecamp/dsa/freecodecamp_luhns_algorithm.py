def verify_card_number(card_num):
    
    string = card_num.replace('-', '').replace(' ', '')
    string=string[::-1]
    string=[int(x) for x in string]
    for i in range(1,len(string),2):
        string[i]*=2
        if string[i]>9:
            string[i]=string[i]%10+1
    total=sum(string)
    if total%10==0:
        return f'{card_num} VALID!'
    else:
        return f'{card_num} INVALID!'

# Test 1: Standard invalid number from the lab description
print(f"Test 1: {verify_card_number('453914881')}") 
# Expected: INVALID!

# Test 2: Standard valid number
print(f"Test 2: {verify_card_number('453914889')}") 
# Expected: VALID!

# Test 3: Number with dashes (The "Wall of Fire" test)
print(f"Test 3: {verify_card_number('4111-1111-1111-1111')}") 
# Expected: VALID!

# Test 4: Number with spaces
print(f"Test 4: {verify_card_number('1234 5678 9012 3456')}") 
# Expected: INVALID!