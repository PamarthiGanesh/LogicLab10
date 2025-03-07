def ask(a,b,c):
    combine_list = []
    print(f'set 1 :{a}\nset 2 :{b}\nset 3 :{c}')
    user=int(input('Enter the number of the set in which you choice the number : '))
    if user==1:
        combine_list=b+a+c
    elif user==2:
        combine_list=c+b+a
    elif user==3:
        combine_list=a+c+b
    else:
        print('Enter the correct choice : ')
        ask(a,b,c)
    return combine_list
#<<<<<<<<<<<<<<<<<<<<->>>>>>>>>>>>>>>>>>>#
def hi(list1):
    sub_set1=[]
    sub_set2=[]
    sub_set3=[]
    j=0
    while j<24:
        sub_set1.append(list1[j])
        j+=1
        sub_set2.append(list1[j])
        j+=1
        sub_set3.append(list1[j])
        j+=1
    return sub_set1,sub_set2,sub_set3
#<<<<<<<<<<<<<<<<<<<<->>>>>>>>>>>>>>>>>>>#
print('\tGIVE 2 CHANCE TO FIND THE NUMBER')
main_list=[]
for i in range(1,25):
    main_list.append(i)
#>>>>>>>>>>>
for i in range(3):
    set1,set2,set3=hi(main_list)
    main_list=ask(set1,set2,set3)
back_up=input(f'the no may be {main_list[11]} (yes/no):')
if back_up=='no' or back_up=='No':
    print(f'then it must be {main_list[12]}')