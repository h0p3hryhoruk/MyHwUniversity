a = int(input())
b = int(input())
c = int(input())

max_number = (a + b + abs(a - b)) // 2
max_number = (max_number + c + abs(max_number - c)) // 2

min_number = (a + b - abs(a - b)) // 2
min_number = (min_number + c - abs(min_number - c)) // 2

mid_number = a + b + c - max_number - min_number

print(max_number)
print(min_number)
print(mid_number)
