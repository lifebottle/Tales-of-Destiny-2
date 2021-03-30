import os, sys, json, shutil, subprocess, struct

ext = ['at3', 'elf', 'iecs', 'pak0', 'pak1', 'pak3', 'pak4',
       'mcd', 'mc1', 'scpk', 'sfm', 'f00', 'smo',
       'tim2', 'unsorted', 'vcd', 'x4f0', 'at3pak']
paks = ['pak0', 'pak1', 'pak4']


def is_compressed(name):
    f = open(name, 'rb')
    data = f.read()
    if struct.unpack('<L', data[1:5])[0] == len(data) - 9:
        f.close()
        return [True, data[0]]
    f.close()
    return [False]

def rename():
    json_file = open('FPB.json', 'r')
    data = json.load(json_file)
    json_file.close()
    c_json = open('compression.json', 'w')
    c_data = {}
    try: os.mkdir('FILE')
    except: pass
    for name in os.listdir('FPB'):
        fname = name.split('.')[0]
        if fname in data.keys():
            print (name)
            try: os.mkdir('file/' + data[fname])
            except: pass
            new_location = 'file/' + data[fname] + '/' + fname + '.' + data[fname]
            shutil.copy(os.path.join('fpb/',name), new_location)
            if data[fname] in paks:
                c_result = is_compressed(new_location)
                if not c_result[0]:
                    c_data[fname] = 0
                    continue
                c_data[fname] = c_result[1]
                dec = new_location + '.d'
                subprocess.run(['comptoe', '-d', new_location, dec])
                os.remove(new_location)
                os.rename(dec, new_location)
    json.dump(c_data, c_json, indent=4)
                
if __name__ == '__main__':
    rename()
