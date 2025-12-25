#5)შექმენით ფუნქცია რომლსაც გადაეცემა რენდომ რიცხვების სია , ამ ფუნქციამ უნდა დააბრუნს სხვა სია სადაც ეს ელემენტები გაორმაგდებიან([1, 4, 7] → შედეგი:[2, 8, 14])

def gaormageba(numbers):
    numbers_2 =[]
    for i in numbers:
        numbers_2.append(i*2)

    return numbers_2

print(gaormageba([2,4,5]))