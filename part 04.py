# I declare that my work contains no examples of misconduct, such as plagiarism, orcollusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20220995

# Date: 08/12/2022

keep_going = "y"
count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0
progress_count = 0
trailer_count = 0
retriever_count = 0
exclude_count = 0
list_1=[] 
list_2=[]
dict_1={}

while True:
    
    user_id=input('Enter user ID:')
    if len(user_id)!=8 or not user_id.startswith('w'):
        print('Invalid User ID, PLease try again!')
        continue
    elif user_id.startswith('w') and len(user_id)==8:
        
        while keep_going == "y":
            try:
                pass_credit = int(input("Enter your total PASS credits: "))
                if pass_credit not in range(0, 121, 20):
                    print("Out of range")
                    continue
                defer_credit = int(input("Enter your total DEFER credits: "))
                if defer_credit not in range(0, 121, 20):
                    print("Out of range")
                    continue
                fail_credit = int(input("Enter your total FAIL credits: "))
                if fail_credit not in range(0, 121, 20):
                    print("Out of range")
                    continue
                x=pass_credit,defer_credit,fail_credit
                list_1.append(x)
            except ValueError:
                print("Integer required")
                continue
            total_credits = pass_credit + defer_credit + fail_credit
            if total_credits != 120:
                print("Total Incorrect")
                continue
            elif pass_credit == 120:
                count_1 += 1
                progress_count = count_1 * "*"
                print("Progress")
                list_1.insert(0,'Progress -')
                list_2.append(list_1)
            elif pass_credit == 100:
                count_2 += 1
                trailer_count = count_2 * "*"
                print("Progress (module trailer)")
                list_1.insert(0,'Progress (module trailer) -')
                list_2.append(list_1)
            elif pass_credit <= 80 and fail_credit < 80:
                count_3 += 1
                retriever_count = count_3 * "*"
                print("Do not progress- module retriever")
                list_1.insert(0,'module retriever -')
                list_2.append(list_1)
            elif fail_credit >= 80:
                count_4 += 1
                exclude_count = count_4 * "*"
                print("Exclude")
                list_1.insert(0,'Exclude -')
                list_2.append(list_1)
            dict_1[user_id]=(list_1)
            list_1=[]
            break
        keep_going = input("""
Would you like to enter another set of data?
Press 'y' for yes and 'q' to quit:
""")
    keep_going = keep_going.lower()
    if keep_going == "q":
        print("Histogram")
        print("-" * 50)
        print(f"Progress {count_1}\t{progress_count}")
        print(f"Trailer {count_2}\t{trailer_count}")
        print(f"Retriever {count_3}\t{retriever_count}")
        print(f"Exclude {count_4}\t{exclude_count}")
        print(f'There are {count_1 + count_2 + count_3 + count_4} outcomes in total')
        print("-" * 50)


        with open('Text_file.txt','w') as file:
            file.write('Part 3:\n')
        
        for count in range(len(list_2)):
            print(list_2[count][0],list_2[count][1][0],(','),list_2[count][1][1],(','),list_2[count][1][2])
            with open('Text_file.txt','a') as file:
                file.write(str(list_2[count][0]))
                file.write(str(list_2[count][1][0]))
                file.write(',')
                file.write(str(list_2[count][1][1]))
                file.write(',')
                file.write(str(list_2[count][1][2]))
                file.write('\n')

        print('Part 4:')
        print(*[str(k)+':'+str(v) for k,v in dict_1.items()])

        break


            
        
        
                
        
