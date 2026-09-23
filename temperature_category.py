#Nicole Ajjan, CMP-131, Week 5, Lab 1, September, 21, 2026
#Part1:temperature_category.py
print("***")
print("Welcome to Our Python Thermometer!")
print("***")

x=float(input("Enter today's current temperature:")) 

if x<=50:
    print("Baby, it's cold outside!")
elif x<=79.9:
    print("Beautiful weather we are having!")
else:
    print("Hot day, stay hydrated!")
