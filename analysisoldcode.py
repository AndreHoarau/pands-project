# Where I keep my old code that I have improved upon
# Note cannot have this here when time to submit final project will move somewhere else 
# Author Andre Hoarau
# Before using for loops to loop through the variables for the histograms.
'''# We use plt hist to look at our data frames petal length. 
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

plt.show()'''