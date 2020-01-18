# Goal

The goal of this project was to build a machine learning model that will predict a home price for the Ames Iowa region.
The model was built for **ML Appriasers** for internal use only, one of the large Apprisal mangement company help to innovate
appraisal space goal of making apprisals consistent, transperant and faster.

This model can be used by appraising officers to generate appriasals, and provide feedback on any improvements areas 
to be incorporated in the model.

# Data Introduction :
We started with around 2050 homes in Ames Iowa from 23 neighborhoods that were sold in the year -2006 to 2010 . There are over 79 attributes
of homes describing size , location ,no of kitchen,bed ,baths, style of the house, additional feature about basment ,garage,
porch,deck so on and so forth.It also included information around when the home was built, remodeled and last sold year.
The data also included quality ratings for various aspects of the home.
See complete list and  description of these features are listed [here](http://jse.amstat.org/v19n3/decock/DataDocumentation.txt)

# Data Cleaning
Most of the  data was quite clean . There was some non-impacting data was cleaned to fill is missing attributes of
pool , garage, basement for the houses where these features were not present.
A cleaning step worth mentioning is the 'lot frontage' the wide area missing  in from of the house, was imputed using the
average value of similar houses ( with in 5% lot area).
The cleaning steps were performed on test data as well if the feature was included in the model.
The steps for cleaning can be found [here](https://git.generalassemb.ly/mzavar/project_2/blob/master/code/01%20-%20Cleaning.ipynb)
 
# EDA
![A typical average home in Ames Iowa](https://git.generalassemb.ly/mzavar/project_2/blob/master/images/avg_iowa_home.png)
https://git.generalassemb.ly/mzavar/project_2/blob/master/images/avg_iowa_home.png
** Column Encoding **
In order for model to take advantage of all non-numerical columns, the features were analysed to separate the numerical from categorical features. The categorical features were further analysed to determine which features has ordinal nature and converted to a numerical represention.
for example
Garage Quality { Ex, Gd, Avg,poor}  was translated to  {3,2,1,0)  do that the model can include these features if they placed
role in the incresed or decresed price of the house.

The second set of categorical variables like  neighborhood, lot configureation etc were  looked at individual level to
determine if they had impact on sale price and converted to multiple numerical columns - one for each category.

** Outliers **
  There were few homes less than 1% that were missing utilities are were removed.
  
# Features
    


# Building Model

#Accuracy :


