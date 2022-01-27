import operator
import collections

n1 =  [3, 30, 34, 5, 9]

def dictionarize(n) :
    
    if n>0 and n<10 :
        return (n/100)*100
    elif n>=10 and n<100 :
        return (n/100)*10
    elif n>=100 and n<1000 :
        return (n/100)


def solution(numbers):
    answer = ''
    list1 = []
    dict1 = {"Key":[], "Value":[]}

    for j in range(len(numbers)) :
        dict1["Key"].append(dictionarize(numbers[j]))
        dict1["Value"].append(numbers[j])

    #print(dict1)
    #dict(sorted(dict1.items(),key=operator.itemgetter(1), reverse=True))
    ordered_dict = collections.OrderedDict(sorted(dict1.items()))
    print(ordered_dict)
    
    return answer
