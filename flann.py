# Daniel Agudelo
# Brandon Carty
# Robotic Systems
# Object Recognition
# Used code from
# http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_feature2d/py_matcher/py_matcher.html
import numpy as np
import cv2
from Result import Result
import Query


def flannMatching(obj_query, query, dataset):

    img1 = cv2.imread(query,0) # queryImage
    obj_result = Result("Flann", "good") #Create a Result object for the Flann Test
    sift = cv2.SIFT() #Create a SIFT object detector
    kp1, des1 = sift.detectAndCompute(img1, None) #Calculate keypoints and descriptors for the query img
    results = {} #results dictionary key: dataset test image's name, value: number of matches

    for index in range(len(dataset)):
        matches = []
        counter = 0

        img2 = cv2.imread(dataset[index],0) # dataset test image

        # find the keypoints and descriptors with SIFT
        kp2, des2 = sift.detectAndCompute(img2,None)

        # FLANN parameters
        FLANN_INDEX_KDTREE = 0
        index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
        search_params = dict(checks=100) # or pass empty dictionary
        flann = cv2.FlannBasedMatcher(index_params,search_params)
        matches = flann.knnMatch(des1,des2,k=2)

        # Need to draw only good matches, so create a mask
        matchesMask = [[0,0] for i in xrange(len(matches))]

        # ratio test as per Lowe's paper
        for i,(m,n) in enumerate(matches):
            if m.distance < 0.7*n.distance:
                matchesMask[i]=[1,0]
                #count matches
                counter += 1

        #store amount of matches found after applying the ratio test
        results[dataset[index]] = counter


    results = sorted([(v, k) for (k, v) in results.items()], reverse=True)

    #Store 4 best results into Result's object
    for index in range(4):
        obj_result.add_match(str(results[index][1]))

    #Store results of this test in the Query object pertaining to the given query image
    obj_query.add_result(obj_result)


    return