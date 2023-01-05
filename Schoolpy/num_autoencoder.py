import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist
from keras import backend as K
import numpy as np

def mydata(img_rows, img_cols):

    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    if K.image_data_format() == 'channels_first':

        x_train = x_train.reshape(x_train.shape[0], 1, img_rows, img_cols)

        x_test = x_test.reshape(x_test.shape[0], 1, img_rows, img_cols)

        input_shape = (1, img_rows, img_cols)

    else:

        x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)

        x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)

        input_shape = (img_rows, img_cols, 1)

    x_train = x_train.astype('float32')

    x_test = x_test.astype('float32')

    x_train /= 255 #归一化

    x_test /= 255

    return  x_train, x_test, input_shape

def mymodel(inputs):
    #encoder
    layer1 = tf.layers.conv2d(inputs,3,kernel_size = (5,5), activation = tf.nn.relu)
    # layer2 = tf.layers.dropout(inputs, rate=0.5, training=False)
    layer2 = tf.layers.flatten(layer1)
    layer3 = tf.layers.dense(layer2,10*10,activation = None)
    layer4 = tf.layers.dense(layer3,28*28, activation=tf.nn.relu, use_bias=True)
    layer4 = tf.reshape(layer4,shape=[-1,28,28,1])
    return layer4

def myloss(inputs,labels):

    y = inputs

    loss = tf.reduce_mean(tf.square(y-labels))

    return loss

def mytrain(loss,learningrate):

    optimizer = tf.train.GradientDescentOptimizer(learningrate)

    train = optimizer.minimize(loss)

    return train

batch_size = 128

num_classes = 10

epochs = 30

learningrate = 0.5

img_rows, img_cols = 28,28

x_train,x_test,input_shape = mydata(img_rows,img_cols)
indexBatch = np.random.randint(0,x_train.shape[0],size=batch_size)

x_input = x_train[indexBatch]

x_input = tf.reshape(x_input,x_input.shape)

y_hat = mymodel(x_input)

loss = myloss(y_hat,x_input)

train = mytrain(loss, learningrate)

init = tf.initialize_all_variables()


sess = tf.Session()

sess.run(init)

for step in range(5000):
    sess.run(train)
    if step % 50 == 0:
        print("第",step,"次的loss为:",sess.run(loss))
plt.figure(1,figsize=(16,8))
for i in range(0,batch_size):
    imm = sess.run(y_hat[i])
    im = imm.reshape(28,28)
    ax = plt.subplot(16,8,i+1)
    for la in (ax.get_xticklabels()+ax.get_yticklabels()):
        la.set_fontname('Arial')
        la.set_fontsize(8)
    plt.imshow(im,cmap="gray",clim=(0.0,1.0))
plt.show()