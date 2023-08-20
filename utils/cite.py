'''
python3 utils/cite.py flower_photos
'''
import os
import sys
import random
import shutil

# init
src = sys.argv[1]
dst = 'dataset'
train_path = os.path.join(dst,'train')
val_path = os.path.join(dst,'val')
test_path = os.path.join(dst,'test')
subsets_path = [train_path,val_path,test_path]
subsets = ['train','val','test']
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

# list all class from source
classes = os.listdir(src)

for subset_path in subsets_path:
    for cls in classes:
        cls_path = os.path.join(subset_path,cls)
        if not os.path.exists(cls_path):
            os.mkdir(cls_path)

if __name__ == "__main__":

    print(f'Start citing from {src},Total {len(classes)} classes')

    for cls in classes:
        
        files = os.listdir(os.path.join(src,cls))
        print('Current class: ',cls)
        total_files = len(files)
        
        # loop over train,val,test
        for i in range(3):
            size = sizes[i]
            subset = subsets[i]
            cite_no = int(total_files*size)
            print(f'citing {cls} {size} to {subset}, Total {cite_no}')
            # random choice
            for j in range(cite_no):
                image_name = random.choice(files)
                src_path = os.path.join(src,cls,image_name)
                dst_path = os.path.join(dst,subset,cls,image_name)
                shutil.copy(src_path,dst_path)

    exit(0)