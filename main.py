from pathlib import Path

dir1 = sorted([x for x in Path('/mnt/e/Stuff/Rips/twitter_old').iterdir()])
dir2 = sorted([x for x in Path('/mnt/e/Stuff/Rips/twitter').iterdir()])

#x = [x.name.split('-')[1].strip() for x in p.iterdir()]
#print(sorted(x))
#for x in p.iterdir():
#    x.rename(Path(dir1) / x.name.split('-')[1].strip())

count = 0
x,y = 0,0
dir1_max = len(dir1)
dir2_max = len(dir2)

while True:
    if dir1[x].name < dir2[y].name:
        print(count, dir1[x].name + "\t")
        x += 1
    elif dir1[x].name > dir2[y].name:
        print(count, "\t"*2 + dir2[y].name)
        y += 1
    elif dir1[x].name == dir2[y].name:
        print(count, dir1[x].name, dir2[y].name)
        x += 1
        y += 1


    if x == dir1_max - 1:
        while y <= dir2_max - 1:
            print(count, "\t"*2 + dir2[y].name)
            y += 1
        break
    if y == dir2_max - 1:
        while x <= dir1_max - 1:
            print(count, dir1[x].name)
            x += 1
        break

    count += 1

print(x,y)