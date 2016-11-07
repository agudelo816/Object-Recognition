# Daniel Agudelo
# Brandon Carty
# Robotic Systems
# Object Recognition
# Used code from
# https://opencv-python-tutroals.readthedocs.io/en/latest/
# py_tutorials/py_imgproc/py_template_matching/py_template_matching.html#template-matching

import cv2
import numpy as np
import matplotlib.pyplot as plt
from Result import Result


def tempMatching(obj_query, query, dataset):
    "Perform template image over scene image andm template matching: Slide get scores for matches at each position"

    # Load puzzle image in gray
    img = cv2.imread(query, 0)

    # Make a copy of puzzle image in color
    img_c = cv2.imread(query, 1)

    methods = ['cv2.TM_SQDIFF']
    method_names = ['Squared Difference']

    for index in range(len(methods)):
        method = eval(methods[index])

        # create a Result object for the given Histogram method (cross correlation, cross correlation normalized etc)
        # methodName sets the variation variable
        obj_result = Result("Template", method_names[index])

        results = {}
        # iterate through dataset performing template matching for given puzzle/query image
        for i in range(len(dataset)):
            # Load query image
            template = cv2.imread(dataset[i], 0)

            #  Get the dimensions of Query image
            h, w = template.shape[:2]

            # Apply template Matching
            res = cv2.matchTemplate(img, template, method)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)


            # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
            if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
                top_left = min_loc
                match_val = min_val
            else:
                top_left = max_loc
                match_val = max_val

            results[dataset[i]] = match_val

        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            #sort matches in ascending
            reverse = False

        else:
            reverse = True


        results = sorted([(v, k) for (k, v) in results.items()], reverse=reverse)
        #store best four results in Result object
        for j in range(4):
            obj_result.add_match(str(results[j][1]))

        obj_query.add_result(obj_result)

    return;


