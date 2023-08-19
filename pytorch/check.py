'''
python3 pytorch/check.py
'''

import torch

print('Pytorch verions: ',torch.__version__)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

device_count = torch.cuda.device_count()
print(f"Total device: {device_count}")

current_device = torch.cuda.current_device()
print(f"Current device: {current_device}")

for i in range(device_count):
    device_name = torch.cuda.get_device_name(i)
    print(i,device_name)