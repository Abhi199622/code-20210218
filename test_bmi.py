import bmi
import pytest as pt



def test_edge_cases_moderatelyObese():
    obj=bmi.BMIApp()
    df=obj.calculateBodyMassIndex('data.json')
    test=df[(df['BMI(Body Mass Index)']==34.9)]
    if test.shape[0]>=1:
      BMICategory=set(test['BMI Category'])
      l=len(BMICategory)
      if l==1 and 'Moderately obese' in BMICategory:
        assert True
      else:
        assert False

def test_edge_cases_Underweight():
    obj=bmi.BMIApp()
    df=obj.calculateBodyMassIndex('data.json')
    test=df[(df['BMI(Body Mass Index)']==18.4)]
    if test.shape[0]>=1:
      BMICategory=set(test['BMI Category'])
      l=len(BMICategory)
      if l==1 and 'Underweight' in BMICategory:
        assert True
      else:
        assert False

def test_edge_case_Lowrisk():
    obj=bmi.BMIApp()
    df=obj.calculateBodyMassIndex('data.json')
    test=df[(df['BMI(Body Mass Index)']==18.5)]
    if test.shape[0]>=1:
      HealthCategory=set(test['Health risk'])
      l=len(HealthCategory)
      if l==1 and 'Low risk' in HealthCategory:
        assert True
      else:
        assert False

def test_edge_case_EnhancedRisk():
    obj=bmi.BMIApp()
    df=obj.calculateBodyMassIndex('data.json')
    test=df[(df['BMI(Body Mass Index)']==29.9)]
    if test.shape[0]>=1:
      HealthCategory=set(test['Health risk'])
      l=len(HealthCategory)
      if l==1 and 'Enhanced risk' in HealthCategory:
        assert True
      else:
        assert False



