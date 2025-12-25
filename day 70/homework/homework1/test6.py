#კითხულობს რიცხვს (input())თუ რიცხვი ლუწი → "რიცხვი <რიცხვი> არის ლუწი" თუ კენტი → "რიცხვი <რიცხვი> არის კენტი"

user =int(input("enter number:"))

if user % 2 == 1:
    print(f"the number {user} are :კენტი")
else:
    print(f"the number {user} are :ლუწი")