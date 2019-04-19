# coding: utf-8
# python3.5.3
# edge_detecting.py


import cv2
import matplotlib.pyplot as plt

from skimage import data, segmentation
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("--content", type=str)
parser.add_argument('--output', type=str)
# blurred staus     >>>     normal=< 7
parser.add_argument('--blurred', type=int)
args = parser.parse_args()


def read_image(content, blurred=7):
    img_origin = data.imread(content)
    img = cv2.medianBlur(img_origin, blurred)
    return img


def edge_detecting(image):
    fig, ax = plt.subplots(1, 1, figsize=(50, 100), sharex=True, sharey=True)
    edges = cv2.Canny(image, 70, 200, apertureSize=3)
    ax.imshow(segmentation.mark_boundaries(img, edges, (0, 0, 0)))
    fig.savefig(args.output)


if __name__ == '__main__':
    img = read_image(args.content, args.blurred)
    edge_detecting(img)
