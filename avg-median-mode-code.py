

def amm():
        testNum = int(input("How many test scores do you want to record? "))
        score = []
        a = 0
        while a < testNum:
                getScore = int(input("What's your test score? "))
                score.append(getScore)
                a+=1
        avg = float(sum(score))/(len(score))
        print("Your average test score is ",str(avg)+".")
        mode = 0
        d = 0
        for x in score:
                c = score.count(x)
                if c > d:
                        d = c
                        mode = x
                else:
                        d = d
        print("Your mode is",str(mode)+".")
        if len(score)%2 ==0:
                e = score[int((len(score))/2-1)]
                f = score[int((len(score))/2+1)]
                print("The median is", str(e),"and",str(f)+".")
        else:
                g = score[int((len(score))/2-1)]
                h = score[int((len(score))/2)]
                if g < h:
                        print("The median is ",str(g)+".")
                else:
                        print("The median is ",str(h)+".")
amm()


