from . import drive, tensorflow

try:
    # This model supports running locally, or on Google Colab. If running on Google Colab, it will automatically detect the environment, install any missing dependencies, and activate the GPU or TPU if available.
    import google.colab
    COLAB = True
    tensorflow.set_default_strategy()
    drive.mount()
except:
    COLAB = False