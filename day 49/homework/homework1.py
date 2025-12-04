#1))მომხმარებელი შემოატანინე ორ რიცხვს. უნდა დაწერო ისეთი პროგრამა რომელიც გაიგებს ეს რიცხვი მეტია მეორეზე ნაკლებია თუ ტოლია

user_number =int(input("enter number:"))
user_number2 =int(input("enter number:"))

if user_number < user_number2:
    print(user_number,"ნაკლებია",user_number2,"ზე")
elif user_number > user_number2:
    print(user_number,"მეტია",user_number2,"ზე")
elif user_number == user_number2:
    print(user_number,"ტოლია",user_number2,"ზე")