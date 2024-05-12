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

# Import the norm module to the statistical distribution we will use.
from scipy.stats import norm

# Import seaborn, a matplotlib library.

import seaborn as sns

# Next we can load the data and refer to it as the data frame df.
df= pd.read_csv("iris_data.csv")

# Describe will look at the data set and return the count of each variable
# Their mean, standard deviation, minimum, 25 , 50 and 75th percentiles and their max.
print(df.describe())
# This describes the data set across all 3 species but let's look at each individual species.
grouped_by_species = df.groupby('species')
summary_stats_by_species = grouped_by_species.describe()
print(summary_stats_by_species)
# From this one can see where perhaps there are difference between species in terms of which have longer sepals which have longer petals and so on.
# Andre to do further analysis of above
with open('Statistic_Summary.txt', 'w')as file:
    file.write(f"{df.describe()},{summary_stats_by_species}")


# Histogram 
# I am going to plot Histograms of all the species sepal petal lengths and widths on one diagram in a 2x2 pattern.
# I want to define the variables and the labels I will use
variables = ["petal_length", "petal_width", "sepal_length", "sepal_width"]
labels = ["Petal Length", "Petal Width", "SepalLength", "Sepal Width"]
# I want each species to be represented by a different color so make a dict with key value pairs
colors= {'setosa' : 'red', 'versicolor': 'green', 'virginica': 'blue'}

# We can determine the size of our combined figure 12 x 10 inches
plt.figure(figsize=(12,10))

# We are going to use a for loop for each variable to detemine the subplots
# This functions will iterate of the variables and add a counter to i so i is the index of the variable in the list
for i, variable in enumerate(variables):
# We create are 2 x 2 plot and as i starts at 0 we need to add one for the first subplot and so on.  
    plt.subplot(2,2, i + 1)
    # This for loop goes over each species in the colors dict above
    for species, color in colors.items():
# This filters the data frame to include only rows where the species column matches the current speices
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
plt.show()

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
# Reference: Inspiration for an analysis available at: https://www.kaggle.com/code/rakesh6184/seaborn-plot-to-visualize-iris-data
# Reference: How to use the seaborn heatmap: https://www.datacamp.com/tutorial/seaborn-heatmaps
# We iterate over each species in our grouped by species vairable and access the species name and the corresponding data frame. 
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


print("Sanity")