# Daniel Agudelo
# Brandon Carty
# Robotic Systems
# Object Recognition
# Used code from
# http://www.pyimagesearch.com/2014/07/14/3-ways-compare-histograms-using-opencv-python/
import cv2
from Result import Result

def histogramMatching(obj_query, query, dataset):

    dict_files_img = {}
    dict_files_hist = {}

    #read in all images in dataset and store their histograms in dict_files_hist
    for index in range(len(dataset)):
        img = cv2.imread(dataset[index])
        dict_files_img[dataset[index]] = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        hist = cv2.calcHist([img], [0, 1, 2], None, [8, 8, 8],
                            [0, 256, 0, 256, 0, 256])
        hist = cv2.normalize(hist).flatten()
        dict_files_hist[dataset[index]] = hist

    #Using the COrrelation method
    OPENCV_METHODS = ("Correlation", cv2.cv.CV_COMP_CORREL)

    # All four of the histogram matching methods in OpenCV
    # OPENCV_METHODS = (
    #     ("Correlation", cv2.cv.CV_COMP_CORREL),
    #     ("Chi-Squared", cv2.cv.CV_COMP_CHISQR),
    #     ("Intersection", cv2.cv.CV_COMP_INTERSECT),
    #     ("Hellinger", cv2.cv.CV_COMP_BHATTACHARYYA))



    results = {}
    reverse = False

    #create a Result object for the given Histogram method (correlation, chi-squared, intersection, hellinger)
    #methodName sets the variation variable
    obj_result = Result("Histogram","Correlation")

    reverse = True

    for (k, hist) in dict_files_hist.items():
        # compute the distance between the two histograms
        # using the method and update the results dictionary
        d = cv2.compareHist(dict_files_hist[query], hist, cv2.cv.CV_COMP_CORREL)
        results[k] = d

    # sort the results
    results = sorted([(v, k) for (k, v) in results.items()], reverse=reverse)


    for index in range(4):
        obj_result.add_match(str(results[index][1]))



    obj_query.add_result(obj_result)

    return;
