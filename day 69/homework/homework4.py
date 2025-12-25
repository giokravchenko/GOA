#4)შექმენით ფუნქცია რომელსაც გადაეცემა რენდომ სახელების სია , შემდეგ ამ ფუნქციამ უნდა დააბრუნოს მხოლოდ ის სახელები რომლებიც შეიცავენ 5 ან მეტ ასობგერას

def printer(names):
    my_list =[]
    for saxeli in names:
        if len(saxeli) >= 5:
            my_list.append(saxeli)
print(printer(['giorgi','luka','mariami','iriska','naza']))