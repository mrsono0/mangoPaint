# coding: utf-8
# python3.5.3
# oil_coloring.py
# Reference: http://supercomputingblog.com/graphics/oil-painting-algorithm/


from PIL import Image
import numpy as np

from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("--content", type=str)
parser.add_argument('--output', type=str)
parser.add_argument('--radius', type=int)
parser.add_argument('--intensity', type=int)
parser.add_argument('--cuda', type=int)
args = parser.parse_args()


def read_image(file_path):
    content = Image.open(file_path)
    width, height = content.size
    return content, width, height


# Step 1
# For each pixel, all pixels within the radius will have to be examined.
# Pixels within the radius of the current pixel will be referred to as
# sub-pixels.
# For each sub-pixel, calculate the intensity, and determine which intensity
# bin that intensity number falls into. Maintain a counter for each intensity
# bin, which will count the number of sub-pixels which fall into each intensity
# bin. Also maintain the total red, green, and blue values for each bin, later;
# these may be used to determine the final value of the pixel.

# Step 2
# For each pixel, determine which intensity bin has the most number of pixels
# in it.
# Yes, this can be rolled into step 1, but for the purposes of this tutorial,
# this way is simpler to understand the code.

# Step 3
# After we determine which intensity the pixel represents, as determined by
# the intensity bin with the most pixels, we can then determine the final color
# of the pixel by taking the total red, green, and blue values in that specific
# bin, and dividing that by the total number of pixels in that specific
# intensity bin.


def oil_painting(content, radius, Intensity, width, height):
    final_img = Image.new("RGB", (width, height), "white")
    print('pixel:', content.getpixel((0, 0)))
    print('width, height:', width, height)
    for nX in range(radius, width - radius):
        for nY in range(radius, height - radius):
            # print('nX, nY: ', nX, nY)
            nSumR = np.zeros((256, ), dtype=np.int)
            nSumG = np.zeros((256, ), dtype=np.int)
            nSumB = np.zeros((256, ), dtype=np.int)
            nIntensityCount = np.zeros((256, ), dtype=np.int)
            for nX_O in range((-1)*radius, radius+1):
                for nY_O in range((-1)*radius, radius+1):
                    nR = content.getpixel((nX + nX_O, nY + nY_O))[0]
                    nG = content.getpixel((nX + nX_O, nY + nY_O))[1]
                    nB = content.getpixel((nX + nX_O, nY + nY_O))[2]
                    CurIntensity = \
                        min(int((((nR+nG+nB)/3.)*Intensity)//255), 255)
                    i = CurIntensity
                    nIntensityCount[i] += 1
                    nSumR[i] += nR
                    nSumG[i] += nG
                    nSumB[i] += nB
            nMaxIndex = np.argmax(nIntensityCount)
            nCurMax = nIntensityCount[nMaxIndex]
            final_color = []
            final_color.append(int(nSumR[nMaxIndex] // nCurMax))
            final_color.append(int(nSumG[nMaxIndex] // nCurMax))
            final_color.append(int(nSumB[nMaxIndex] // nCurMax))
            final_img.putpixel((nX, nY), tuple(final_color))
    final_img.save(args.output)


if __name__ == '__main__':
    content, width, height = read_image(args.content)
    oil_painting(content, args.radius, args.intensity, width, height)
