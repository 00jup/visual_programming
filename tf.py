import tensorflow as tf

# Path: tf.keras.py

키 = 170
신발 = 260

a = tf.Variable(0.1)
b = tf.Variable(0.2)

# 신발 = 키 * a + b
def loss():
    return tf.square(신발 - (키 * a + b))


opt = tf.keras.optimizers.legacy.Adam(learning_rate=0.1)

for i in range(300):
    opt.minimize(loss, var_list=[a, b])
    print(a.numpy(), b.numpy())
