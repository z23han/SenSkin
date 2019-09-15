from PIL import Image
import os
import numpy as np


class ImageObject:

    def __init__(self, file_name):
        self.file_name = file_name
        self.size = ()
        self.mode = ""
        self.format = ""
        self.rgb = []
        self.read_file()
        
    
    """ read file and get the image object
    """
    def read_file(self):
        with Image.open(self.file_name, 'r') as fin:

            self.mode, self.size, self.format = fin.mode, fin.size, fin.format

            rgb_im = fin.convert('RGB')
            pixels = rgb_im.load()

            width, height = self.size

            for i in range(width):
                row = []
                for j in range(height):
                    row.append(pixels[i, j])
                self.rgb.append(row)