import numpy as np 
import cv2


def find_bbox(keypoints): 
    xmin = keypoints[:, 0].min()
    ymin = keypoints[:, 1].min()
    xmax = keypoints[:, 0].max()
    ymax = keypoints[:, 1].max()
    return xmin, ymin, xmax, ymax


def drawBBox(img, joints):
    img_ = img.copy()
    xmin, ymin, xmax, ymax = find_bbox(joints)
    color = (0, 0, 255)
    cv2.line(img_, (int(xmin), int(ymin)), (int(xmin), int(ymax)), color, thickness=2)
    cv2.line(img_, (int(xmin), int(ymin)), (int(xmax), int(ymin)), color, thickness=2)
    cv2.line(img_, (int(xmax), int(ymax)), (int(xmin), int(ymax)), color, thickness=2)
    cv2.line(img_, (int(xmax), int(ymax)), (int(xmax), int(ymin)), color, thickness=2)
    cv2.imwrite('bbox.jpg', img_)


def drawKeyPoints(img, keypoints, color):
    img_ = img.copy()
    for keypoint in keypoints:
        cv2.circle(img_, (int(keypoint[0]), int(keypoint[1])), radius=1, color=color, thickness=1)
    cv2.imwrite('keypoints.jpg', img_)


def drawMesh(img, vertices, faces, lineColor): 
    pass


def visSkeleton(img, joints): 
    pass


def drawJoints(img, joints, links, lineColor, keypointColor):
    pass
