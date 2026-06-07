'''                    List Packing and Unpacking Challenge :
Write a Python program to handle a list of employee details where each employee is stored as a list like [id, name, age, salary].
The program should :

1. Unpack each employee record into separate variables
2. Store employees with salary above a given limit in a new list
3. Sort the filtered list by salary
4. Extract only the employee names using list comprehension
5. Search for a particular employee ID in the list.    '''


employees = [
    [101, "Amit", 25, 35000],
    [102, "Priya", 30, 52000],
    [103, "Rohan", 28, 47000],
    [104, "Neha", 32, 60000],
    [105, "Karan", 26, 42000]]
salary_limit = int(input("enter the minimum salary :"))
search_id = int(input("enter the id to be searched :"))

for i in employees:
    e_id, name, age, salary = i
    print("e_id:", e_id, "name:", name, "age:", age, "salary:", salary)

lst=[]
for i in employees:
    if i[3] > salary_limit:
        lst.append(i)
lst.sort()
print("employees with salary above",salary_limit)

for i in lst:
    print(i)
names = [i[1]]
print("employee names:")
print(names)

for i in employees:
    if i[0] == search_id:
        found = True
        break
if found:
    print(search_id, "Found !")
else:
    print(search_id, "Not Found !")