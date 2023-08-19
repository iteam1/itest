'''
python3 utils/cite.py flower_photos
'''
import os
import sys
import shutil

# init
src = sys.argv[1]
dst = 'dataset'
train_path = os.path.join(dst,'train')
val_path = os.path.join(dst,'val')
test_path = os.path.join(dst,'test')
sizes = [0.2,0.05,0.05] # train, val, test

# check source dataset
if not os.path.exists(src):
    print(src,' not exist')
    exit(-1)

# make dataset
if not os.path.exists(dst):
    os.mkdir(dst)

if not os.path.exists(train_path):
    os.mkdir(train_path)

if not os.path.exists(val_path):
    os.mkdir(val_path)

if not os.path.exists(test_path):
    os.mkdir(test_path)

if __name__ == "__main__":

    print(f'Start citing from {src}')

    # list all class from source
    classes = os.listdir(src)

    print('Total ', len(classes), ' classes')

    for cls in classes:
        files = os.listdir(os.path.join(src,cls))
        print(files)
        print('Current class: ',cls)

    exit(0)