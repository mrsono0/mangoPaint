# coding: utf-8
# python3.5.3
# segment.py
# ------------------------------------------------------------------------
# purpose:
#   MyStudio 1레벨중 선택한 이미지 파일을 조각내는 기능, 조각 조절기능을 구현함.

import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
import collections

from PIL import Image
from skimage import data, io, segmentation, color, measure, filters
from skimage.future import graph
from skimage.transform import resize
from skimage.color import rgb2gray
from skimage.color.adapt_rgb import adapt_rgb, each_channel, hsv_value
from skimage.exposure import rescale_intensity
from operator import itemgetter

from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import ObjectProperty, StringProperty

from kivymd.imagelists import SmartTile


class Segment(Screen):
    events_callback = ObjectProperty(None)
    sets = ObjectProperty(None)
    title_previous = StringProperty('')  # 액션바
    selectedImagePath = StringProperty('')

    def __init__(self, **kwargs):  # selectedImagePath 받아온 것으로 이미지 보여주고.
        super(Segment, self).__init__(**kwargs)
        Clock.schedule_once(self.create_segment_screen, 1)

    # 이미지 보여주고, 수 초후 segment 조각내기 실행
    def create_segment_screen(self, imagePath):
        # self.selectedImagePath = imagePath
        # self.ids.myimage.source = self.selectedImagePath
        pass

    @adapt_rgb(each_channel)
    def sobel_each(image):
        return filters.sobel(image)

    @adapt_rgb(hsv_value)
    def sobel_hsv(image):
        return filters.sobel(image)

    def as_gray(image_filter, image, *args, **kwargs):
        gray_image = rgb2gray(image)
        return image_filter(gray_image, *args, **kwargs)

    @adapt_rgb(as_gray)
    def sobel_gray(image):
        return filters.sobel(image)

    def _weight_mean_color(graph, src, dst, n):
        """Callback to handle merging nodes by recomputing mean color.
        The method expects that the mean color of `dst` is already computed.

        Parameters
        ----------
        graph: RAG
            The graph under consideration.
        src, dst: int
            The vertices in `graph` to be merged.
        n: int
            A neighbor of `src` or `dst` or both.

        Returns
        -------
        data: dict
            A dictionary with the `"weight"` attribute set as the absolute
            difference of the mean color between node `dst` and `n`.
        """    
        diff = graph.node[dst]['mean color'] - graph.node[n]['mean color']
        diff = np.linalg.norm(diff)
        return {'weight': diff}

    def merge_mean_color(graph, src, dst):
        """Callback called before merging two nodes of a mean color distance graph.
        This method computes the mean color of `dst`.

        Parameters
        ----------
        graph: RAG
            The graph under consideration.
        src, dst: int
            The vertices in `graph` to be merged.
        """    

        graph.node[dst]['total color'] += graph.node[src]['total color']
        graph.node[dst]['pixel count'] += graph.node[src]['pixel count']
        graph.node[dst]['mean color'] = (graph.node[dst]['total color'] / graph.node[dst]['pixel count'])
        
        

    def choose_rep_rgb(result, COLOR_TYPE=1):
        """choose representative rgb color.
        
        Parameters
        ----------
        result: list
            input/output data
        color_count: palette color count (24/32/64/128/256)
        
        Returns
        -------
        result: list [prop.label, prop.centroid, prop.area, (r,g,b)]
        """
        
        for i in range(len(result)):
            rep_rgb = find_rgb(result[i][3][0], result[i][3][1], result[i][3][2], COLOR_TYPE)
            result[i].extend([rep_rgb])
        return result


    def find_rgb(r, g=None, b=None, COLOR_TYPE=1):
        """
        Return the nearest xterm 256 color code from rgb input.
        """
        c = r if isinstance(r, list) else [r, g, b]
        best = {}
        if COLOR_TYPE == 2:
            lists = COLORS_128
        elif COLOR_TYPE == 3:
            lists = COLORS_64
        else:
            lists = COLORS_256

        for index, item in enumerate(lists):
            d = _distance(item, c)
            if(not best or d <= best['distance']):
                best = {'distance': d, 'index': index}

        if 'index' in best:
            return best['index']
        else:
            return 1


    def _hex2rgb(hexa):
        r = int(hexa[0:2], 16)
        g = int(hexa[2:4], 16)
        b = int(hexa[4:6], 16)
        return [r, g, b]


    def _distance(a, b):
        x = (a[0] - b[0]) ** 2
        y = (a[1] - b[1]) ** 2
        z = (a[2] - b[2]) ** 2
        return np.sqrt(x + y + z)


    COLORS_256 = list(map(_hex2rgb, [
        "000000","800000","008000","808000","000080","800080","008080","c0c0c0","808080","ff0000",
        "00ff00","ffff00","0000ff","ff00ff","00ffff","ffffff","000000","00005f","000087","0000af",
        "0000d7","0000ff","005f00","005f5f","005f87","005faf","005fd7","005fff","008700","00875f",
        "008787","0087af","0087d7","0087ff","00af00","00af5f","00af87","00afaf","00afd7","00afff",
        "00d700","00d75f","00d787","00d7af","00d7d7","00d7ff","00ff00","00ff5f","00ff87","00ffaf",
        "00ffd7","00ffff","5f0000","5f005f","5f0087","5f00af","5f00d7","5f00ff","5f5f00","5f5f5f",
        "5f5f87","5f5faf","5f5fd7","5f5fff","5f8700","5f875f","5f8787","5f87af","5f87d7","5f87ff",
        "5faf00","5faf5f","5faf87","5fafaf","5fafd7","5fafff","5fd700","5fd75f","5fd787","5fd7af",
        "5fd7d7","5fd7ff","5fff00","5fff5f","5fff87","5fffaf","5fffd7","5fffff","870000","87005f",
        "870087","8700af","8700d7","8700ff","875f00","875f5f","875f87","875faf","875fd7","875fff",
        "878700","87875f","878787","8787af","8787d7","8787ff","87af00","87af5f","87af87","87afaf",
        "87afd7","87afff","87d700","87d75f","87d787","87d7af","87d7d7","87d7ff","87ff00","87ff5f",
        "87ff87","87ffaf","87ffd7","87ffff","af0000","af005f","af0087","af00af","af00d7","af00ff",
        "af5f00","af5f5f","af5f87","af5faf","af5fd7","af5fff","af8700","af875f","af8787","af87af",
        "af87d7","af87ff","afaf00","afaf5f","afaf87","afafaf","afafd7","afafff","afd700","afd75f",
        "afd787","afd7af","afd7d7","afd7ff","afff00","afff5f","afff87","afffaf","afffd7","afffff",
        "d70000","d7005f","d70087","d700af","d700d7","d700ff","d75f00","d75f5f","d75f87","d75faf",
        "d75fd7","d75fff","d78700","d7875f","d78787","d787af","d787d7","d787ff","d7af00","d7af5f",
        "d7af87","d7afaf","d7afd7","d7afff","d7d700","d7d75f","d7d787","d7d7af","d7d7d7","d7d7ff",
        "d7ff00","d7ff5f","d7ff87","d7ffaf","d7ffd7","d7ffff","ff0000","ff005f","ff0087","ff00af",
        "ff00d7","ff00ff","ff5f00","ff5f5f","ff5f87","ff5faf","ff5fd7","ff5fff","ff8700","ff875f",
        "ff8787","ff87af","ff87d7","ff87ff","ffaf00","ffaf5f","ffaf87","ffafaf","ffafd7","ffafff",
        "ffd700","ffd75f","ffd787","ffd7af","ffd7d7","ffd7ff","ffff00","ffff5f","ffff87","ffffaf",
        "ffffd7","ffffff","080808","121212","1c1c1c","262626","303030","3a3a3a","444444","4e4e4e",
        "585858","606060","666666","767676","808080","8a8a8a","949494","9e9e9e","a8a8a8","b2b2b2",
        "bcbcbc","c6c6c6","d0d0d0","dadada","e4e4e4","eeeeee"]))

    COLORS_128 = list(map(_hex2rgb, [
        "000000","008000","000080","008080","808080","00ff00","0000ff","00ffff","000000","000087",
        "0000d7","005f00","005f87","005fd7","008700","008787","0087d7","00af00","00af87","00afd7",
        "00d700","00d787","00d7d7","00ff00","00ff87","00ffd7","5f0000","5f0087","5f00d7","5f5f00",
        "5f5f87","5f5fd7","5f8700","5f8787","5f87d7","5faf00","5faf87","5fafd7","5fd700","5fd787",
        "5fd7d7","5fff00","5fff87","5fffd7","870000","870087","8700d7","875f00","875f87","875fd7",
        "878700","878787","8787d7","87af00","87af87","87afd7","87d700","87d787","87d7d7","87ff00",
        "87ff87","87ffd7","af0000","af0087","af00d7","af5f00","af5f87","af5fd7","af8700","af8787",
        "af87d7","afaf00","afaf87","afafd7","afd700","afd787","afd7d7","afff00","afff87","afffd7",
        "d70000","d70087","d700d7","d75f00","d75f87","d75fd7","d78700","d78787","d787d7","d7af00",
        "d7af87","d7afd7","d7d700","d7d787","d7d7d7","d7ff00","d7ff87","d7ffd7","ff0000","ff0087",
        "ff00d7","ff5f00","ff5f87","ff5fd7","ff8700","ff8787","ff87d7","ffaf00","ffaf87","ffafd7",
        "ffd700","ffd787","ffd7d7","ffff00","ffff87","ffffd7","080808","1c1c1c","303030","444444",
        "585858","666666","808080","949494","a8a8a8","bcbcbc","d0d0d0","e4e4e4"]))

    COLORS_64 = list(map(_hex2rgb, [
        "008000","008080","00ff00","00ffff","000087","005f00","005fd7","008787","00af00","00afd7",
        "00d787","00ff00","00ffd7","5f0087","5f5f00","5f5fd7","5f8787","5faf00","5fafd7","5fd787",
        "5fff00","5fffd7","870087","875f00","875fd7","878787","87af00","87afd7","87d787","87ff00",
        "87ffd7","af0087","af5f00","af5fd7","af8787","afaf00","afafd7","afd787","afff00","afffd7",
        "d70087","d75f00","d75fd7","d78787","d7af00","d7afd7","d7d787","d7ff00","d7ffd7","ff0087",
        "ff5f00","ff5fd7","ff8787","ffaf00","ffafd7","ffd787","ffff00","ffffd7","1c1c1c","444444",
        "666666","949494","bcbcbc","e4e4e4"]))

    def _report_result(img_origin, properties):

    # ====================================
    # display Action Level for more information
    # ====================================
        print("img.shape: " + str(img_origin.shape))
        print()
        print("segments count: " + str(len(properties)))
        print()

        if len(properties) > 3000:
            print("Lelel 5 : Expert ==> Warnning !!!")
        elif 2000 < len(properties) < 3000:
            print("Level 4 : Professional")
        elif 1000 < len(properties) < 2000:
            print("Level 4 : Standard")
        elif 500 < len(properties) < 1000:
            print("Level 2 : Begginer")
        else:
            print("Level 1 : Starter")

        print()    
        seg_colors = [result[x][4] for x in range(len(result))]
        counter = collections.Counter(seg_colors)
        _count = len(counter.items()) - len(counter.most_common(30))
        _list1 = sorted(counter.items(), key=itemgetter(1), reverse=True)
        _list2 = counter.most_common(30)
        
        print("Colors count: " + str(len(counter.items())))
        print(str(_list1))
        print()
        if len(counter.items()) < 30:
            print("Most used colors: " + str(len(counter.items())))
        else:
            print("Most used colors: 30")
        print(str(_list2))
        print()

        print("Remained colors adjusting: " , str(len(_list1) - len(_list2)))
        print([item for item in _list1 if item not in _list2])

    #     _remainer = counter - counter.most_common(30)
    #     print(_remainer)

    def callback(self, obj):
        print(obj.source)
        self.selectedImagePath = obj.source
        self.parent.current = 'effects'















