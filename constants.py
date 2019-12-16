import tensorflow as tf

value1 = tf.constant(1)
value2 = tf.constant(2)

sum = value1 + value2
#print(sum)
with tf.Session() as session:
    s = session.run(sum)
#print(s)

text1 = tf.constant("text 1")
text2 = tf.constant("text 2")
#print(text1)

with tf.Session() as session:
    concat = session.run(text1 + text2)
print (concat)