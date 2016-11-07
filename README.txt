1) Open the Python project folder "ObjectRecognition" in PyCharm IDE
2) Open "main.py"
3) Run "main.py"

Results will print in this format for each query image:

Query: "Query Image name"
	Test: "Flann"
		Ranking: 
		1: Best match
		2: 2nd best match
		3: 3rd best match
		4: 4th best match
	Test: "Histogram"
		Ranking: 
		1: Best match
		2: 2nd best match
		3: 3rd best match
		4: 4th best match
	Test: "Template"
		Ranking: 
		1: Best match
		2: 2nd best match
		3: 3rd best match
		4: 4th best match
	Test: "Sift"
		Ranking: 
		1: Best match
		2: 2nd best match
		3: 3rd best match
		4: 4th best match

Results will print in this format for each method used (e.g Flann )



"Method name": queries= x matches= y mean= z
Query Image: "Query image 1 name" Score = (0-4)
... and so on for each query image
standard deviation= some value


e.g Flann
Flann: queries= 20 matches= 76 mean= 3.8
Query Image: ukbench00020.jpg Score= 4
Query Image: ukbench00021.jpg Score= 4
Query Image: ukbench00022.jpg Score= 4
Query Image: ukbench00023.jpg Score= 3
Query Image: ukbench00284.jpg Score= 3
Query Image: ukbench00285.jpg Score= 3
Query Image: ukbench00286.jpg Score= 4
Query Image: ukbench00287.jpg Score= 3
Query Image: ukbench00720.jpg Score= 4
Query Image: ukbench00721.jpg Score= 4
Query Image: ukbench00722.jpg Score= 4
Query Image: ukbench00723.jpg Score= 4
Query Image: ukbench01492.jpg Score= 4
Query Image: ukbench01493.jpg Score= 4
Query Image: ukbench01494.jpg Score= 4
Query Image: ukbench01495.jpg Score= 4
Query Image: ukbench09120.jpg Score= 4
Query Image: ukbench09121.jpg Score= 4
Query Image: ukbench09122.jpg Score= 4
Query Image: ukbench09123.jpg Score= 4
standard deviation= 0.4






