# colabtools

Helper methods to simplify working with Google Colab

## Usage

Include the following cell at the top of your Colab notebook:

```python
!pip install git+https://github.com/itsjohnward/colabtools.git
from colabtools import COLAB
```

Just by importing the library, two things happen:

1. Tensorflow is automatically configured to use a GPU or TPU if one is available.
2. Your Google Drive is automatically mounted at `/content/drive`.

You can also use the `COLAB` boolean to check if you're running in Colab.
