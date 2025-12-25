#მომხმარებელი შემოიყვანს ქულას (0–100).თუ ქულა >= 90 → ბეჭდავს: "A" თუ >= 80 → "B" თუ >= 70 → "C" თუ >= 60 → "D"

user =int(input("enter number:"))

if 90 == user:
    print("A")
elif 80 == user:
    print("B")
elif 70 == user:
    print("C")
elif 60 == user:
    print("D")