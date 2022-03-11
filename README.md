## car price predictor 

ML model for car selling price prediction and analysis.
This kind of system becomes handy for many people.


>>project idea: Imagine a situation where you have an old car and want to sell it.
You may of course approach an agent for this and find the market price,
but later may have to pay pocket money for his service in selling your car.
But what if you can know your car selling price without the intervention of an agent. 
Or if you are an agent, definitely this will make your work easier. 
Yes, this system has already learned about previous selling prices over years of various cars.

>>Importing Dataset
quickr_car.csv file taken as a 
dataset from kaggle


>> importing important libraries 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib as mpl 
%matplotlib inline
mpl.style.use('ggplot')
import seaborn as sns  

>> defining the libraries

1.  for pre-processing numpy and pandas used for 
    reading and writing the file in numpy array 
2.  seaborn and ggplot used for data visualization

3. %matplotlib inline sets the backend of matplotlib to the 'inline' backend: 
   With this backend, the output of plotting commands is displayed
   inline within frontends like the Jupyter notebook

>>columns in dataset (892rows X 6cols) 
1.name	
2.company	
3.year	
4.Price	
5.kms_driven	
6.fuel_type



>>Data Inspection

In this section, we will explore the data. 
First Let’s see what columns we have in the data
 and their data types along with missing values information.

>>Data Preparation
Here we will clean the data for cleaning used normalization 
and prepare it for training the model.


>>Training the model
train and test split 
I have used the linear regression to predict the selling prices

>>Handling ‘Outliers’
This we will examine across numerical features
used a boxplot 

>>Handling Categorical features
i have used One hot encoding : is a process of converting categorical data variables 
so they can be provided to machine learning algorithms to improve predictions. 
One hot encoding is a crucial part of feature engineering for machine learning.


>>What is a pipeline?
 
Pipeline are a sequence of data processing mechanisms.
Pandas pipeline feature allows us to string together 
various user-defined Python functions in order to build a pipeline of data processing





