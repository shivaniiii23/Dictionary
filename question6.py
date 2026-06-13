"""
6.

=========================================
MOBILE APP DOWNLOAD COUNTER
===========================

Downloads received from different cities:

cities = ["Indore","Bhopal","Indore","Pune","Delhi","Pune","Indore"]

Write a program to:

* Count downloads city-wise.
* Display city with maximum downloads.

Sample Output:
{'Indore':3,'Bhopal':1,'Pune':2,'Delhi':1}
Most Downloads : Indore
"""
cities = ["Indore","Bhopal","Indore","Pune","Delhi","Pune","Indore",]
d ={}
for i in cities:
    d[i] = d.get(i,0)+1
print(d)
m_d = 0
for k,v in d.items():
    if v>m_d:
        m_d = v
        print("MOST DOWNLOAD:",k)        

    
    
    
"""
cities = ["Indore","Bhopal","Indore","Pune","Delhi","Pune","Indore",]
d ={}
for i in cities:
    d[i] = d.get(i,0)+1
print(d)
max_key = max(d,key=d.get)
print("most downloads:",max_key)    

    """    
