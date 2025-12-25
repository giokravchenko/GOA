#3)შექმენით ფუნქცია რომელსაც გადაეცემა რიცხვების სია , ამ ფუნქციამ უნდა დააბრუნოს ამ რიცხვების ჯამი

def numbers_sum(number_list):
    jami = 0
    for i in number_list:
        jami+=i

    return jami

print(numbers_sum([100,10,20,40]))