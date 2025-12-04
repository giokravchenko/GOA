#2)while loop-ის მეშვეობით შექმენი თამაში სადაც მომხმარებელმა უნდა გამოიცნოს ჩვენი ჩაფიქრებული რიცხვი , თუ გამოიცნობს დაიბეჭდოს "ყოჩაღ შენ ეს შეძელი" , თუ ვერ გამოიცნობს უთხრას რომ ახლიდან სცადე , 

number = 100

user =int(input("enter number: "))

while user != number:
    user =int(input("number is inccorect,please try agayn: "))
   

print("ყოჩაღ შენ ეს შეძელი")