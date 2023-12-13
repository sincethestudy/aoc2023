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


#first pass

track = []


count = 0
prev = ''
done = False
for j, item in enumerate(data):
    done = False
    for i, row in enumerate(item):
        if row == prev:
            vert, l = iterate_out_rows(i, item)
            if vert:
                count += 100*i
                track.append((j, i, 'r'))
                done = True
                break
        prev = row
    
    if not done:
        item_t = [list(i) for i in zip(*item[::-1])]
        for i, col in enumerate(item_t):
            if col == prev:
                hor, l = iterate_out_rows(i, item_t)
                if hor:
                    count += 1*i
                    track.append((j, i, 'c'))
                    done = True
                    break

            prev = col
       

print(track)



count = 0
for j, item in enumerate(data):
    done = False
    for g in range(len(item)):
        print('item ', g)
        for h in range(len(item[g])):
            print(item)
            prev = ''

            if item[g][h] == '#':
                item[g] = item[g][:h] + '.' + item[g][h+1:]
            elif item[g][h] == '.':
                item[g] = item[g][:h] + '#' + item[g][h+1:]

            print(item)

            for i, row in enumerate(item):
                if row == prev and (j, i, 'r') not in track:
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
                for i, col in enumerate(item_t):
                    if col == prev and (j, i, 'c') not in track:
                        hor, l = iterate_out_rows(i, item_t)
                        if hor:
                            print("cols", i)
                            count += 1*i
                            done = True
                            break


                    prev = col

            if item[g][h] == '#':
                item[g] = item[g][:h] + '.' + item[g][h+1:]
            elif item[g][h] == '.':
                item[g] = item[g][:h] + '#' + item[g][h+1:]

            if done:
                break

        if done:
            break
       

print(count)