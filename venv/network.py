import keras
from keras.models import load_model, Sequential
from keras.layers import Dense, Flatten, Conv2D, MaxPool2D
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn import preprocessing
import cv2

np.random.seed(3)

X = []
y = []

with open('actions.csv', 'r') as f:
    for line in f:
        y.append(line.rstrip())


all_images = []
img_num = 0
while img_num < 3711:
    img = cv2.imread(r'./dataset/frame_{0}.jpg'.format(img_num), cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (0, 0), fx=0.3, fy=0.3)
    img = img[:, :, np.newaxis]
    all_images.append(img)
    img_num += 1

X = np.array(all_images)

print(X[0].shape)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)

img_x, img_y = 90, 498
input_shape = (img_x, img_y, 1)

classifications = 2
y_train = keras.utils.to_categorical(y_train, classifications)
y_test = keras.utils.to_categorical(y_test, classifications)

model = Sequential()
model.add(Conv2D(100, kernel_size=(2, 2), strides=(2, 2), activation='relu', input_shape=input_shape))
model.add(MaxPool2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(250, activation='relu'))
model.add(Dense(classifications, activation='softmax'))
model.compile(loss = 'categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

tbCallback = keras.callbacks.TensorBoard(log_dir='./Graph', histogram_freq=0, write_graph=True, write_images=True)

model.fit(X_train, y_train, batch_size=250, epochs=13, validation_data=(X_test, y_test), callbacks=[tbCallback])

model.save('model.h5')