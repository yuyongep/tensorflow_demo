import tensorflow as tf
a = tf.constant([1.0,2.0],name='a')
b = tf.constant([1.0,2.0],name='b')
c = tf.constant([3,5], name = 'tensor_c')
c2 = tf.constant([3,5.9], name = 'tensor_c')
result = tf.add(a,b,name='add')
print('Tensor result:', result)
print('result.get_shape:',result.get_shape)
print('result.get_shape():',result.get_shape())
print('result.shape:',result.shape)
print('result.dtype:',result.dtype)
print('result[0].dtype:',result[0].dtype)
print('c[0].dtype:',c[0].dtype)
print('c[1].dtype:',c[1].dtype)
print('c2[0].dtype:',c2[0].dtype)
print('c2[1].dtype:',c2[1].dtype)
