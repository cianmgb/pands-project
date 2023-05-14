#first of all we need to import the tools that we will need - pandas, sklearn and matplotlib
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets

#Load Iris Data set from Sklearn
iris = datasets.load_iris()
data = pd.DataFrame(data= iris.data, columns= iris.feature_names)
data['target'] = iris.target

#Save the data to a CSV file
data.to_csv('iris.csv', index=False)

# Load the iris dataset from the CSV file
data = pd.read_csv('iris.csv')

# Get summary statistics
summary = data.describe(include='all')

# Write the summary statistics to a text file
with open('summary.txt', 'w') as f:
    f.write(summary.to_string())

# Create and save histograms for each variable
for column in data.columns:
    if column != 'target':
        data[column].plot(kind='hist', edgecolor='k', title=f'Histogram of {column}')
        plt.savefig(f'{column}_histogram.png')
        plt.clf()
# Convert 'target' to numerical categories for coloring
data['target_cat'] = data['target'].astype('category').cat.codes

# Extract the columns for the scatter plot
sepal_length = data['sepal length (cm)']
sepal_width = data['sepal width (cm)']
petal_length = data['petal length (cm)']
petal_width = data['petal width (cm)']
target = data['target']

# Create a scatter plot
plt.scatter(sepal_length, sepal_width, c=target)

# Add labels and a title
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.title('Scatter Plot of Iris Sepal Data')

# Show the plot
plt.show()