# This is the programming and scripting project.
# I will perform an analysis on the Iris data set (Iris.data)
# I will summarise the variables, generate plots and perform further analysis.
# Author Andre Hoarau

# Let's import the pandas module in order to outline our data frame and summarise it.
import pandas as pd

# We will need matplotlib pyplot to generate our plots 
import matplotlib.pyplot as plt
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
plt.hist("sepal_length", "sepal_width", "petal_length", "petal_width")
plt.show()

print("Sanity")