import pandas as pd
import json
import numpy as np
class BMIApp:
    def calculateBodyMassIndex(self,filepath):
        with open(filepath) as file:
            json_data=json.loads(file.read())
            BMI_Dataframe=pd.json_normalize(json_data)
            BMI_Dataframe["BMI(Body Mass Index)"]=BMI_Dataframe["WeightKg"]/((BMI_Dataframe["HeightCm"]/100))**2
            BMI_Dataframe.replace([np.inf, -np.inf], np.nan, inplace=True) #Handling HeightCm=0 case
            BMI_Dataframe.dropna(inplace=True) 
            
            bmi_range=[(BMI_Dataframe['BMI(Body Mass Index)']<=18.4),
            (BMI_Dataframe['BMI(Body Mass Index)']>=18.5)&(BMI_Dataframe['BMI(Body Mass Index)']<=24.9),
            (BMI_Dataframe['BMI(Body Mass Index)']>=25)&(BMI_Dataframe['BMI(Body Mass Index)']<=29.9),
            (BMI_Dataframe['BMI(Body Mass Index)']>=30)&(BMI_Dataframe['BMI(Body Mass Index)']<=34.9),
            (BMI_Dataframe['BMI(Body Mass Index)']>=35)&(BMI_Dataframe['BMI(Body Mass Index)']<=39.9),
            (BMI_Dataframe['BMI(Body Mass Index)']>=40)
            ]
            Weight_Category=['Underweight','Normal weight','Overweight','Moderately obese','Severly obese','Very severly obese']
            Risk_Category=['Malnutrition risk','Low risk','Enhanced risk','Medium risk','High risk','Very high risk']

            BMI_Dataframe['BMI Category']=np.select(bmi_range,Weight_Category)
            BMI_Dataframe['Health risk']=np.select(bmi_range,Risk_Category)

            BMI_Dataframe['BMI(Body Mass Index)']=BMI_Dataframe['BMI(Body Mass Index)'].astype('float64')
            BMI_Dataframe['BMI(Body Mass Index)']=BMI_Dataframe['BMI(Body Mass Index)'].round(1) #rounding BMI(Body Mass Index) column values to 1 decimal place
            return BMI_Dataframe


    def count_overweight(self,BMI_Dataframe) :
        count_overweight_persons=BMI_Dataframe[BMI_Dataframe['BMI Category']=='Overweight'].shape[0]
        return count_overweight_persons
    
if __name__=='__main__':
    obj=BMIApp()
    df=obj.calculateBodyMassIndex('data.json')
    count=obj.count_overweight(df)
    print(df)
    print("Count of overweight persons: ",count)
