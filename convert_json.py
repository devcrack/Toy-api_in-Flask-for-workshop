import json, io
import glob, os


path = '/home/delcracnk/REPOSITORIES/Bank_Models/01Sk_HSphere/Benny_Version/data/sk_HSpheere.dat'
try:
    to_unicode = unicode
except NameError:
    to_unicode = str

def convert_file():
    data = {}
    line_counter = 0
    raw_file = open(path, 'r')
    for line in raw_file.readlines():
        line = line.replace('\t', ',', 1)
        a_data = line.split(',')
        if line_counter == 0:
            key1 = a_data[0]
            key2 = a_data[1].strip()
            data[key1] = []
            data[key2] = []
            # print(data)
        else:
            # print(a_data[0])
            # print(a_data[1].strip())
            data[key1].append(a_data[0])
            data[key2].append(a_data[1].strip())
        line_counter = line_counter + 1
    print(data)
    split_path  = path.split('/')
    jason_name = split_path[len(split_path) - 1]
    with io.open(jason_name.replace('.dat','.json'), 'w', encoding='utf8') as outfile:
        str_ = json.dumps(data, indent = 2, sort_keys = True, separators = (',', ': '), ensure_ascii=False)
        outfile.write(to_unicode(str_))

if __name__ == '__main__':
    convert_file()
