questions=[
["which language use in python?",
"python","php","java","none",4]
["which language use in python?",
 "python","php","java","none",4]
["which language use in python?",
 "python","php","java","none",4]
["which language use in python?",
 "python","php","java","none",4]
["which language use in python?",
 "python","php","java","none",4]
["which language use in python?",
 "python","php","java","none",4]
["which language use in python?",
 "python","php","java","none",4]
["which language use in python?",
 "python","php","java","none",4]
["which language use in python?"
 ,"python","php","java","none",4]
]

levels=[1000,2000,3000,4000,5000,6000,7000,8000,9000,100000]
money=0
for i in range(0,len(questions)):
    question=questions[i]
    print(f"question for rs.{levels[i]}")
    print("a.{question[1]} b.{question[2]}")
    print("c.{question[3]} d.{question[4]}")
    reply=int(input("enter the answer(1-4)"))
    if(reply==questions[-1]):
        print(f"current answer is.{levels[i]}")
        if(i==4):
            money==5000
        elif(i == 8):
            money==9000
    
    else:
        print("wrong answer")
        break
