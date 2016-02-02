
def is_palindrome(number):
    number = str(number)
    if (len(number) % 2 != 0):
        first_half, second_half = number[:int(len(number)/2)], number[int(len(number)/2)+1:]
    else:
        first_half, second_half = number[:int(len(number)/2)], number[int(len(number)/2):]

    return (first_half[::-1] == second_half)

length=3

candidate_1 = pow(10, length)-1
candidate_2 = pow(10, length)-1

current = 0

while (candidate_2 > 0):
    if (is_palindrome(candidate_1 * candidate_2)):
        if ((candidate_1 * candidate_2) > current):
            current = candidate_1 * candidate_2
    candidate_2 = candidate_2 - 1
    if (pow(10, length)*9/10 == candidate_2 and pow(candidate_1 - 1, 2) > current):
        candidate_2 = candidate_1
        candidate_1 = candidate_1 - 1

print(current)

