#### show image

        >>> import PIL
        >>> PIL.__version__
        '7.0.0'
        >>> from PIL import Image
        >>> img = Image.open('C:\\Users\\mitchann\\Downloads\\mithuns.jpeg')
        >>> img.show() # shows normal image

#### convert to grey image

        >>> img = Image.open('C:\\Users\\mitchann\\Downloads\\mithuns.jpeg').convert("L")
        >>> img.show() 

