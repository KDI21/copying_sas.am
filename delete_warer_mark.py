import csv
import requests
import re
import cv2
import numpy as np
from matplotlib import pyplot as plt
#
# class Water_mark(object):
#
#     def delete_water_mark(self):
#         maska =



# kernel = np.ones((5,5),np.float32)/25
# dst = cv2.filter2D(img,-1,kernel)
# dst = cv2.GaussianBlur(img,(5,5),0)
# plt.subplot(121),plt.imshow(img),plt.title('Original')
# plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
# plt.xticks([]), plt.yticks([])
# plt.show()

def copying_product_table(file_obj):
    reader = csv.DictReader(file_obj, delimiter=';')
    i = 0
    for line in reader:
        product_name = line['name_product']
        product_img = line['img_product']
        product_item = open("./csv/product_item_en_one to one.csv", 'r')
        product_list = csv.DictReader(product_item, delimiter=';')
        for lin in product_list:
            if product_name == lin['name_product']:
                print(product_name)
                print(product_img)
                img = cv2.imread('./img/'+lin['img_product']+'',)
                width_percent = 222 # percent of original size
                height_percent = 200 # percent of original size
                width = int(img.shape[1] * width_percent / 100)
                height = int(img.shape[0] * height_percent / 100)
                dim = (width, height)
                # resize image

                resized = cv2.resize(img, dim, interpolation = cv2.INTER_CUBIC)
                print(resized.shape)
                cv2.imwrite('./test1/'+product_img+'', resized)
        # print(product_name)
        product_item.close()



                # print('Resized Dimensions : ',resized.shape)
                # print(line['img_product'])
                # alpha = 2.2
                # beta = -160
                # new = alpha * img + beta
                # new = np.clip(new, 0, 255).astype(np.uint8)
                # cv2.resize(src, dsize[, dst[, fx[, fy[, interpolation]]]])
                # # assert i != 100
                # i = i + 1
                #







if __name__ == "__main__":
    with open("./csv/product_list_en.csv") as f_obj:
        copying_product_table(f_obj)
