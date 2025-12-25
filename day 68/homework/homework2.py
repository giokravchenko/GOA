#2) დაწერე ფუნქცია სახელად char_b, რომელიც იღებს string თავის ერთადერთ არგუმენტად და აბრუნებს სტრიქონში დიდი "B" სიმბოლოების რაოდენობას.

# text = "BiBilashvili"
# count = 0
# for i in text:
#     if i == "B":
#         count+=1

# print("დიდი ბიების რაოდენობა არის:",count)

def char_b(text):
    count = 0
    for i in text:
        if i == "B":
            count+=1
    return count

countb = char_b(input("enter text: ")) 
print("დიდი ბიების რაოდენობაა: ",countb)