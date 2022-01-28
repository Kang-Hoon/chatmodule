#numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
#hand = 'right'

def dleft(a,b) :
    if (a==1 and b==2) or (a==4 and b==5) or (a==7 and b==8) :
        distl = 1
        return distl
    elif (a==2 and b==5) or (a==5 and b==2) or (a==5 and b==8) or(a==8 and b==5) or (a==8 and b==0) or (a==0 and b==8) :
        distr = 1
        return distl
    elif (a==1 and b==5) or (a==4 and b==2) or (a==4 and b==8) or (a==7 and b==5) or (a==7 and b==0) :
        distl = 2
        return distl
    elif (a==1 and b==8) or (a==7 and b==2) or (a==4 and b==0) :
        distl = 3
        return distl
    else :
        distl = 2
        return distl

def dright(a,b) :
    if (a==3 and b==2) or (a==6 and b==5) or (a==9 and b==8) :
        distr = 1
        return distr
    elif (a==2 and b==5) or (a==5 and b==2) or (a==5 and b==8) or(a==8 and b==5) or (a==8 and b==0) or (a==0 and b==8) :
        distr = 1
        return distr
    elif (a==3 and b==5) or (a==6 and b==2) or (a==6 and b==8) or (a==9 and b==5) or (a==9 and b==0) :
        distr = 2
        return distr
    elif (a==3 and b==8) or (a==9 and b==2) or (a==6 and b==0) :
        distr = 3
        return distr
    else :
        distr = 2
        return distr

def lrc(n) :
    if n==1 or n==4 or n==7:
        return 1
    elif n==3 or n==6 or n==9:
        return 2
    else :
        return 3

def solution(numbers, hand):
    answer = ''
    currl = [0]
    currr = [0]
    
    for i in numbers :
        lrc(i)
        print(lrc(i))
        if lrc(i)==1 :
            answer += 'L'
            currl.append(i)
        elif lrc(i)==2 :
            answer += 'R'
            currr.append(i)
        elif lrc(i)==3 :
            if dright(currr[-1],numbers[i]) < dleft(currl[-1],numbers[i]) :
                answer += 'R'
                currr.append(i)
            elif dright(currr[-1],numbers[i]) > dleft(currl[-1],numbers[i]) :
                answer += 'L'
                currl.append(i)
            elif dright(currr[-1],numbers[i]) == dleft(currl[-1],numbers[i]) :
                answer += 'R'
                currr.append(i)
            #answer += 'R'
            #cr.append(i)
    return answer
