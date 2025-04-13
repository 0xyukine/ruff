from pathlib import Path
import hashlib

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
            yield (dir1[x].name, "")
            x += 1
        elif dir1[x].name > dir2[y].name:
            yield ("", dir2[y].name)
            y += 1
        elif dir1[x].name == dir2[y].name:
            yield (dir1[x].name, dir2[y].name)
            x += 1
            y += 1


        if x == dir1_max - 1:
            while y <= dir2_max - 1:
                yield ("", dir2[y].name)
                y += 1
            break
        if y == dir2_max - 1:
            while x <= dir1_max - 1:
                yield (dir1[x].name, "")
                x += 1
            break

        count += 1

    # print(x,y)

def md5hash(file_bytes):
    h = hashlib.new('md5')
    h.update(file_bytes)
    return h.hexdigest()

def perceptualhash():
    pass

def open_file(file_path):
    with open(file_path, 'rb') as f:
        file_bytes = f.read()
    return file_bytes

# dir1 = list_dir('/mnt/e/Stuff/Rips/twitter_old')
# dir2 = list_dir('/mnt/e/Stuff/Rips/twitter')

# compare_generator = compare_dirs(dir1, dir2)
# for item_tuple in compare_generator:
#     print(item_tuple)

print(md5hash(open_file('')))