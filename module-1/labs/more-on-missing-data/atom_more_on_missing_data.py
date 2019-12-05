# %% markdown
# # More on Missing Data - Lab
#
# ## Introduction
#
# In this lab, you'll continue to practice techniques for dealing with missing data. Moreover, you'll observe the impact on distributions of your data produced by various techniques for dealing with missing data.
#
# ## Objectives
#
# In this lab you will:
#
# - Evaluate and execute the best strategy for dealing with missing, duplicate, and erroneous values for a given dataset
# - Determine how the distribution of data is affected by imputing values
# %% markdown
# ## Load the data
#
# To start, load the dataset `'titanic.csv'` using pandas.
# %% codecell
import pandas as pd
df = pd.read_csv('titanic.csv')
# %% markdown
# Use the `.info()` method to quickly preview which features have missing data
# %% codecell
df.info()
df.head()
# %% markdown
# ## Observe previous measures of centrality
#
# Let's look at the `'Age'` feature. Calculate the mean, median, and standard deviation of this feature. Then plot a histogram of the distribution.
# %% codecell
df['Age']
# %% codecell
df['Age'].describe()
# %% codecell
df.Age.agg(['mean', 'median', 'std', 'min'])
# %% codecell
df['Age'] == 29
# %% codecell
df.loc[df['Age'] == 29] #awesome way to do it

df[df['Age'] == 29] #twice as slow
# %% codecell
df['Age']
# %% codecell
import matplotlib.pyplot as plt
%matplotlib inline

df.Age.hist(bins = 16)
# %% codecell
import matplotlib.pyplot as plt
%matplotlib inline

plt.hist(df.Age, bins = 16)
# %% markdown
# ## Impute missing values using the mean
#
# Fill the missing `'Age'` values using the average age. (Don't overwrite the original data, as we will be comparing to other methods for dealing with the missing values.) Then recalculate the mean, median, and std and replot the histogram.
# %% codecell
pd.set_option('display.max_rows', 200)
# %% codecell
# Your code here
filled_in_ages = df.Age.fillna(df.Age.mean())
# %% codecell
plt.hist(filled_in_ages, bins = 16)
# %% markdown
# ### Commentary
#
# Note that the standard deviation dropped, the median was slightly raised and the distribution has a larger mass near the center.
# %% markdown
# ## Impute missing values using the median
#
# Fill the missing `'Age'` values, this time using the media age. (Again, don't overwrite the original data, as we will be comparing to other methods for dealing with the missing values.) Then recalculate the mean, median, and std and replot the histogram.
# %% codecell
# Your code here
med_filled_in_ages = df.Age.fillna(df.Age.median())
# %% codecell
series = med_filled_in_ages.agg(['mean', 'median', 'std'])

series.head()
# %% markdown
# ### Commentary
#
# Imputing the median has similar effectiveness to imputing the mean. The variance is reduced, while the mean is slightly lowered. You can once again see that there is a larger mass of data near the center of the distribution.
# %% markdown
# ## Dropping rows
#
# Finally, let's observe the impact on the distribution if we were to simply drop all of the rows that are missing an age value. Then, calculate the mean, median and standard deviation of the ages along with a histogram, as before.
# %% codecell
df.Age.dropna()
df.Age.agg(['mean', 'median', 'std'])

# %% markdown
# ### Commentary
#
# Dropping missing values leaves the distribution and associated measures of centrality unchanged, but at the cost of throwing away data.
#
# ## Summary
#
# In this lab, you briefly practiced some common techniques for dealing with missing data. Moreover, you observed the impact that these methods had on the distribution of the feature itself. When you begin to tune models on your data, these considerations will be an essential process of developing robust and accurate models.
