def LuuFile(path, data):
    file = open(path, 'a', encoding='utf-8')
    file.writelines(data)
    file.writelines('\n')
    file.close()

def Read(path):
    arrDS = []
    file = open(path, 'r', encoding='utf-8')
    for line in file:
        data = line.strip()
        arr = data.split(',')
        arrDS.append(arr)

    file.close()
    return arrDS