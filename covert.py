import os
import numpy as np
from nibabel.testing import data_path
import nibabel as nib
import cv2


def convertnii_to_jpg(path, save_path):
    li = [file for file in os.listdir(path) if file.endswith(".gz")]
    img_arr = []
    examples = []
    for i in range(len(li)):
        #print(li[i])
        example = path+li[i]
        examples.append(example)
        img = nib.load(example)
        img_arr.append(img)

    final_img = []
    for i in range(len(examples)):
        image = nib.load(examples[i])
        final_img.append(image)

    data_ = []
    for i in range(len(final_img)):
        image_data = image.get_fdata()
        data_.append(image_data)

    print(data_[0][0].shape)
    for j in range(len(data_)):
        for i in range(3):
            print(i, j, i+j, li[j])
            cv2.imwrite("{}/image{}.jpg".format(save_path, li[j]+str(i)), data_[j][i])

convertnii_to_jpg("anat/", "anat_jpg")
