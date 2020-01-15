
# Import libraries here.
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

class DataCleaner:
    """docstring for ."""


    def __init__(self, df):
        self.m_df =df
        self.m_categorical_features =list(sorted(df.select_dtypes(exclude ="number").columns))
        self.m_numerical_features =list(sorted(df.select_dtypes(include="number").columns))


    def any_missing_data(self,df):
        return df.isnull().sum().sum()

    def missing_non_numerical_columns(self):
       missing_column_list =self.m_df.columns[self.m_df.isnull().any()]
       return list(self.m_df[missing_column_list].select_dtypes(exclude ="number").columns)

    def missing_numerical_columns(self):
       missing_column_list =self.m_df.columns[self.m_df.isnull().any()]
       return list(self.m_df[missing_column_list].select_dtypes(include ="number").columns)

    def Replace_pool_quality_as_na_if_no_pool(self):
        missing_pool_quality = self.m_df['ord_Pool QC'].isnull()
        self.m_df.loc[ (missing_pool_quality & (self.m_df['Pool Area'] ==0)),'ord_Pool QC'] ='N_A'
        return self.m_df

    def Replace_fireplace_quality_as_na_if_no_fireplace(self):
        missing_fireplace_quality =self.m_df['ord_Fireplace Qu'].isnull()
        missing_quality_when_no_fireplace =(missing_fireplace_quality) & (self.m_df['Fireplaces']==0)
        self.m_df.loc[missing_quality_when_no_fireplace,'ord_Fireplace Qu'] ='N_A'
        return self.m_df

    def Replace_garage_attributes_as_na_if_no_garage(self):
        garage_area_zero = self.m_df['Garage Area'] == 0
        self.m_df.loc[(garage_area_zero & (self.m_df['ord_Garage Cond'].isnull())),'ord_Garage Cond'] ='N_A'
        self.m_df.loc[(garage_area_zero & (self.m_df['ord_Garage Finish'].isnull())),'ord_Garage Finish'] ='N_A'
        self.m_df.loc[(garage_area_zero & (self.m_df['Garage Yr Blt'].isnull())),'Garage Yr Blt'] =0
        self.m_df.loc[(garage_area_zero & (self.m_df['ord_Garage Qual'].isnull())),'ord_Garage Qual'] ='N_A'
        self.m_df.loc[(garage_area_zero & (self.m_df['Garage Type'].isnull())),'Garage Type'] ='N_A'
        return self.m_df

    def Replace_basement_attributes_as_na_if_no_basement(self):
        zero_total_sqft_basement_area = self.m_df['Total Bsmt SF'] ==0  #Total square feet of basement area
        self.m_df.loc[ (zero_total_sqft_basement_area & (self.m_df['ord_BsmtFin Type 2'].isnull())) ,'ord_BsmtFin Type 2']='N_A'
        self.m_df.loc[ (zero_total_sqft_basement_area & (self.m_df['ord_BsmtFin Type 1'].isnull())) ,'ord_BsmtFin Type 1']='N_A'
        self.m_df.loc[ (zero_total_sqft_basement_area & (self.m_df['ord_Bsmt Qual'].isnull())) ,'ord_Bsmt Qual']='N_A'
        self.m_df.loc[ (zero_total_sqft_basement_area & (self.m_df['ord_Bsmt Cond'].isnull())) ,'ord_Bsmt Cond']='N_A'
        self.m_df.loc[ (zero_total_sqft_basement_area & (self.m_df['ord_Bsmt Exposure'].isnull())) ,'ord_Bsmt Exposure']='N_A'
        self.m_df.loc[ (zero_total_sqft_basement_area & (self.m_df['Bsmt Half Bath'].isnull())) ,'Bsmt Half Bath']=0
        self.m_df.loc[ (zero_total_sqft_basement_area & (self.m_df['Bsmt Full Bath'].isnull())) ,'Bsmt Full Bath']=0
        self.m_df.loc[ (zero_total_sqft_basement_area & (self.m_df['Bsmt Unf SF'].isnull())) ,'Bsmt Unf SF']=0
        return self.m_df

    def Replace_misc_feature_as_na_if_null(self):
        missing_misc_feature = self.m_df['Misc Feature'].isnull()
        self.m_df.loc[missing_misc_feature, 'Misc Feature'] ='N_A'
        return self.m_df

    def Replace_access_to_Alley_as_na_if_null(self):
         missing_alley =self.m_df['Alley'].isnull()
         self.m_df.loc[missing_alley, 'Alley'] ='N_A'
         return self.m_df

    def Replace_fence_as_na_if_null(self):
         missing_fence =self.m_df['ord_Fence'].isnull()
         self.m_df.loc[missing_fence, 'ord_Fence'] ='N_A'
         return self.m_df

    def impute_lot_frontage_with_avg_of_similar_homes(self,threshold):
         missing_lot_frontage =self.m_df['Lot Frontage'].isnull()
         for lot_area in self.m_df[missing_lot_frontage]['Lot Area']:
            lower_threshold_bracket =  lot_area-  (lot_area* threshold/100)
            upper_threshold_bracket =  lot_area +  (lot_area* threshold/100)
            # find all similar homes in with  +/-5% 'lot area' which has lot frontage
            lots_with_given_lot_area = (self.m_df['Lot Area'] > lower_threshold_bracket) & (self.m_df['Lot Area'] <upper_threshold_bracket)
            similar_lots_non_missing_frontage_count = len(self.m_df[lots_with_given_lot_area  & (~missing_lot_frontage)])
            # take average frontage  to impute the values
            if similar_lots_non_missing_frontage_count >0:
               mean_frontage = self.m_df[lots_with_given_lot_area & (~missing_lot_frontage) ]['Lot Frontage'].mean()
               self.m_df.loc[ (self.m_df['Lot Area'] == lot_area) & missing_lot_frontage ,'Lot Frontage'] =mean_frontage
         return self.m_df

    def disp_missing_data(self):
       column_null_counts = self.m_df.isnull().sum() *100/ len(self.m_df) #Filter to find missing data in percetage
       missing_data_columns =column_null_counts[column_null_counts >0] # get only columns where missing data  >0
       print (missing_data_columns.sort_values(ascending=False)) # display them in highest missing data at top

    def prefix_ordinal_column_names(self):
       self.m_df.rename(columns = {
            'Lot Shape': 'ord_Lot Shape',
            'Utilities': 'ord_Utilities',
            'Land Slope' : 'ord_Land Slope',
            'Overall Cond': 'ord_Overall Cond',
            'Overall Qual': 'ord_Overall Qual',
            'Exter Qual': 'ord_Exter Qual',
            'Exter Cond': 'ord_Exter Cond',
            'Bsmt Qual': 'ord_Bsmt Qual',
            'Bsmt Cond': 'ord_Bsmt Cond',
            'Bsmt Exposure': 'ord_Bsmt Exposure',
            'BsmtFin Type 1': 'ord_BsmtFin Type 1',
            'BsmtFin Type 2': 'ord_BsmtFin Type 2',
            'Heating QC': 'ord_Heating QC',
            'Central air conditioning': 'ord_Central air conditioning',
            'Electrical': 'ord_Electrical',
            'Kitchen Qual': 'ord_Kitchen Qual',
            'Functional': 'ord_Functional',
            'Fireplace Qu': 'ord_Fireplace Qu',
            'Garage Finish': 'ord_Garage Finish',
            'Garage Qual': 'ord_Garage Qual',
            'Garage Cond': 'ord_Garage Cond',
            'Paved Drive': 'ord_Paved Drive',
            'Pool QC': 'ord_Pool QC',
            'Fence': 'ord_Fence'
        },
        inplace = True
        )

def main():
  print("Hello World!")
  #dc = DataCleaner()

if __name__ ==  '__main__':
   main()
