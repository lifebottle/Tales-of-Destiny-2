import sys
import os
import shutil

def move_to_sced_folder():
    try:
        os.mkdir('_SCED')
    except:
        pass
    
    for folder in os.listdir(os.getcwd()):
        if not os.path.isdir(folder):
            continue
        if folder == '_SCED':
            continue
        for n in os.listdir(folder):
            if n.endswith('sced'):
                f = n
                break
        new_name = '%s_%s.sced' % (folder, f.split('.')[0])
        shutil.copy(os.path.join(folder,f), '_sced/' + f)
        print (new_name)

def move_to_pak_folder():
    for name in os.listdir('_SCED'):
        folder = name.split('_')[0]
        n = name.split('_')[1]
        shutil.copy(os.path.join('_sced/', name), os.path.join(folder, n))
        print (name)

if __name__ == '__main__':
    if sys.argv[1] == '1':
        move_to_sced_folder()
    elif sys.argv[1] == '2':
        move_to_pak_folder()
    else:
        sys.exit(1)
