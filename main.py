def sum1(list1):
    n =0
    for i in list1:
        n += int(i)
    return n

def mul(list1):
    n=1
    for i in list1:
        n = n*i
    return n

def rev(str1):
    revstr= ''
    for i in str1[::-1]:
        revstr += i
    return revstr

def cntupperlower(str1):
    atoz = 'abcdefghijklmnopqrstuvwxyz'
    uppercase =atoz.upper()
    lowercase = atoz.lower()
    uppercnt =0
    lowercnt =0
    for i in str1:
        if i in uppercase:
            uppercnt +=1
        elif i in lowercase:
            lowercnt+=1
        else:
            pass
    return (uppercnt, lowercnt)

def uniquelist(list1):
    list1 = set(list1)
    return list1

def factorial(int1):
    int1 = int(int1)
    list1 =[]
    str1=''
    while int(int1)>0:
        list1.append(int1)
        int1 -=1
    for i in list1[::-1]:
        str1=str(i)+'x'+str1
    return str1.strip('x')

def everyletter(str1):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    str1 =str1.lower()
    list1 = []
    for i in str1:
        if (i not in list1) and (i in letters):
            list1.append(i)
    if len(list1)==26:
        return True
    else:
        return False