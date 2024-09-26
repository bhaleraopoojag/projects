menu={
    'Black Tea':10,
    'Green Tea':20,
    'White Tea':25,
    'Pizza':85,
    'Burger':100,
    'Vada Pav':15

}
print("Welcome to Restaurant")
print("plz place the order")

ord_cnt=0
item=input("Enter the items from menu card:")
if item in menu:
    ord_cnt+=menu[item]
    print(ord_cnt)
else:
    print(f"{item} is not available")

ord_another=input("Any thing else(YES/NO)")
if ord_another=='YES':
    item2=input("Enter the item=")
    if item2 in menu:
        ord_cnt+=menu[item2]
    print(f"{item2} added")
    print(f'{item2} is not avilable')
print(f"You have to pay {ord_cnt} ..")
