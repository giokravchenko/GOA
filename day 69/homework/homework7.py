#7)შექმენით ფუნქცია რომელიც შეამოწმებს სიტყვას პალინდრომია თუ არა( პალინდრომი - სიტყვა რომელიც ერთნაირად იკითხება თავიდანაც და ბოლოდანაც მაგ. Level , Ana და ა.შ.)

def paliindrom(word):
    word =word.lower()
    if word == word[::-1]:
        return "პალინდრომიაა"
    else:
        return "არაა პალინდრმი"
    
print(paliindrom("level"))