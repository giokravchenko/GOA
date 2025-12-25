#4)შექმენი ფუნქცია რომელიც მომხმარებელს ჰკითხავს რაიმე სიტყვას  ან წინადადებას და ამ სიტყვაში ან წინადადებაში დაითვლის “ა”-ასობგერის რაოდენობას

def A_returner(text):
    count_a = 0
    for i in text:
        if i == "a" or i == "A":
             count_a+=1
        
    return count_a

print(A_returner(input("enter text:")))