def merge_mean_color(graph, src, dst):
    """Callback called before merging two nodes of a mean color distance graph.
    This method computes the mean color of `dst`.

    Parameters
    ----------
    graph: RAG
        The graph under consideration.
    src, dst: int
        The vertices in `graph` to be merged.
    """    

    graph.node[dst]['total color'] += graph.node[src]['total color']
    graph.node[dst]['pixel count'] += graph.node[src]['pixel count']
    graph.node[dst]['mean color'] = (graph.node[dst]['total color'] / graph.node[dst]['pixel count'])




# ====================================
# Hyper Parameters
# ====================================

PIC_NAME = "/home/ubuntu/Pictures/test_iris_result.png"

# kernel_size value controls the size of segments ( >= 1. )
# ex)  1.0(Standard): 1,000ea. ==>  1.5: 600ea.  ==>  2.1: 370ea.  ==> 3.0: 288ea.  ==> 4.0: 255ea.
KERNEL_SIZE = 1.

# color type:  1: 256 colors  ==>  2: 128 colors  ==> 3: 64 colors  ==> 
#              4: 36 colors  ==>  5: 24 colors  ==> 6: 12 colors
COLOR_TYPE = 1

# thresh : segments size control  >>>   30: small   ==>    20: medium    ==>   10:large
THREASH = 20

