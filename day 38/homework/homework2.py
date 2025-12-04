#2) მომხმარებელს შემოატანინე სიტყვები მანამდე სანამ ეს სიტყვა არ იქნება "Stop" , ხოლო როდესაც მომხმარებელი შემოიყვანს სიტყვა "Stop" - ს ციკლი შეწყდეს და პროგრამამ დაითვალოს მანამდე რამდენი სიტყვა ჰქონდა შემოტანილი.

user =input("enter word:")

number = 0

while user != "stop":
    user =input("word is incorect,please try again:")
    number+=1


print(number)