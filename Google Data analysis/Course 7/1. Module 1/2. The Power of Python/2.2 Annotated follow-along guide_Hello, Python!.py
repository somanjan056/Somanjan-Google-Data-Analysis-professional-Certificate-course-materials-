#!/usr/bin/env python
# coding: utf-8

# # Annotated follow-along guide: Hello, Python!
# 
# This notebook contains the code used in the instructional videos from [Module 1: Hello, Python!](https://www.coursera.org/learn/copy-of-get-started-with-python/home/module/1).
# 

# ## Introduction
# 
# This follow-along guide is an annotated Jupyter Notebook organized to match the content from each module. It contains the same code shown in the videos for the module. In addition to content that is identical to what is covered in the videos, you’ll find additional information throughout the guide to explain the purpose of each concept covered, why the code is written in a certain way, and tips for running the code.
# 
# As you watch each of the following videos, an in-video message will appear to advise you that the video you are viewing contains coding instruction and examples. The in-video message will direct you to the relevant section in the notebook for the specific video you are viewing. Follow along in the notebook as the instructor discusses the code.
# 
# To skip directly to the code for a particular video, use the following links:
# 
# 1.   **[Discover more about Python](#1)**
# 2.   **[Jupyter Notebooks](#2)**
# 3.   **[Object-oriented programming](#3)**
# 4.   **[Variables and data types](#4)**
# 5.   **[Create precise variable names](#5)**
# 6.   **[Data types and conversions](#6)**

# <a name="1"></a>
# ## 1. [Discover more about Python](https://www.coursera.org/learn/get-started-with-python/lecture/JC2zu/discover-more-about-python)
# 

# In[1]:


# Print to the console.
print("Hello, world!")


# In[2]:


# Print to the console.
print(22)


# In[3]:


# Simple arithmetic
(5 + 4) / 3


# In[4]:


# Assign variables.
country = 'Brazil'
age = 30

print(country)
print(age)


# In[5]:


# Evaluations
# Double equals signs are used to check equivalency.
10**3 == 1000


# In[6]:


# Evaluations
# A single equals sign is reserved for assignment statements.
10 ** 3 = 1000


# In[7]:


# Evaluations
# Double equals signs are used to check equivalency.
10 * 3 == 40


# In[8]:


# Evaluations
# Double equals signs are used to check equivalency.
10 * 3 == age


# In[9]:


# Conditional statements
if age >= 18:
    print('adult')
else:
    print('minor')


# In[10]:


# Loops
for number in [1, 2, 3, 4, 5]:
    print(number)


# In[11]:


# Loops
my_list = [3, 6, 9]

for x in my_list:
    print(x / 3)


# In[12]:


# Functions
def is_adult(age):

    if age >= 18:
        print('adult')
    else:
        print('minor')


# In[13]:


# Use the function that was just created.
is_adult(14)


# In[14]:


# Use the built-in sorted() function.
new_list = [20, 25, 10, 5]

sorted(new_list)


# <a name="2"></a>
# ## 2. [Jupyter Notebooks](https://www.coursera.org/learn/get-started-with-python/lecture/2l42i/jupyter-notebooks)

# **NOTE:** The import statements cell must be run before running some of the following cells. This setup step was not shown in the instructional video, but you will learn about import statements later in this course.

# In[37]:


# Import statements.
import warnings
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns


# In[38]:


# Create a list.
my_list = [10, 'gold', 'dollars']


# In[39]:


# Use the helper function to calculate F1 score used in the following graphics.
def f1_score(precision, recall):
    score = 2*precision*recall / (precision + recall)
    score = np.nan_to_num(score)

    return score


# In[40]:


# Generate a graph of F1 score for different precision and recall scores.
x = np.linspace(0, 1, 101)
y = np.linspace(0, 1, 101)
X, Y = np.meshgrid(x, y)
Z = f1_score(X, Y)
fig = plt.figure()
fig.set_size_inches(10, 10)
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=2, cstride=3, cmap='plasma')

ax.set_title('$F_{1}$ of precision, recall', size=18)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.view_init(35, -65)


# **NOTE:** The following cells use markdown (like this cell) to create formatted text like headers and bullets, tables, and mathematical equations. You can select any cell and enter into edit mode to view the markdown text. Then run the cell to view the rendered output.

# ### **Section 2**
# 
# * Part 1:
# * Part 2:

