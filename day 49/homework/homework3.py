#1))მომხმარებელი შემოატანინე ორ რიცხვს. უნდა დაწერო ისეთი პროგრამა რომელიც გაიგებს ეს რიცხვი მეტია მეორეზე ნაკლებია თუ ტოლია

num1 =int(input("enter number:"))
user =input("enter(//,*,+,-)")
num2 =int(input("enter number:"))

if user == "//":
    print(num1//num2)
elif user == "*":
    print(num1*num2)
elif user == "+":
    print(num1+num2)
elif user == "-":
    print(num1-num2)
