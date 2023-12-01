with open('input.txt', 'r') as file:
    total_sum = 0
    for i, line in enumerate(file):
        print(line)
        digits = [num for num in line if num.isdigit()]
        print(digits)

        if len(digits) == 1:
            total_sum += int(str(digits[0]) + str(digits[0]))

        else:
            total_sum += int(str(digits[0]) + str(digits[-1]))
print(total_sum)

