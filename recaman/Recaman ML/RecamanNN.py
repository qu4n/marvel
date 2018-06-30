from __future__ import absolute_import, division, print_function

import os
import matplotlib.pyplot as plt

import tensorflow as tf
import tensorflow.contrib.eager as tfe

tf.enable_eager_execution()

print("TensorFlow version: {}".format(tf.VERSION))
print("Eager execution: {}".format(tf.executing_eagerly()))


def parse_csv(line):
  example_defaults = [[0], [0]]  # sets field types
  parsed_line = tf.decode_csv(line, example_defaults)
  # First field is the feature, combine into single tensor
  feature = tf.reshape(parsed_line[:-1], shape=(1,))
  # Last field is the label
  label = tf.reshape(parsed_line[-1], shape=())
  return feature, label

def loss(model, x, y):
  y_ = model(x)
  return tf.losses.sparse_softmax_cross_entropy(labels=y, logits=y_)

def grad(model, inputs, targets):
  with tf.GradientTape() as tape:
    loss_value = loss(model, inputs, targets)
  return tape.gradient(loss_value, model.variables)

#Specify path to where training data file resides
train_dataset_rs = ".\\Datasets\\RecamanTrainingData_30000.csv"

train_dataset = tf.data.TextLineDataset(train_dataset_rs)
train_dataset = train_dataset.map(parse_csv)      # parse each row
train_dataset = train_dataset.shuffle(buffer_size=1000)  # randomize
train_dataset = train_dataset.batch(32)

# View a single example entry from a batch
feature, label = iter(train_dataset).next()
print("\nexample features:", feature[0])
print("\nexample label:", label[0])

model = tf.keras.Sequential([
  tf.keras.layers.Dense(10, activation="relu", input_shape=(1,)),  # input shape required
  tf.keras.layers.Dense(10, activation="relu"),
  tf.keras.layers.Dense(3)
])

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)

## Note: Rerunning this cell uses the same model variables

''' Under Contruction
# keep results for plotting
train_loss_results = []
train_accuracy_results = []

num_epochs = 201

for epoch in range(num_epochs):
  epoch_loss_avg = tf.metrics.
  epoch_accuracy = tf.metrics.accuracy()

  # Training loop - using batches of 32
  for x, y in train_dataset:
    # Optimize the model
    grads = grad(model, x, y)
    optimizer.apply_gradients(zip(grads, model.variables),
                              global_step=tf.train.get_or_create_global_step())

    # Track progress
    epoch_loss_avg(loss(model, x, y))  # add current batch loss
    # compare predicted label to actual label
    epoch_accuracy(tf.argmax(model(x), axis=1, output_type=tf.int32), y)

  # end epoch
  train_loss_results.append(epoch_loss_avg.result())
  train_accuracy_results.append(epoch_accuracy.result())
  
  if epoch % 50 == 0:
    print("Epoch {:03d}: Loss: {:.3f}, Accuracy: {:.3%}".format(epoch,
                                                                epoch_loss_avg.result(),
                                                                epoch_accuracy.result()))
'''