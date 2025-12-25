#2)შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა სია და ამ სიას გაფილტრავს დაყოფს ორ ნაწილად დადებითებად და უარყოფითებად

def filter_numbers(numbers):
    minus_sia =[]
    plus_sia =[]
    for num in numbers:
        if num < 0:
            minus_sia.append(num)
        else:
            plus_sia.append(num)
    return minus_sia,plus_sia


print(filter_numbers([0,-1,2,10,-2]))