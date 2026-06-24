'''The Top 'K' Sales Items (Intermediate) An e-commerce store wants to know its top-selling products for the day. You are given a list of product IDs representing individual sales.
Task: Write a function top_k_products(sales, k) that takes a list of integers (product IDs) and an integer k. Use a Counter to find and return a list of the k most frequently sold product IDs in descending order of frequency.

Sample Input: sales = [101, 102, 101, 103, 101, 102, 104, 105, 102, 101], k = 2

Expected Output: [101, 102] (Explanation: 101 appears four times, and 102 appears three times)'''


from collections import Counter
sales = [101, 102, 101, 103, 101, 102, 104, 105, 102, 101]
a = Counter(sales)
print(a)

print(a.most_common(2))
