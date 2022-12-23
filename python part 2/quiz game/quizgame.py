def new_game():
    gusses=[]
    correct_gusses=0
    question_num=0

    for key in questions:
        print("------------------------------")
        print(key)
        print("------------------------------")
        for i in option[question_num]:            
            print(i)
        guss=input("Enter (A,B,C or D ): ").upper()
        gusses.append(guss)
        
        correct_gusses+=check_answer(questions.get(key),guss)
        question_num+=1
    display_score(correct_gusses,gusses)
#------------------------------------------------
def check_answer(answer,guess):

    if answer==guess:
        print("correct!")
        return 1        
    else :
        print("wrong!")
        return 0
#------------------------------------------------
def display_score(correct_gusses,gusses):
    print("------------------------------")
    print("Result")
    print("Answer ",end="")
    for i in questions:
        print(questions.get(i),end=" ")
    print()    
    print("Guesses ",end="")
    for i in gusses:
        print(i,end=" ")
    print() 
    score= int((correct_gusses/len(questions))*100)
    print("Your score is : "+str(score)+"%")
#------------------------------------------------
def play_agane():
    response=input("Do you want to play agane ? (yes or no)").upper()
    if response=="YES":
        return True
    else:
        return False    

questions={ 
"Who creat python ? : " : "A" ,
"What years python created ? : " :  "B",
"python is trubited to which comedy group ? : " : "C",
"Is earth round ? : " : "A"
}

option=[
["A. Guido van rossum","B.Elon Musk","C.Bill Gates","D.Mark Zuckerburg"],
["A.1989","B.1991","C.2000","D. 2016"],
["A.Lonly Island","B.Smash","C.Monty Python","D.SNL"],
["A.True","B.False","C.sometimes","D.what is Earth?"]]

new_game()

while play_agane():
     new_game()


print("Byee")