# blurred staus     >>>     normal:7
BLURRED = 7


# ====================================
# read Image 
# ====================================
# For Reading : No Blurred, Just Image
img_origin = data.imread('Screens/resources/imgs/mango.jpg')


# ====================================
# initialize Figure 
# ====================================
# 3. color mode
# labels = segmentation.slic(img_origin, compactness=200, n_segments=5000) ==> another type 
labels = segmentation.quickshift(img_origin, kernel_size=KERNEL_SIZE, ratio=0.3, convert2lab=False, random_seed=10)

g = graph.rag_mean_color(img_origin, labels)

labels2 = graph.merge_hierarchical(labels, g, thresh=THREASH, rag_copy=False,
                                   in_place_merge=True,
                                   merge_func=merge_mean_color,
                                   weight_func=_weight_mean_color)

properties = measure.regionprops(labels2)


for i, prop in enumerate(properties):
    try:
        r, g, b = rgb_im.getpixel((prop.centroid[1], prop.centroid[0]))
    except:
        print("Prop.centroid Exception ===> " + str(prop.centroid[1]) + " : " + str(prop.centroid[0]))
        continue
    
    temp = [prop.label, prop.centroid, prop.area, (r,g,b)]
    result.append(temp)

result = list(result)

# color type      1(default): 256colors,  2: 128colors,    3:64colors
result = choose_rep_rgb(result, 3)
_report_result(img_origin, properties)


