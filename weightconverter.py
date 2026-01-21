try:
    # 1. Handle non-numeric input immediately
    weight = float(input('Enter your weight: '))
    weight_type = input('Unit: (L)bs or (K)gs? ').strip().lower()

    # 2. Use a cleaner check for unit types
    if weight_type in ['l', 'lb', 'lbs']:
        kg = weight * 0.453592
        lbs = weight
    elif weight_type in ['k', 'kg', 'kgs']:
        kg = weight
        lbs = weight * 2.20462
    else:
        # 3. Raise an error for invalid strings to jump to the except block
        raise ValueError("Invalid unit type.")

    # 4. Standardized Output using f-strings for clean decimals
    print(f"\nResults:\n{'-'*10}")
    print(f"Weight in KG:  {kg:.2f}")
    print(f"Weight in LBS: {lbs:.2f}")

except ValueError as e:
    print(f"Input Error: {e} Please enter a number for weight and L or K for unit.")
    
    
# weight=int(input("Enter your weight: "))
# weight_type=input("(L)bs or K(gs): ")
# if weight_type.lower()=='l' or weight_type.lower()=='lb' or weight_type.lower()=='lbs' :
#     weight_in_kg=weight*0.453592
#     print("Weight in kg:",weight_in_kg)
#     print("Weight in lbs:",weight)
# else:
#     weight_in_lbs=weight*2.205
#     print("Weight in kg:",weight)
#     print("Weight in lbs:",weight_in_lbs)