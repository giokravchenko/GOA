#მომხმარებელი შეყავს რიცხვი n. while ციკლით დაითვალე 1+2+3+…+n, ანუ n-მდე რიცხვების ჯამი.

user =int(input("enter number:"))

i = 1

jami = 0



while i <= user:
    jami+=i
    i+=1
    
    
print(jami)