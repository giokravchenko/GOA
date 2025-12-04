#1)დახატე ორი ერთმანეთის პარარელური ოთკუთხედი , გამოიყენე turtle , ეცადე რაც შეიძლება ნაკლები ხაზი კოდი დაგჭირდეს,უნდა გამოიყენო ფუნქციები , if&else ები და ა.შ. 
from turtle import *

def kvadrat():
    for i in range(4):
        forward(200)
        left(90)


kvadrat()
penup()
goto(200,0)
pendown()
kvadrat()