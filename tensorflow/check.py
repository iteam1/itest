'''
python3 tensorflow/check.py
'''

import tensorflow as tf
from tensorflow.python.client import device_lib

print('Tensorflow Version: ',tf.__version__)

# device_lib.list_local_devices()

print('GPU Available: ',tf.test.is_gpu_available())

gpus = tf.config.list_physical_devices('GPU')
print('Total GPU available: ',len(gpus))

if gpus:
  # Only allocate GPU memory as needed
  for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)
    print(f"Available GPU: {gpu}")
else:
  print("No available GPUs")