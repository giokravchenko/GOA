#თუ ასაკი ≥ 18:gender == "M" → დაბეჭდოს: "გამარჯობა {name}, თქვენ ზრდასრულ მამაკაცს წარმოადგენთ!" gender == "F" → დაბეჭდოს: "გამარჯობა {name}, თქვენ ზრდასრულ ქალს წარმოადგენთ!" თუ ასაკი < 18 → "გამარჯობა {name}, თქვენ ჯერ არასრულწლოვანი ხართ"

def info(name,age,gender):
    if gender == "M" and age >= 18:
        return f"hello {name} you are adult men!"
    elif gender == "F" and age >= 18:
        return f"hello {name} you are adult women!"
    elif age < 18:
        return f"hello {name} sorry but you are not 18+"
    
print(info("giorgi",20,"M"))