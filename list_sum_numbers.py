li = []
n = int(input("Enter the number of elements you want in the list."))
for i in range(n):
    a = int(input())
    li.append(a)

n_sum = 0
p_even_sum = 0
p_odd_sum = 0
for ele in li:
    if ele < 0:
        n_sum += ele
    else:
        if ele % 2 == 0:
            p_even_sum += ele
        else:
            p_odd_sum += ele


print("Sum of negative numbers:", n_sum)
print("Sum of positive even numbers:", p_even_sum)
print("Sum of positive odd numbers:", p_odd_sum)
