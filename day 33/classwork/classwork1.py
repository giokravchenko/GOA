#1)მომხმარებელს შემოატანინე სახელი , თუ ეს სახელი ტოლია "giorgi" - ს , ამ შემთხვევაში დაბეჭდოს 10 ჯერ "giorgi" , თუ სახელი არ იქნება "giorgi",დაბეჭდოს რომ შენ ხარ უცხო

user_name ="გიორგი"

name =input("თქვენი სახელი:")

while user_name != name:
    name =input("თქვენ ხართ უცხო!:")


for i in range(10):
    print(user_name)