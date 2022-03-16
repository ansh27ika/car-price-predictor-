## CAR PRICE PREDICTOR
##### REGRESSION MODEL

ML model for car selling price prediction and analysis.
This kind of system becomes handy for many people.

## PROJECT OVERVIEW
Imagine a situation where you have an old car and want to sell it.
You may of course approach an agent for this and find the market price,
but later may have to pay pocket money for his service in selling your car.
But what if you can know your car selling price without the intervention of an agent. 
Or if you are an agent, definitely this will make your work easier. 
Yes, this system has already learned about previous selling prices over years of various cars.

#### Importing Dataset
quickr_car.csv file taken as a 
dataset from kaggle


### Importing  libraries 
1. `numpy` 
2.  `pandas` 
3.  `matplotlib` 
4. `%matplotlib inline`
5. `ggplot`
6.  `seaborn` 
7.  `pickle`



### Columns in dataset (892rows X 6cols) 
1. Name	
2. Company	
3. Year	
4. Price	
5. kms_driven	
6. Fuel_type



### Data Inspection

In this section, we will explore the data. 
First Let’s see what columns we have in the data
and their data types along with missing values information.

###  Data Preparation
Here we will clean the data for cleaning used normalization 
and prepare it for training the model.


### Training the model
train and test split 
I have used the linear regression to predict the selling prices

### Handling ‘Outliers’
This we will examine across numerical features
used a boxplot 

### Handling Categorical features
i have used One hot encoding : is a process of converting categorical data variables 
so they can be provided to machine learning algorithms to improve predictions. 
One hot encoding is a crucial part of feature engineering for machine learning.


### Pipeline
 
Pipeline are a sequence of data processing mechanisms.
Pandas pipeline feature allows us to string together 
various user-defined Python functions in order to build a pipeline of data processing

### DEPLOYMENT 
used python flask 
postmamn is added to show end to end points 
this is my body style
{"name":"Audi A4 1.8","company": "Audi", "year": 2010, "kms_driven": 12000, "fuel_type": "Petrol"}
prediction style
{
    "prediction": [
        738551.2095113248
    ]
}



