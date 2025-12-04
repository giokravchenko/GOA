#3)For ციკლის გამოყენებით გამოთვალე 1 დან 99 მდე ყველა კენტი რიცხვისჯამი

# i = 1

# x = 99
 
# jami = 0
# while i <= x:
#     jami+=i
#     i+=2

# print(jami)

jami = 0

for i in range(1,100,2):
    jami+=i

print(jami)