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
 
# Exploratory Data Analysis
A typical average home in Ames Iowa 
![](https://git.generalassemb.ly/mzavar/project_2/blob/master/images/avg_iowa_home.png)
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
A set of new features were created  like  total_sq_ft, number of porches, age of the home  to  evaluate if they could impact the home price

# Transformation
 The sale price distribution was found to  be right skewed. A logarithmic trasnformation was applied for it to be more normally distributed so that was more suitable for the model.


#  Model building and Evaluation
Linear regression was used as a choice of machine learning model using the  following set of features that were identified as secret sauce to get optimal performance  from the model
<TODO>
 
 The model was evaluated for two diffrent loss function RMSE  and R2 score.
 Based on the results  the model could predict the home price with in +/-23158$ of the actual value. The model could absorb
 80% of the time variabiiity in the data . Based on the resulys we fine the model itself was robust in terms of accuracy and generalising the results for unseen data. The model is using 30 features and can be improved upon to include additional features up  to 45 without sacrificing the
generalization. Additionally some of the numerical features that went in to model exhibited right skewed distribution and
can be transformed to normal distribution  for the model to better interpret them. Advanced models like polynomial linear
regression and other can be tried  to further improve accuracy.

# Conclusion
At high level  the results from the model are  promising given that  it can predict the  price of the house in ball park of
23000$ , this might be good  model intially for larger homes.This may not be ready of prime time and to be rolled out.
But we work with appraisers and improve the model with their input and more advanced statistical techniques, this should bring us closer to our goal of faster , consistent, transperant appriasal process for our stakeholders. 
