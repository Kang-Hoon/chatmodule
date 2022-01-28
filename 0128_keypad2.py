import math

dict_pad = {1: [0, 0], 2: [0, 1], 3: [0, 2],
            4: [1, 0], 5: [1, 1], 6: [1, 2],
            7: [2, 0], 8: [2, 1], 9: [2, 2],
            '*':[3, 0], 0: [3, 1], '#': [3, 2]}

def lrc(n) :
    if n==1 or n==4 or n==7:
        return 1
    elif n==3 or n==6 or n==9:
        return 2
    else :
        return 3
    
def distance(a,b) :
    return math.sqrt((dict_pad[a][0]-dict_pad[b][0])**2 + (dict_pad[a][1]-dict_pad[b][1])**2)

def solution(numbers, hand):
    answer = ''
    currl = ['*']
    currr = ['#']
    
    for i in numbers :
        lrc(i)
        print(lrc(i))
        if lrc(i)==1 :
            answer += 'L'
            currl.append(i)
        elif lrc(i)==2 :
            answer += 'R'
            currr.append(i)
        elif hand=="right" and lrc(i)==3 :
            if distance(i,currl[-1]) > distance(i,currr[-1]) :
                answer += 'R'
                currr.append(i)
            elif distance(i,currl[-1]) < distance(i,currr[-1]) :
                answer += 'L'
                currl.append(i)
            elif distance(i,currl[-1]) == distance(i,currr[-1]) :
                answer += 'R'
                currr.append(i)
        elif hand=="left" and lrc(i)==3 :
            if distance(i,currl[-1]) > distance(i,currr[-1]) :
                answer += 'R'
                currr.append(i)
            elif distance(i,currl[-1]) < distance(i,currr[-1]) :
                answer += 'L'
                currl.append(i)
            elif distance(i,currl[-1]) == distance(i,currr[-1]) :
                answer += 'L'
                currl.append(i)
                
    return answer
