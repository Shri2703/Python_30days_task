'''Problem Statement:
student Name and the five subject mark and make the name total mark and the percentaage of the total maek 
'''

#soluton

name = input("Enter your name:")
marks = [int(input("Enter your marks for subject" + str(i)+":")) for i in range(1,6)]

total_mark = sum(marks)
if (total_mark >= 500):
    print("enter the proper mark of each subject")
else:    
    percentage =(total_mark/500)*100
    print(" Student Name:",name," and the Total matk :", total_mark, " and the percentage percentage is :", percentage)