'''Write a closure-based function make_average_tracker() that returns a function which accepts a new number each time 
it's called and returns the running average of all numbers seen so far.
This requires the closure to track both the running sum and the count of values, using nonlocal for both.'''

def make_average_tracker():
    total = 0
    count = 0

    def average(num):
        nonlocal total,count

        total+=num
        count+=1
        return total / count
    return average

tracker = make_average_tracker()

print(tracker(10)) 
print(tracker(20))