from image import ImageObject
import os
from canny import *
from utils import Base
import cv2
from matplotlib import pyplot as plt
from PIL import Image


def main():

    base = Base()

    try:
        curr_folder = os.getcwd()
        image_name = 'img2.jpg'
        img_obj = ImageObject(os.path.join(curr_folder, 'images', image_name))

        convert_pix = base.convert_rbg(img_obj.rgb)

        retgrad, x_indices, y_indices = canny(convert_pix, 2.0, thresHigh=45, thresLow=30)

        """
        plt.scatter(x_indices, y_indices, s=1)
        plt.title("edge points")
        plt.xlabel('x-axis')
        plt.ylabel('y-axis')
        plt.show()
        """

        new_img_obj = Image.new(img_obj.mode, img_obj.size)
        width, height = img_obj.size

        for i in range(width):
            for j in range(height):
                pixel = ()
                if retgrad[i][j] == 1:
                    pixel = (255, 255, 255)
                else:
                    pixel = (0, 0, 0)
                new_img_obj.putpixel((i, j), pixel)
        
        
        new_img_obj.save(os.path.join(curr_folder, 'images', 'image2_out.jpg'))
        

    except Exception as ex:
        print(ex)



if __name__ == "__main__":

    main()