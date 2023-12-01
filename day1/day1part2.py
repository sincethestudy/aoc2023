## the strat for this one thats more interesting to do is to reverse the string and reverse the words we are checking, and then run the same algorithm for both first and last

with open('input.txt', 'r') as file:
    total_sum = 0
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i, line in enumerate(file):
        print(line)
        found = False
        first = ''
        last = ''
        for j in range(len(line)):
            if found:
                break
            for word in words:
                if line.startswith(word, j):
                    first = words.index(word) + 1
                    found = True
                    break
            if not found and line[j].isdigit():
                first = line[j]
                break

        found = False
        for j in range(len(line) - 1, -1, -1):
            if found:
                break
            for word in words:
                if line.startswith(word, j):
                    last = words.index(word) + 1
                    found = True
                    break
            if not found and line[j].isdigit():
                last = line[j]
                break

        print(int(str(first) + str(last)))

        total_sum += int(str(first) + str(last))
            


print(total_sum)

