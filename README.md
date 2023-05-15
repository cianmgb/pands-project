# pands-project
## My interpretation / summary of Fishers Iris Data Set:

Fisher’s Data set is a widely used multivariate data set in the field of machine learning and statistics. It is a dataset that contains four measurements of fifty different sepals and petals of three different Iris species: Iris setosa, Iris virginica, and Iris versicolor. The measurements are as follows:
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

## Libraries used

For this project I imported Pandas, matplotlib.pyplot, and sklearn.

I found a github submission that dealt with the Iris Data set that helped guide my work - https://github.com/RitRa/Project2018-iris/tree/master However this was far more detailed than what was required for this project so it was just used as an interesting source to see what methods could be used to get the results needed.

I originally pulled the data from the UCI repository, however as this had no headings and was causing problems when trying to analyse it (histograms were incorrect, labels didn't match) I researched a different way of doing it, which was to pull it in from SKlearn (found this site useful https://medium.com/analytics-vidhya/exploration-of-iris-dataset-using-scikit-learn-part-1-8ac5604937f8)

## Methodology

I then had to write the data to a csv file, which I did using a graph generated from https://stackoverflow.com/questions/16923281/writing-a-pandas-dataframe-to-csv-file

Next, I had to get summary statistics and write to text file - I found the data.describe function here: https://www.geeksforgeeks.org/python-pandas-dataframe-describe-method/ https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html#:~:text=If%20include%3D%27all%27%20is,Describing%20a%20numeric%20Series%20 https://www.freecodecamp.org/news/with-open-in-python-with-statement-syntax-example/ 

This pulled the data in, and then I wrote summary with f.write https://towardsdatascience.com/4-tips-to-master-python-f-strings-a70ca896faa4#:~:text=To%20write%20an%20f%2Dstring,into%20curly%20braces%20%E2%80%9C%7B%7D%E2%80%9D.

When this was done I had to plot the histogram using pandas https://www.machinelearningplus.com/pandas/pandas-histogram/

https://www.w3schools.com/python/pandas/pandas_plotting.asp was the resource I referenced to use the plot function using 'hist'..

To pull the data into VScode I found the following link to be helpful: https://www.listendata.com/2017/02/import-data-in-python.html , this described the import pandas as pd function.

## Summary of Data

The summary of the data is found below:

       sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)      target
count         150.000000        150.000000         150.000000        150.000000  150.000000
mean            5.843333          3.057333           3.758000          1.199333    1.000000
std             0.828066          0.435866           1.765298          0.762238    0.819232
min             4.300000          2.000000           1.000000          0.100000    0.000000
25%             5.100000          2.800000           1.600000          0.300000    0.000000
50%             5.800000          3.000000           4.350000          1.300000    1.000000
75%             6.400000          3.300000           5.100000          1.800000    2.000000
max             7.900000          4.400000           6.900000          2.500000    2.000000


## References


Bhalla, D. (no date) How to import data in python, ListenData. Available at: https://www.listendata.com/2017/02/import-data-in-python.html (Accessed: 12 May 2023).

Chris, K. (2022) With open in python – with statement syntax example, freeCodeCamp.org. Available at: https://www.freecodecamp.org/news/with-open-in-python-with-statement-syntax-example/ (Accessed: 11 May 2023)

C, A. (no date) About Fisher’s Iris dataset. Available at: https://www.angela1c.com/projects/iris_project/the-iris-dataset/  (Accessed: 11 May 2023).

Cui, Y. (2020) The iris dataset - A little bit of history and biology, Medium. Available at: https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5 (Accessed: 15 May 2023).

MachineLearningPlus (2022) Pandas histogram, Machine Learning Plus. Available at: https://www.machinelearningplus.com/pandas/pandas-histogram/ (Accessed: 12 May 2023)

Pandas dataframe describe() method (2023) GeeksforGeeks. Available at: https://www.geeksforgeeks.org/python-pandas-dataframe-describe-method/ (Accessed: 11 May 2023)

Pandas – plotting (no date). Available at: https://www.w3schools.com/python/pandas/pandas_plotting.asp (Accessed: 13 May 2023).

Pandas.dataframe.describe# (no date) pandas.DataFrame.describe - pandas 2.0.1 documentation. Available at: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html#:~:text=If%20include%3D%27all%27%20is,Describing%20a%20numeric%20Series%20  (Accessed: 12 May 2023).

Piepenbreier, N. (2021) 4 tips to master python F-strings!, Medium. Available at: https://towardsdatascience.com/4-tips-to-master-python-f-strings-a70ca896faa4  (Accessed: 12 May 2023).

Stack Overflow (No date) Writing a pandas DataFrame to CSV file, Stack Overflow. Available at: https://stackoverflow.com/questions/16923281/writing-a-pandas-dataframe-to-csv-file (Accessed: 11 May 2023).

