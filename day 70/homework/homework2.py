#2) შექმენი ფუნქცია რომელიც გაიგებს მომხმარებელი სრულწლოვანია თუ არასრულწლოვანი

def age_test(age):
    if 18 <= age:
        return "you are 18+"
    else:
        return "you are -18 age"
    

print(age_test(int(input("enter age: "))))