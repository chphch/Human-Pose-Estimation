import numpy as np 
import cv2


def find_bbox(keypoints): 

    return bbox


def drawKeyPoints(img, keypoints, color):
    img_ = img.copy()
    for keypoint in keypoints:
        cv2.circle(img_, (int(keypoint[0]), int(keypoint[1])), radius=1, color=color, thickness=1)
    cv2.imwrite('test.jpg', img_)


def drawMesh(img, vertices, faces, lineColor): 
    pass


def visSkeleton(img, joints): 
    pass


def drawJoints(img, joints, links, lineColor, keypointColor):
    pass
