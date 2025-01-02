"""
Question 1: Name any five plots that we can plot using the Seaborn library. Also, state the uses of each plot.
Line Plot:

Use: To display trends over time or continuous data.
Example: Time series data like stock prices, temperature over time.
Bar Plot:

Use: To compare categorical data with a numerical value.
Example: Average sales per product category.
Box Plot:

Use: To display the distribution of data and detect outliers.
Example: Age distribution in a population.
Heatmap:

Use: To visualize matrix-like data or correlations.
Example: Correlation between variables in a dataset.
Pair Plot:

Use: To explore relationships between all pairs of numerical variables.
Example: Relationships between features in the Iris dataset.
"""
# Question 2: Load the "fmri" dataset and plot a line plot.
import seaborn as sns
import matplotlib.pyplot as plt
fmri = sns.load_dataset("fmri")
sns.lineplot(data=fmri, x="timepoint", y="signal", hue="event", style="region")
plt.title("FMRI Signal Over Time")
plt.show()

# Question 3: Load the "titanic" dataset and plot two box plots.
titanic = sns.load_dataset("titanic")
plt.figure(figsize=(12, 6))
sns.boxplot(data=titanic, x="pclass", y="age")
plt.title("Box Plot of Age by Passenger Class")
plt.show()
sns.boxplot(data=titanic, x="pclass", y="fare")
plt.title("Box Plot of Fare by Passenger Class")
plt.show()

# Question 4: Plot a histogram for the "price" column in the "diamonds" dataset.
diamonds = sns.load_dataset("diamonds")
sns.histplot(data=diamonds, x="price", hue="cut", kde=True)
plt.title("Price Distribution by Diamond Cut")
plt.show()

# Question 5: Plot a pair plot for the "iris" dataset.
iris = sns.load_dataset("iris")
sns.pairplot(data=iris, hue="species")
plt.suptitle("Pair Plot of Iris Dataset", y=1.02)
plt.show()

# Question 6: Plot a heatmap for the "flights" dataset.
flights = sns.load_dataset("flights")
pivot_table = flights.pivot(index="month", columns="year", values="passengers")
plt.figure(figsize=(10, 8))
sns.heatmap(pivot_table, annot=True, fmt="d", cmap="coolwarm")
plt.title("Heatmap of Flight Passengers")
plt.show()

