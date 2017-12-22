'''
Created on Aug 20, 2017

@author: J Chavan
'''
print("*****Welcome to text finder*****\nEnter PARAGRAPH:\n")
para=input()
list1=[]
list2=[]
while(1):
    choice=int(input("1.Search 2.Replace 3.Recent Search 4.Recent Replace 5.Clear Lists:\n"))
    if(choice==1):
        search=input("Enter search item:\n")
        list1.insert(0,search)
        print("'"+search+"'"+" found at:", para.index(search))
    elif(choice==2):
        old=input("what do u want to replace?:")
        list2.insert(0,old)
        new=input("enter new text:")
        para=para.replace(old,new)
        print(para)
    elif(choice==3):
        if len(list1)==0:
            print("list is empty")
        else:
            print("recently searched:",list1)
    elif(choice==4):
        if len(list2)==0:
            print("list is empty")
        else:
            print("recently replaced:",list2)
    elif(choice==5):
        list1.clear()
        list2.clear()
        
    else:
        print("Invalid choice")
        