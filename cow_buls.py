import random
def cow_buls():
    name=input("enter the your name=------")
    print("welcwme--------",name,)
    num1=set()
    i=0
    while i<5:
        num1.add(random.randint(0,9))
        if len(num1)!=5:
            num1.add(random.randint(0,9))
        if len(num1)==5:
            break
        i=i+1
    list1=list(num1)
    print(list1)
    chance=10
    cow=[]
    bull=[]    
    while chance>0:
        num=int(input("enter the gasnum="))
        position=int(input("enter the position="))
        if num  in list1:
            index=list1.index(num)
            if index==position:
                bull.insert(index,num)
                print("--------------------------------")
                print("Bull",bull)
                print("your choice list is correct")
            else:
                cow.append(num)
                print("Its a cow u can use this num",cow)
                print("your are wrong please currect your number and position-----")
                chance-=1
        if bull==list1:
            print("Congractulation You Win ")
            break
        else:
            pass
            # print("its not in list")
        chance-=1
        print(chance)
cow_buls()





# list=[3,4,56,78]
# user=int(input("enter any number="))
# i=0
# while i<len(list):
#     if list[i]==user:
#         print(i)
#     i=i+1


# alphabets = ['a', 'e', 'i', 'o', 'g', 'l', 'i', 'u']

# # index of 'i' in alphabets
# index = alphabets.index('e')   # 1
# print('The index of e:', index)
