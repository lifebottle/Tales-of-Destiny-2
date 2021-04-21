import os, sys, json, shutil, subprocess, struct

# folders that will be decompressed
compressed = ['bin', 'mcd', 'pak0', 'pak1', 'pak4', 'tm2']

def is_compressed(name):
    f = open(name, 'rb')
    data = f.read()
    if struct.unpack('<L', data[1:5])[0] == len(data) - 9:
        f.close()
        return [True, data[0]]
    f.close()
    return [False, 0]

def unpack():
    json_file = open('FPB.json', 'r')
    data = json.load(json_file)
    json_file.close()
    c_json = open('compression.json', 'w')
    c_data = {}
    
    try: os.mkdir('FILE')
    except: pass

    for d in data.values():
        if d == 'dummy':
            continue
        try: os.mkdir('FILE/' + d)
        except: pass
    
    for name in os.listdir('FPB'):
        fname = name.split('.')[0]
        if fname in data.keys():
            print (name)
            new_location = f'FILE/{data[fname]}/{fname}.{data[fname]}'
            #new_location = 'file/' + data[fname] + '/' + fname + '.' + data[fname]
            shutil.copy(os.path.join('FPB/', name), new_location)
            c_result = is_compressed(new_location)
            c_data[fname] = c_result[1]
            if data[fname] in compressed:
                if not c_result[0]:
                    continue
                dec = new_location + '.d'
                subprocess.run(['comptoe.exe', '-d', new_location, dec])
                os.remove(new_location)
                os.rename(dec, new_location)
    json.dump(c_data, c_json, indent=4)
                
if __name__ == '__main__':
    unpack()