_centroids = [result[x][1] for x in range(len(result))]
# alpha ????  image_alpha ?????? 
out = color.label2rgb(labels2, img_origin, kind='avg')



for x in range(len(result)):
    ax[2].text(_centroids[x][1], _centroids[x][0], result[x][4])

ax[2].imshow(segmentation.mark_boundaries(out, labels2, color=(218,218,218), mode='inner'))
ax[2].set_title("color mode")



    # def make_base_canvas(self):

    #     for i in range(out.shape[0]):
    #         for j in range(out.shape[1]):
    #             for k in range(out.shape[2]):
    #                 if out[i,j,k] != 0:
    #                     out[i,j,k] = 255
    #                 else:
    #                     out[i,j,k] = 108

    #     for x in range(len(result)):
    #         ax[3].text(_centroids[x][1], _centroids[x][0], result[x][4])

    #     ax[3].imshow(segmentation.mark_boundaries(out, labels2, color=(108, 108, 108), mode='inner'))
    #     ax[3].set_title("base mode")        


# 4-1. gray mode --> base mode
# rgb2gray_val = edges[:,:] + out[:,:,0]
# print(rgb2gray_val.shape)
# print(rgb2gray_val)
    
# for i in range(rgb2gray_val.shape[0]):
#     for j in range(rgb2gray_val.shape[1]):
#         if rgb2gray_val[i,j] != 0:
#             rgb2gray_val[i,j] = 255

# for x in range(len(result)):
#     ax[3].text(_centroids[x][1], _centroids[x][0], result[x][4])
            
# ax[3].imshow(segmentation.mark_boundaries(out, labels2, color=(108, 108, 108), mode='inner'))
# ax[3].set_title("gray mode")


plt.tight_layout()
plt.show()