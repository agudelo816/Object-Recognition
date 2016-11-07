# Daniel Agudelo
# Brandon Carty
# Robotic Systems
# Object Recognition
# Used code from
# http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_feature2d/py_matcher/py_matcher.html

import cv2
import numpy as np
from Result import Result
import Query

def siftMatching(obj_query, query, dataset):
    #read images in as grayscale
    img1 = cv2.imread(query, 0)
    results = {}

    #Create sift detector object
    sift = cv2.SIFT()

    # Detect keypoints and compute descriptors for query image
    kp1, des1 = sift.detectAndCompute(img1, None)

    for index in range(len(dataset)):

        img2 = cv2.imread(dataset[index], 0)

        #Create Result object
        obj_result = Result("Sift","good")

        #Detect keypoints and compute descriptors for test image
        kp2,des2 = sift.detectAndCompute(img2, None)

        bf = cv2.BFMatcher()
        matches = bf.knnMatch(des1,des2,k=2)

        good = []
        #apply ratio test
        for m,n in matches:
            if m.distance < 0.75*n.distance:
                good.append([m])

        #store results = amount of matches found after ratio test
        results[dataset[index]] = len(good)

    #Sort results
    results = sorted([(v, k) for (k, v) in results.items()], reverse=True)

    #store best four matches in Result object
    for i in range(4):

        obj_result.add_match(str(results[i][1]))

    #Store result in query object
    obj_query.add_result(obj_result)

    return;
