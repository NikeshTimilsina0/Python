prices=[1,3,5,2,7,453,763,645,8484,5,3]
new_price=[]
for p in prices:
    if p not in new_price:
        new_price.append(p)
print(new_price)