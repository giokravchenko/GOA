#დაწერე ფუნქცია greet(name, age) თუ ასაკი ≥ 18 → "გამარჯობა {name}, თქვენ ზრდასრულები ხართ" თუ ასაკი < 18 → "გამარჯობა {name}, თქვენ ჯერ არასრულწლოვანი ხართ"გამოიყენე f-string


def greet(name, age):
    if age < 18:
        return f"hello {name} this age {age} is not 18+"             
    else:
        return f"hello {name} youre are 18+!"
    
print(greet("giorgi",18))