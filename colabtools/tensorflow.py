import tensorflow as tf

def get_gpu_names():
    return [gpu.name.strip('/physical_device:') for gpu in tf.config.list_physical_devices('GPU')]

def get_strategy():
    try:
        tpu = tf.distribute.cluster_resolver.TPUClusterResolver()  # TPU detection
        print('Running on TPU ', tpu.cluster_spec().as_dict()['worker'])
        tf.config.experimental_connect_to_cluster(tpu)
        tf.tpu.experimental.initialize_tpu_system(tpu)
        print('Using TPU')
        return tf.distribute.experimental.TPUStrategy(tpu)
    except ValueError:
        print('No TPU found')
    gpus = tf.config.list_physical_devices('GPU')
    if gpus:
        print(f'Using GPU(s): {gpus}')
        return tf.distribute.MirroredStrategy(devices=get_gpu_names())
    print('Using CPU')
    return tf.distribute.MirroredStrategy()

def set_default_strategy():
    tf.distribute.experimental_set_strategy(get_strategy())