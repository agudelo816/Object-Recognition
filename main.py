import histogram
import template
import sift
import flann
from Result import Result
from Query import Query
import math



def objectRecognition(mObj, methodType, query, dataset):
    if methodType == "Template Matching":
        template.tempMatching(mObj, query, dataset)
    elif methodType == "Histogram Matching":
        histogram.histogramMatching(mObj, query, dataset)
    elif methodType == "Sift Matching":
        sift.siftMatching(mObj, query, dataset)
    elif methodType == "Flann Matching":
        flann.flannMatching(mObj, query, dataset)


    return;

def main():

    #Dataset
    dataset = ['ukbench00020.jpg', 'ukbench00021.jpg', 'ukbench00022.jpg', 'ukbench00023.jpg',
               'ukbench00284.jpg', 'ukbench00285.jpg', 'ukbench00286.jpg', 'ukbench00287.jpg',
               'ukbench00720.jpg', 'ukbench00721.jpg', 'ukbench00722.jpg', 'ukbench00723.jpg',
               'ukbench01492.jpg', 'ukbench01493.jpg', 'ukbench01494.jpg', 'ukbench01495.jpg',
               'ukbench09120.jpg', 'ukbench09121.jpg', 'ukbench09122.jpg', 'ukbench09123.jpg'
               ]

    objects = []

    #each image in dataset will be used as a query
    for i in range(len(dataset)):

        #Create a Query object for each image
        #Each Query object will store reference to 4 Result objects (1 per test)
        #Each result object will store the top 4 matches returned for that test on that query image
        objects.append(Query(dataset[i]))

        objectRecognition(objects[i], "Flann Matching", dataset[i], dataset)
        objectRecognition(objects[i], "Histogram Matching", dataset[i], dataset)
        objectRecognition(objects[i], "Template Matching", dataset[i], dataset)
        objectRecognition(objects[i], "Sift Matching", dataset[i], dataset)

        #Print the ranking for each test
        print "Query image: "+dataset[i]
        for k in range(len(objects[i].results)):
            print "    Test: "+objects[i].get_result(k).type
            print "         Ranking: "
            for j in range(len(objects[i].get_result(k).matches)):
                print "         "+str(j+1)+": "+objects[i].get_result(k).get_match(j)

    #Multi dimensional dictionary to store Method used, Variation of method, # of queries, # of matches, and scores
    testing = {}


    testing['Flann'] = {}
    testing['Flann']['good'] = {}
    testing['Flann']['good']['queries'] = 0
    testing['Flann']['good']['matches'] = 0
    testing['Flann']['good']['results'] = []

    testing['Sift'] = {}
    testing['Sift']['good'] = {}
    testing['Sift']['good']['queries'] = 0
    testing['Sift']['good']['matches'] = 0
    testing['Sift']['good']['results'] = []


    testing['Template'] = {}
    testing['Template']['Squared Difference'] = {}
    testing['Template']['Squared Difference']['queries'] = 0
    testing['Template']['Squared Difference']['matches'] = 0
    testing['Template']['Squared Difference']['results'] = []


    testing['Histogram'] = {}
    testing['Histogram']['Correlation'] = {}
    testing['Histogram']['Correlation']['queries'] = 0
    testing['Histogram']['Correlation']['matches'] = 0
    testing['Histogram']['Correlation']['results'] = []

    #this loop is used to count the correct matches for each test on every query image
    for i in range(len(objects)):

        counter = i + 1;
        counter %= 4;

        if (counter == 0):
            counter -= 3
        else:
            counter -= 1

        print str(objects[i].query)
        str_type= ""
        str_var = ""

        for k in range(len(objects[i].results)):

            str_type = objects[i].get_result(k).type
            str_var = objects[i].get_result(k).variation

            mcounter = 0

            for j in range(len(objects[i].get_result(k).matches)):

                if (counter >= 0):
                    zcounter = i - counter
                else:
                    zcounter = i + counter

                for z in range(4):
                    if objects[i].results[k].get_match(j) == dataset[zcounter + z]:
                        #mcounter counts the correct matches
                        mcounter += 1


            testing[str_type][str_var]['queries'] += 1
            testing[str_type][str_var]['matches'] += mcounter
            testing[str_type][str_var]['results'].append(mcounter)

        n_queries = testing[str_type][str_var]['queries']
        n_matches = testing[str_type][str_var]['matches']




    str_type = ["Flann", "Histogram", "Sift", "Template"]
    str_var = ["good", "Correlation", "good", "Squared Difference"]

    #this loop calcualtes the mean and standard deviation of each test
    for i in range(len(str_type)):
        n_queries = testing[str_type[i]][str_var[i]]['queries']
        n_matches = testing[str_type[i]][str_var[i]]['matches']
        n_avg = n_matches/(n_queries * 1.0)
        print str_type[i]+": queries= "+str(n_queries)+" matches= "+str(n_matches)+" mean= "+str(n_avg)
        sum = 0
        for j in range(len(testing[str_type[i]][str_var[i]]['results'])):
            print "Query Image: "+dataset[j]+" Score= "+str(testing[str_type[i]][str_var[i]]['results'][j])

            diff = testing[str_type[i]][str_var[i]]['results'][j] - n_avg
            sq_diff = diff ** 2

            sum += sq_diff
        mean_sq_diff = sum / (n_queries * 1.0)
        std_dev = math.sqrt(mean_sq_diff)

        print "standard deviation= "+str(std_dev)





    pass;


if __name__ == "__main__": main()


