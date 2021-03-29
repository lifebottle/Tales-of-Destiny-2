import os, sys, json, shutil, subprocess

ext = ['at3', 'elf', 'iecs', 'pak0', 'pak1', 'pak3', 'pak4',
       'mcd', 'mc1', 'scpk', 'sfm', 'f00', 'smo',
       'tim2', 'unsorted', 'vcd', 'x4f0', 'at3pak']
paks = ['pak0', 'pak1', 'pak3']

def rename():
    json_file = open('tree.json', 'r')
    data = json.load(json_file)
    json_file.close()
    try: os.mkdir('FILE')
    except: pass
    for name in os.listdir('FPB'):
        fname = name.split('.')[0]
        if fname in data.keys():
            try: os.mkdir('file/' + data[fname])
            except: pass
            new_location = 'file/' + data[fname] + '/' + fname + '.' + data[fname]
            shutil.copy(os.path.join('fpb/',name), new_location)
            #if data[fname] in paks:
                #dec = 'file/' + data[fname] + '/' + '0' + fname + '.' + data[fname]
                #subprocess.run(['comptoe', '-d', new_location, dec])
                #os.remove('file/' + data[fname] + '/' + fname + '.' + data[fname])
        print (name)

if __name__ == '__main__':
    rename()
