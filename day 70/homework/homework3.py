#3) შექმენი ფუნქცია რომელსაც პარამეტრად გადაეცემა რიცხვების სია, ამ სიიდან უნდა ამოიღოს მხოლოდ 50 ზე მეტი რიცხვები და დააბრუნოს როგორც ახალი სია

def number_sum(numbers):
    numbers_more_50 =[]
    for i in numbers:
        if i > 50:
             numbers_more_50.append(i)
    return numbers_more_50


print(number_sum([51,10,40,70]))