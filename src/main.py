import tensorflow as tf

print("Hello, World")

print(f"Tensorflow Version: {tf.__version__}")
print(f"GPUs Available: {tf.config.list_physical_devices('GPU')}")
