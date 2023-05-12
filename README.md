# pands-project
My interpretation / summary of Fishers Iris Data Set:

Fisher’s Data set is a widely used data set in the field of machine learning and statistics. It is a dataset that contains four measurements of fifty different sepals and petals of three different Iris species: Iris setosa, Iris virginica, and Iris versicolor. The measurements are as follows:
1.	Sepal length in cm
2.	Sepal width in cm
3.	Petal length in cm
4.	Petal width in cm
5.	The class of Iris:
    a.	Setosa
    b.	Versicolour
    c.	Virginica

The class of Iris is associated with each set of measurements to help layout a set of rules that we can use to estimate, using just the measurements, what a newly measured Iris is.
The dataset is significant in machine learning and data mining as it gives a pattern that can be followed with new data.
The data was collected at the same time, by the same person, using the same apparatus, all from the same location, which means the measurements should all be consistent relative to one another. The person who collected the data is Ronald Fisher, a man known as the father of statistics, as he came up with methods of analysing small samples of data to produce principles that were ground-breaking in statistics.

The summary of the data is found below:

	    sepal_length	    sepal_width	        petal_length	    petal_width
count	150.0		        150.0	        	150.0	           	150.0

mean	    5.843333333333334	3.0540000000000003	3.758666666666666	1.1986666666666668

std	    0.8280661279778629	0.4335943113621737	1.7644204199522617	0.7631607417008414

min	    4.3		            2.0		            1.0		            0.1

25%     	5.1		        2.8		            1.6		            0.3

50%	    5.8		            3.0		            4.35		    1.3

75%	    6.4		            3.3		            5.1		            1.8

max	    7.9		            4.4		            6.9		            2.5

This was compiled using the code found in lines 2 -7 of analysis.py

Notes / References
Note 1 - https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/ was used to pull the data set frrom the UCI repository into Python. This was my problem with the project yesterday, no matter how much I tried, pandas would not work. I got it going eventually! I was trying to import it from the website URL originally, which didn't work, so I just downloaded the data from the link

