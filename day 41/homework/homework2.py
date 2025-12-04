#2)მომხმარებელს შეჰყავს რიცხვი, დაბეჭდე მისი კვადრატი მანამ, სანამ მომხმარებელი არ შეიყვანს 0-ს.

i = 0

user =int(input("enter number:"))

while i != user:
    print(user,"ის კვადრატი არის",user**2)
    user =int(input("enter number:"))


print(user)
