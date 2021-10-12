from textwrap import wrap

def currencyFormater (num):
    list = wrap(str(num)[::-1], 3)
    return ','.join(list)[::-1]

#print (currencyFormater(12345678))