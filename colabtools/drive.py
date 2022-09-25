def mount():
    """Mounts Google Drive to the Colab VM."""
    try:
        from google.colab import drive
        drive.mount('/content/drive')
        print('Mounted at /content/drive')
    except:
        print('Not running on Google Colab')