#numbers = [6, 10, 2]
numbers =  [3, 30, 34, 5, 9]
# 자릿수판별 / 첫자리판별

def digit(n) :
    if n>0 and n<10 :
        return int(n)
    elif n>=10 and n<100 :
        return int(n/10)
    elif n>=100 and n<1000 :
        return int(n/100)

def solution(numbers):
    answer = ''
    dnum = []
    for j in range(len(numbers)) :
        dnum.append(digit(numbers[j]))
    dnum.sort(reverse=True)

    numbers.sort(reverse=True)

    temp_list = []

    for i in range(len(numbers)) :
        if digit(numbers[i]) == 9 :
            temp_list.append(str(numbers[i]))
        elif digit(numbers[i]) == 8 :
            temp_list.append(str(numbers[i]))
        elif digit(numbers[i]) == 7 :
            temp_list.append(str(numbers[i]))            
        elif digit(numbers[i]) == 6 :
            temp_list.append(str(numbers[i]))
        elif digit(numbers[i]) == 5 :
            temp_list.append(str(numbers[i]))  
        elif digit(numbers[i]) == 4 :
            temp_list.append(str(numbers[i]))    
        elif digit(numbers[i]) == 3 :
            temp_list.append(str(numbers[i]))
        elif digit(numbers[i]) == 2 :
            temp_list.append(str(numbers[i]))
        elif digit(numbers[i]) == 1 :
            temp_list.append(str(numbers[i]))
            return

    print(temp_list)
    answer = "".join(temp_list)

    return answer
