from pathlib import Path

def list_dir(dir_path='.', sort=True):
    directory = [x for x in Path(dir_path).iterdir()]
    if sort == True:
        return sorted(directory)
    else:
        return directory

def compare_dirs(dir1='.', dir2='.'):
    count = 0
    x,y = 0,0
    dir1_max = len(dir1)
    dir2_max = len(dir2)

    while True:
        if dir1[x].name < dir2[y].name:
            # print(count, dir1[x].name + "\t")
            yield (dir1[x].name, "")
            x += 1
        elif dir1[x].name > dir2[y].name:
            # print(count, "\t"*2 + dir2[y].name)
            yield ("", dir2[y].name)
            y += 1
        elif dir1[x].name == dir2[y].name:
            # print(count, dir1[x].name, dir2[y].name)
            yield (dir1[x].name, dir2[y].name)
            x += 1
            y += 1


        if x == dir1_max - 1:
            while y <= dir2_max - 1:
                # print(count, "\t"*2 + dir2[y].name)
                yield ("", dir2[y].name)
                y += 1
            break
        if y == dir2_max - 1:
            while x <= dir1_max - 1:
                # print(count, dir1[x].name)
                yield (dir1[x].name, "")
                x += 1
            break

        count += 1

    # print(x,y)

dir1 = list_dir('/mnt/e/Stuff/Rips/twitter_old')
dir2 = list_dir('/mnt/e/Stuff/Rips/twitter')

compare_generator = compare_dirs(dir1, dir2)
# for x in compare_generator:
#     print(x)

while True:
    print(next(compare_generator))