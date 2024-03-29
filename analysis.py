# This is the programming and scripting project.
# I will perform an analysis on the Iris data set (Iris.data)
# I will summarise the variables, generate plots and perform further analysis.
# Author Andre Hoarau

# Let's import the pandas module in order to outline our data frame and summarise it.
import pandas as pd

# Next we can load the data and refer to it as the data frame df.
df= pd.read_csv("iris_data.csv")

# Describe will look at the data set and return the count of each variable
# Their mean, standard deviation, minimum, 25 , 50 and 75th percentiles and their max.
print(df.describe())
print("Sanity")