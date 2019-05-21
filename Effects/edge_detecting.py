# coding: utf-8
# python3.5.3
# edge_detecting.py

import cv2

from skimage import data, segmentation
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("--content", type=str)
parser.add_argument('--output', type=str)
# blurred staus     >>>     normal=< 7
parser.add_argument('--blurred', type=int)
args = parser.parse_args()

global image, minT, maxT

#  Callback function for minimum threshold trackbar.
def adjustMinT(v):
    global minT
    minT = v
    cannyEdge()

# Callback function for maximum threshold trackbar.
def adjustMaxT(v):
    global maxT
    maxT = v
    cannyEdge()


###################################
#  Main program begins here. 
###################################


# load original image as grayscale
image = cv2.imread(filename=args.content, flags=cv2.IMREAD_GRAYSCALE)

# set up display window with trackbars for minimum and maximum threshold
# values
# 추후에 미세값 조정하기 위한 부분으로 현재는 미완료부분임.
cv2.namedWindow(winname = "edges", flags = cv2.WINDOW_NORMAL)

minT = 30
maxT = 150

# cv2.createTrackbar() does not support named parameters
cv2.createTrackbar("minT", "edges", minT, 255, adjustMinT)
cv2.createTrackbar("maxT", "edges", maxT, 255, adjustMaxT)

# Smoothing without removing edges.
gray_filtered = cv2.bilateralFilter(image, 7, 50, 50)

# minT, maxT 값을 밖으로 빼내서 조정값으로 변경해야함. 추후
edge = cv2.Canny(image=gray_filtered, threshold1=minT, threshold2=maxT)

# subtract 방식이 색상 미세조정이 가능해서 더 성능이 좋아보여, bitwise 를 대기로 함.
# edge = cv2.bitwise_not(edge)
edge = cv2.subtract(250, edge)

cv2.imwrite(args.output, edge)