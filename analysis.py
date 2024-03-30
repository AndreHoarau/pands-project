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


# Histogram 
# I am going to plot Histograms of all the species sepal petal lengths and widths on one diagram in a 2x2 pattern.
# We can determine the size of our combined figure
plt.figure(figsize=(12,10))
# We use plt hist to look at our data frames petal length. 
# As there are 150 entries of which the square root is about 12 so 12 bins is apropriate (SOURCETHIS)
# We use an aplha of 0.5 to add some transparancy to the bars and we use an internal color of red with an edge color of black to allow it to stand out.
# We label this all species so we can differentiate between the different histograms as we build on this.
# We want this to be the top left subplot
plt.subplot(221)
plt.hist(df["petal_length"], bins =12, alpha = 0.5, color= "red", edgecolor= "black", label= "All Species Petal Length")
# Labels the x axis
plt.xlabel("Petal Length (cm) ")
# Labels the y axis
plt.ylabel("Frequency of Petal Length")
# Gives histogram a title.
plt.title("Frequency of Petal Lengths Across All Species")




# We wil repeat for all variables across all the species.
# Petal width
# We want this to be the top right subplot
plt.subplot(222)
plt.hist(df["petal_width"], bins =12, alpha = 0.5, color= "red", edgecolor= "black", label= "All Species Petal Width")
plt.xlabel("Petal Width (cm) ")
plt.ylabel("Frequency of Petal Width")
plt.title("Frequency of Petal Widths Across All Species")

# Sepal Length
# We want this to be the bottom left subplot
plt.subplot(223)
plt.hist(df["sepal_length"], bins =12, alpha = 0.5, color= "red", edgecolor= "black", label= "All Species Sepal Length")
plt.xlabel("Sepal Length (cm) ")
plt.ylabel("Frequency of Sepal Length")
plt.title("Frequency of Sepal Length Across All Species")

# Sepal Width
# We want this to be the bottom right subplot
plt.subplot(224)
plt.hist(df["sepal_width"], bins =12, alpha = 0.5, color= "red", edgecolor= "black", label= "All Species Sepal Width")
plt.xlabel("Sepal Width (cm) ")
plt.ylabel("Frequency of Sepal Width")
plt.title("Frequency of Sepal Widths Across All Species")


# We want to ensure that we do not have overlapping so will use
plt.tight_layout

plt.show()
print("Sanity")