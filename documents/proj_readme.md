# Goal

The goal of this project was to build a machine learning model that will predict a home price for the Ames Iowa region.
The model was built for ML Appriasers internal use , one of the large Apprisal mangement company help to innovate
appraisal space goal of making apprisals consistent, transperant and faster.

This model can be used by appraising officers to generate appriasals, and provide feedback on any improvements areas 
to be incorporated in the model.

# Data Introduction :
We started with around 2050 homes in Ames Iowa that were sold in the year -2006 to 2010 . There are over 79 attributes
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
The features were nu

# Features

# Building Model

#Accuracy :


