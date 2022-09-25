try:
    # This model supports running locally, or on Google Colab. If running on Google Colab, it will automatically detect the environment, install any missing dependencies, and activate the GPU or TPU if available.
    from google.colab import drive
    COLAB = True
except:
    COLAB = False