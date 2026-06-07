'''Student Marks Analyzer : Write a Python program that takes a list of student marks and performs the following tasks :
Remove all invalid marks (less than 0 or greater than 100)
Find the highest and lowest marks using indexing / negative indexing
Sort the valid marks in descending order
Print the top 3 marks using slicing
Check whether a given target mark exists in the list'''


ori_marks=[78, 95, 102, 45, -5, 88, 67, 99, 120, 54]
lst=[ori_marks[i] for i in ori_marks if -1<=i<=101 continue else ori_marks.remove(i)]

for i in ori_marks:
    if -1<=i<=101:
        continue
    else:
        ori_marks.remove(i)

ori_marks.sort(reverse=True)

print(ori_marks)

highest_marks = ori_marks[0]
lowest_marks = ori_marks[-1]

print("Top 3 marks:", ori_marks[:3])

user=int(input("enter the marks to be searched :"))

if user not in ori_marks:
    print("INVALID !")
else:
    print("NUMBER FOUND !")

