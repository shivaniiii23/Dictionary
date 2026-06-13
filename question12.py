"""
12.

=========================================
ONLINE FOOD DELIVERY ANALYSIS
=============================

orders = [
"Pizza",
"Burger",
"Pizza",
"Pasta",
"Burger",
"Pizza",
"Pasta"
]

Write a program to:

* Count orders of each food item.
* Find the most ordered item.

Sample Output:
Pizza : 3
Burger : 2
Pasta : 2

Most Ordered : Pizza
"""
orders = [
"Pizza",
"Burger",
"Pizza",
"Pasta",
"Burger",
"Pizza",
"Pasta"
]
d = {}
for i in orders:
    d[i]=d.get(i,0)+1
print(d)
for k,v in d.items():
    print(k,":",v)
m_o = 0
for k,v in d.items():
    if v > m_o:
        m_o = v
        print("Most Ordered:",k)        
    