# |Title|Author|Date|
# |:--|:--|:-:|
# |The Art of War|Sun Tzu|5th cent. BCE|
# |Don Quixote de la Mancha|Miguel de Cervantes Saavedra|1605|
# |Pride and Prejudice|Jane Austen|1813|
# 

# $$
#   \int_0^\infty \frac{x^3}{e^x-1}\,dx = \frac{\pi^4}{15}
# $$

# <a name="3"></a>
# ## 3. [Object-oriented programming](https://www.coursera.org/learn/get-started-with-python/lecture/1SJMN/object-oriented-programming) 

# In[41]:


# Assign a string to a variable and check its type.
magic = 'HOCUS POCUS'
print(type(magic))


# In[42]:


# Use the swapcase() string method to convert from caps to lowercase.
magic = 'HOCUS POCUS'
magic = magic.swapcase()
magic


# In[43]:


# Use the replace() string method to replace some letters with other letters.
magic = magic.replace('cus', 'key')
magic


# In[44]:


# Use the split() string method to split the string into two strings.
magic = magic.split()
magic


# In[45]:


# Set up the cell to create the `planets` dataframe.
# (This cell was not shown in the instructional video.)
import pandas as pd
data = [['Mercury', 2440, 0], ['Venus', 6052, 0,], ['Earth', 6371, 1],
        ['Mars', 3390, 2], ['Jupiter', 69911, 80], ['Saturn', 58232, 83],
        ['Uranus', 25362, 27], ['Neptune', 24622, 14]
]

cols = ['Planet', 'radius_km', 'moons']

planets = pd.DataFrame(data, columns=cols)


# In[46]:


# Display the `planets` dataframe.
planets


# In[47]:


# Use the shape dataframe attribute to check the number of rows and columns.
planets.shape


# In[48]:


# Use the columns dataframe attribute to check column names.
planets.columns


# <a name="4"></a>
# ## 4. [Variables and data types](https://www.coursera.org/learn/get-started-with-python/lecture/k3ex2/variables-and-data-types) 

# In[15]:


# Assign a list containing players' ages.
age_list = [34, 25, 23, 19, 29]


# In[16]:


# Find the maximum age and assign to `max_age` variable.
max_age = max(age_list)
max_age


# In[17]:


# Convert `max_age` to a string.
max_age = str(max_age)
max_age


# In[18]:


# Reassign the value of `max_age`.
max_age = 'ninety-nine'
max_age


# In[19]:


# FIRST, RE-RUN THE SECOND CELL IN THIS VIDEO.
# Check the value contained in `max_age` (SHOULD OUTPUT 34).
max_age


# In[20]:


# Find the minimum age and assign to `min_age` variable.
min_age = min(age_list)

# Subtract `min_age` from `max_age`
max_age - min_age


# <a name="5"></a>
# ## 5. [Create precise variable names](https://www.coursera.org/learn/get-started-with-python/lecture/fB03O/create-precise-variable-names) 

# In[55]:


# Trying to assign a value to a reserved keyword will return a syntax error.
else = 'everyone loves some esparagus'


# In[56]:


# The word "asparagus" is misspelled. That's allowed.
esparagus = 'everyone loves some esparagus'


# In[57]:


# Order of operations
2 * (3 + 4)


# In[58]:


# Order of operations
(2 * 3) + 4


# In[59]:


# Order of operations
3 + 4 * 10


# <a name="6"></a>
# ## 6. [Data types and conversions](https://www.coursera.org/learn/get-started-with-python/lecture/z9zda/data-types-and-conversions)

# In[60]:


# Addition of 2 ints
print(7+8)


# In[61]:


# Addition of 2 strings
print("hello " + "world")


# In[62]:


# You cannot add a string to an integer.
print(7+"8")


# In[63]:


# The type() function checks the data type of an object.
type("A")


# In[64]:


# The type() function checks the data type of an object.
type(2)


# In[65]:


# The type() function checks the data type of an object.
type(2.5)


# In[66]:


# Implicit conversion
print(1 + 2.5)


# In[67]:


# Explicit conversion (The str() function converts a number to a string.)
print("2 + 2 = " + str(2 + 2))


# **Congratulations!** You've completed this lab. However, you may not notice a green check mark next to this item on Coursera's platform. Please continue your progress regardless of the check mark. Just click on the "save" icon at the top of this notebook to ensure your work has been logged.
