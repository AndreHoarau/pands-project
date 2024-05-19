# This is the programming and scripting project.
# I will perform an analysis on the Iris data set (Iris.data)
# I will summarise the variables, generate plots and perform further analysis.
# Author Andre Hoarau

# Let's import the pandas module in order to outline our data frame and summarise it.
import pandas as pd

# We will need matplotlib pyplot to generate our plots 
import matplotlib.pyplot as plt

# We will use Numpy for numerical operations
import numpy as np

# Import seaborn, a matplotlib library.
import seaborn as sns

# Next we can load the data and refer to it as the data frame df.
df= pd.read_csv("iris_data.csv")

# Describe will look at the data set and return the count of each variable
# Their mean, standard deviation, minimum, 25 , 50 and 75th percentiles and their max.
description = df.describe()
# This describes the data set across all 3 species but let's look at each individual species.
grouped_by_species = df.groupby('species')
summary_stats_by_species = grouped_by_species.describe()

# Write the full DataFrame descriptions to the file
# We are formatting out txt file and ensuring that all the data is easy to read in a string.
with open('Statistic_Summary.txt', 'w') as file:
    file.write("Full Data Description:\n")
    file.write(description.to_string())
    file.write("\n\n")
    file.write("Summary Statistics by Species:\n")
    file.write(summary_stats_by_species.to_string())


# Histogram 
# I am going to plot Histograms of all the species sepal petal lengths and widths on one diagram in a 2x2 pattern.
# I want to define the variables and the labels I will use.
variables = ["petal_length", "petal_width", "sepal_length", "sepal_width"]
labels = ["Petal Length", "Petal Width", "Sepal Length", "Sepal Width"]
# I want each species to be represented by a different color so make a dict with key value pairs
colors= {'setosa' : 'red', 'versicolor': 'green', 'virginica': 'blue'}

# We can determine the size of our combined figure 12 x 10 inches
plt.figure(figsize=(12,10))

# We are going to use a for loop for each variable to determine the subplots
# This functions will iterate of the variables and add a counter to i so i is the index of the variable in the list
for i, variable in enumerate(variables):
# We create are 2 x 2 plot and as i starts at 0 we need to add one for the first subplot and so on.  
    plt.subplot(2,2, i + 1)
    # This for loop goes over each species in the colors dict above
    for species, color in colors.items():
# This filters the data frame to include only rows where the species column matches the current species
        species_data = df[df['species']== species]
# The histogram is plotted for the current variable in the current species.
# As we have 150 data points and sqrt is approx 12 we have 12 bins.
# Alpha transparency measure makes it easier to see overlapping
# We are assigning the colors as per species 
# Edge color black helps it to stand out.
# Label the histogram bars with the species
        plt.hist(species_data[variable], bins= 12, alpha = 0.5, color = color, edgecolor= 'black', label=species)
# Set the x axis label using the label based on the current variable index
# Sets the y axis to Frequency
# Sets a title to each histogram based on the variable.
    plt.xlabel(f'{labels[i]} (cm)')
    plt.ylabel("Frequency")
    plt.title(f'Frequency of {labels[i]} Across Species')
# Adds legends to subplots
    plt.legend()
# Prevents overlapping
plt.tight_layout()
plt.savefig("Histograms.png")

# Scatter plot of each pair of variables.
# Similar to the above we will plot across the 4 variables separated by species to start clustering the species into unique variable trends.
# First need to create a list  of the variables we want but we do not need to analyse the same variables against each other.
pairs= [('petal_length','petal_width'),('petal_length','sepal_length'), ('petal_length','sepal_width'), ('sepal_length','sepal_width'), ('sepal_length','petal_width'), ('sepal_width','petal_width')  ]
# This evaluates every possible permutation of unique variable types anaylsed against each other.
# We want this all on one plot.
plt.figure(figsize=(11, 16))
# We want to loop over each pair of variables.
for i, pair in enumerate(pairs, start=1):
    plt.subplot(3,2,i)
# We want to loop over each speices
    for species, color in colors.items():
# This will get the data associated with each species
        species_data = df[df['species'] == species]
