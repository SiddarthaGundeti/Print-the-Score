d=int(input())
score=0
if d<=50:
    score=score+(d*3) 
elif d<=100:
    score=score+(50*3)+((d-50)*5)
elif d<=200:
    score=score+(50*3)+(50*5)+((d-100)*6)
else:
    remaining=d-200
    distance_score=remaining*10
    third_above_100=100*6
    next_50_to_100=50*5
    first_50=50*3
    total_score=third_above_100+next_50_to_100+first_50
    score=distance_score+total_score
score+=100
print(score)
