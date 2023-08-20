'''
python3 tensorflow/train.py
'''
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

# Init
DIM = 224
epochs = 10
batch_size = 16
AUTOTUNE = tf.data.AUTOTUNE
train_dir = 'dataset/train'
val_dir = 'dataset/val'
test_dir = 'dataset/test'

train_ds = tf.keras.utils.image_dataset_from_directory(
  train_dir,
  seed=123,
  image_size=(DIM, DIM),
  batch_size=batch_size
  )

val_ds = tf.keras.utils.image_dataset_from_directory(
  val_dir,
  seed=123,
  image_size=(DIM, DIM),
  batch_size=batch_size
  )

class_names = train_ds.class_names
num_classes = len(class_names)
print('class_names: ',class_names, ' num of classes: ',num_classes)

for image_batch, labels_batch in train_ds:
  print(f'image batch: {image_batch.shape} label batch: {labels_batch.shape}')
  break

train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)

if __name__ == "__main__":

    print('Start training!')

    model = Sequential([
            layers.Rescaling(1./255, input_shape=(DIM, DIM, 3)),
            layers.Conv2D(16, 3, padding='same', activation='relu'),
            layers.MaxPooling2D(),
            layers.Conv2D(32, 3, padding='same', activation='relu'),
            layers.MaxPooling2D(),
            layers.Conv2D(64, 3, padding='same', activation='relu'),
            layers.MaxPooling2D(),
            layers.Flatten(),
            layers.Dense(128, activation='relu'),
            layers.Dense(num_classes)
            ])

    model.summary()

    model.compile(optimizer='adam',
                loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                metrics=['accuracy'])

    history = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=epochs
    )