# Create the scatter plot for the data pairs.
        plt.scatter(species_data[pair[0]], species_data[pair[1]], color=color, label=species)
 # Add labels and title
 # Add labels and title
    plt.xlabel(pair[0])
    plt.ylabel(pair[1])
    plt.title(f'Scatter Plot of {pair[0]} vs {pair[1]}')
    plt.legend()
    # Show the plot
    
plt.subplots_adjust(hspace=0.5)
plt.tight_layout    
plt.show()


# Seaborn Heat Map
# We iterate over each species in our grouped by species variable and access the species name and the corresponding data frame. 
for species, group_df in grouped_by_species:
# We need to modify the matrix to remove the species strings by only including numbers. 
    only_number_matrix = group_df.select_dtypes(include="number")
# We then get the correlation of these variables in each item.
    correlation_matrix= only_number_matrix.corr()
# We then adjsut the size of our figure.
    plt.figure(figsize=(8, 6))
# Create the heatmap, label the squares and pick a colour palette. 
    sns.heatmap(correlation_matrix, annot=True, cmap="viridis")
# Add the titles
    plt.title(f'Correlation Heatmap for {species}')
    plt.show()

# Machine learning to predict flower Species

# Train_test_split enables us to split our data into training and testing sets.
from sklearn.model_selection import train_test_split
# RandomForestClassifier is the machine learning model for testing the sets.
from sklearn.ensemble import RandomForestClassifier
# StandardScaler normalises the feature data
from sklearn.preprocessing import StandardScaler

# We then are going to take the features and the target from our data frame and extract them.
# We use double [[]] here to extract the variables from our data frame as a data frame.
X = df[['sepal_length','sepal_width','petal_length','petal_width']]
# We use single brackets here a one dimensional array also known as a series.
y = df['species']
# We are now going to split the dataset into training and testing sets.
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)
# We are doing a 20% testing size and therefore a 80% training split. This is a common choice.
# We are also seeding our training and testing split using the random state set to a random number in this case 42.
# We are then going to scale the features
scaler= StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Scaling normalises the features so they have a mean of 0 and a standard deviation of 1.
# fit_transform computes the mean and std and then scales the data.
# transform scales the test set using the mean and std from the training set.


# Ensure X_train and X_test are Pandas DataFrames with appropriate column names
# This is to try and prevent the warning that is occuring.
assert isinstance(X_train, pd.DataFrame), "X_train is not a Pandas DataFrame"
assert isinstance(X_test, pd.DataFrame), "X_test is not a Pandas DataFrame"
assert set(X_train.columns.tolist()) == set(X_test.columns.tolist()), "Column names of X_train and X_test do not match"

# Ensure consistency in feature names
assert set(X_train.columns.tolist()) == set(scaler.get_feature_names_out()), "Feature names are not consistent"

# Train the Random Forest classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
# This will initialise the Random Forrest Classifier with 100 trees
clf.fit(X_train_scaled, y_train)
# This then fits the classifier to the scaled training data.

# Get the inputs
# We are then going to ask the use to input the lengths and change them to floats
sepal_length = float(input("Enter sepal length (cm): "))
sepal_width = float(input("Enter sepal width (cm): "))
petal_length = float(input("Enter petal length (cm): "))
petal_width = float(input("Enter petal width (cm): "))


# Prepare the input data for prediction with column names
input_data = pd.DataFrame([[sepal_length, sepal_width, petal_length, petal_width]], 
columns=['sepal_length','sepal_width','petal_length','petal_width'])



# Make the prediction
# This takes the input values creates a numpy array
input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
# This then scales the input data using the previous scaler.
input_data_scaled = scaler.transform(input_data)
# This predicts the probability of each class using the trained classifier.
predicted_probabilities = clf.predict_proba(input_data_scaled)

# Output of the probabilities
print("Predicted probabilities:")
# List the species names
species_names = ['setosa', 'versicolor', 'virginica']
# This loops through the predicted probabilities for the input sample.
for i, prob in enumerate(predicted_probabilities[0]):
# This then prints species and the probability as a percentage to 2 decimal places.
    print(f"{species_names[i]}: {prob*100:.2f}%")
