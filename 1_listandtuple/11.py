''' Question 1: The Sensor Data Cleaner
Topics Covered: List Comprehensions (Sec 9), Sorting (Sec 12), Slicing (Sec 5). Scenario: An IoT sensor records temperature data, but sometimes it glitches and records a 0.

Task : Write a program that takes a list of raw sensor readings.

Use a list comprehension to create a new list that excludes all 0 readings.
Sort this new list in descending order (highest to lowest).
Use slicing to extract and print only the top 3 highest valid readings. '''


readings = [1, 2, 0, 27, 10, 0, 89, 0, 11]

for i in readings:

    if i!=0:
        print("Valid Readings :",i)

i.sort(reverse=True)

top_3 = i[:3]
print("Top 3 Highest Readings:", top_3)