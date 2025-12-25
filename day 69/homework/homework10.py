#10)ფუნქცია რომელიც იღებს რიცხვების სიას და ბეჭდავს მხოლოდ დადებითი რიცხვების ჯამს


def funqcion_numbers(number):
    jami = 0
    for i in number:
        if i >= 0:
             jami+=i
    return jami
    
print(funqcion_numbers([-1,-2,3,3]))