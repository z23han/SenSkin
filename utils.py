import numpy as np

class Base:

    def save_file(self, image_obj, image_folder, image_name):
        
        size = image_obj.size
        pixels = image_obj.convert('RGB')

        width = size[0]
        height = size[1]

        for i in range(width):
            for j in range(height):
                image_obj.putpixel((i, j), (pixels[i, j][0], pixels[i, j][1], pixels[i, j][2]))
        image_obj.save(os.path.join(image_folder, image_name))
    

    """
    the method uses algorithm I(x) = 0.3 * R(x) + 0.59 * G(x) + 0.11 * B(x)
    """
    def convert_rbg(self, pixels):
        out_pixels = []

        width, height = len(pixels), len(pixels[0])

        for i in range(width):
            row = []
            for j in range(height):
                pix_r = pixels[i][j][0]
                pix_g = pixels[i][j][1]
                pix_b = pixels[i][j][2]
                pix_t = (0.3 * pix_r + 0.59 * pix_g + 0.11 * pix_b) / 255.0
                row.append(pix_t)
            out_pixels.append(row)

        return np.array(out_pixels)