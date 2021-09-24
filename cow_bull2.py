import random
def rand_om():
    name=input("enter the your_name:--")
    print("***** welcome****",name)
    num=set()
    i=1
    while i<=5:
        num.add(random.randint(0,9))
        if len(num)!=5:
            num.add(random.randint(0,9))
        if len(num)==5:
            break
        i=i+1
    list1=list(num)
    print(list1)
    
    index=0
    user_chance=9
    cow=0
    bull=0
    list2=[]
    list3=[]
    while user_chance>=1:
        user_choice=int(input("enter the guess number:--"))
        user_position=int(input("enter the position:--"))
        list3.append(user_position)
        print("you have only ",user_chance,"chances left")
        # print("your position is wrong")
        if user_choice in list1:
            list2.append(user_choice)
            
            if list3[index]==list1.index(user_choice):
                bull+=1
                print(bull,"bull")
            else:
                cow+=1
                print(cow,"cow")
        if len(list2)==len(list1)==len(list3)==5:
            break
        user_chance-=1
        index+=1
    print(list2)
    print(list3)
    # print(cow)
    # print(bull)

    if cow>=1 :
        print("losser")
    else:
        print("***** congratulations",name, "you have*** ",bull,"bulls")
        print("*** you are win****")
    

    user_play_again=input("enter weather you want to play game again or not: yes/no*****")
    if user_play_again=="yes":
        rand_om()
    else:
        return "exit"

print(rand_om())