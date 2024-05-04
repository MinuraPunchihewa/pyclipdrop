# PyClipdrop
Copyright © 2023 Minura Punchihewa

PyClipdrop is a Python library for interacting with the Clipdrop API. [Clipdrop](https://clipdrop.co/) is a service that allows you to perform a variety of tasks on images such removing the background, removing text, and more.

## Installation
### With pip
```
pip install pyclipdrop
```

## Usage
The library will first need to be configured with a Clipdrop API key. You can get an API key by signing up for the [Clipdrop API](https://clipdrop.co/apis). Once you have an API key, you can either set it to the `CLIPDROP_API_KEY` environment variable or pass it to the constructor of the `ClipdropClient` class.

```python
from pyclipdrop import ClipdropClient

client = ClipdropClient('your-api-key')
# OR, if you have the API key set as an environment variable
client = ClipdropClient()
```

This client can now be used to perform a variety of tasks.

### Image to Text
```python
client.image_to_text(
    prompt='shot of vaporwave fashion dog in miami', 
    output_file='path/to/output.png'
)
```

### Remove Background
```python
client.remove_background(
    image_file='path/to/input.png', 
    output_file='path/to/output.png'
)
```

### Replace Background
```python
client.replace_background(
    image_file='path/to/input.png', 
    prompt='a cozy marble kitchen with wine glasses',
    output_file='path/to/output.png'
)
```

### Remove Text
```python
client.remove_text(
    image_file='path/to/input.png', 
    output_file='path/to/output.png'
)
```

# License
This code is licensed under the GNU GENERAL PUBLIC LICENSE. See LICENSE.txt for details.