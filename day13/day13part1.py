data = open('input.txt').read().strip().split('\n\n')

for i, item in enumerate(data):
    data[i] = item.split('\n')    

def iterate_out_rows(i, item):
    k = 0
    valid = True
    while (i+k+1) < len(item) and (i-k-2)>=0 :
        k += 1
        if item[i+k] != item[i-k-1]:
            valid = False

    return valid, k


count = 0
prev = ''
done = False
for j, item in enumerate(data):
    done = False
    print("ON ITEM ", j)
    for i, row in enumerate(item):
        if row == prev:
            print("row", i)
            vert, l = iterate_out_rows(i, item)
            if vert:
                print("vert", i, l)
                count += 100*i
                done = True
                break
        prev = row
    
    if not done:
        item_t = [list(i) for i in zip(*item[::-1])]
        print('\n'.join(item))
        print()
        print(item_t)
        for i, col in enumerate(item_t):
            if col == prev:
                hor, l = iterate_out_rows(i, item_t)
                if hor:
                    print("cols", i)
                    count += 1*i
                    done = True
                    break


            prev = col
       

print(count)