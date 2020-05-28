# total_comprehension.py

my_numbers = [1, 2, 3, 4, 5, 6, 7]
print("--------------")
print("ORIGINAL LIST:", my_numbers)

print("--------------")
print("TOTAL COMPREHENSION...")

# TODO: write python code here

for i in my_numbers:
    print(i)

    
print("--------------")
mapped_numbers = [n * 100 for n in my_numbers]
print("MAPPED LIST:", mapped_numbers)

print("--------------")
filtered_numbers = [n for n in my_numbers if n > 3]
print("FILTERED LIST W/ MATCHES:", filtered_numbers)

print("--------------")
no_numbers = [n for n in my_numbers if n > 8]
print("FILTERED LIST W/O MATCHES:", no_numbers)

print("--------------")
map_filter_numbers = [n * 100 for n in filtered_numbers]
print("MAPPED AND FILTERED LIST:", map_filter_numbers)    
#[400, 500, 600, 700]