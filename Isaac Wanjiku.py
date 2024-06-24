import pandas as pd
import requests
import seaborn as sns
import matplot.pyplot as plt

#load data from computer

dkut = 'file_name.txt'  # Define dkut as the filename
with open(dkut, 'r') as file:
    data = file.read()
    print(data)

#load data from Github



def get_github_user_data(username):
    url = f": https://api.github.com/users/Isaacwanjiku"
    response = requests.get(url)

#load data from website

url = https//archive.ics.uci.edu/dataset/53/iris
response = requests.get(url)
# fetch dataset 
iris = fetch_ucirepo(id=53)

#Show the first 8 records
# import dataset
heart_disease = fetch_ucirepo(id=45)

print('First 8 data points in the Iris dataset')
print(data.head(8))

#Number of records (rows)
num_records = len(data)
print("Number of records:", num_records)

# Number of features (columns)
num_features = len(data.columns)

print("Number of features:", num_features)

# Load the dataset
data = pd.read_csv(url, header=None)

# Display data types of each column
print("Data types of each column:")
print(data.dtypes)


# Check for missing data
missing_data = data.isnull().sum()

print("Missing data in the Iris dataset:")
print(missing_data)


# Case 1: Relationship between sepal length and sepal width
sns.scatterplot(x='sepal_length', y='sepal_width', data=data, hue='class')
plt.title('Relationship between Sepal Length and Sepal Width')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.show()

# Case 2: Relationship between sepal length and petal length
sns.scatterplot(x='sepal_length', y='petal_length', data=data, hue='class')
plt.title('Relationship between Sepal Length and Petal Length')
plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')
plt.show()

# Case 3: Relationship between petal width and petal length
sns.scatterplot(x='petal_width', y='petal_length', data=data, hue='class')
plt.title('Relationship between Petal Width and Petal Length')
plt.xlabel('Petal Width')
plt.ylabel('Petal Length')
plt.show()

#In this code:

#We load the Iris dataset and define column names since the original dataset doesn't have column names.
#We then create scatter plots to visualize the relationships between different pairs of features.
#Case 1: Sepal length vs. Sepal width
#Case 2: Sepal length vs. Petal length
#Case 3: Petal width vs. Petal length
