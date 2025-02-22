# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15fGPVtON4RMx1CRYqXMgyit3XulYtNXR
"""

import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

from sklearn.model_selection import train_test_split

from  sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier

from sklearn.tree import DecisionTreeClassifier

from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import f1_score

from sklearn.metrics import classification_report, confusion_matrix

import warnings

import pickle

from scipy import stats

warnings.filterwarnings('ignore')

plt.style.use('fivethirtyeight')

df=pd.read_excel('/content/Data_Train.xlsx')

df.head()

df.shape

df.Date_of_Journey=df.Date_of_Journey.str.split('/')

df.Date_of_Journey

#Since the maximum number of stops is 4, there should be maxium 6 citles in any particular route. We split the data in route col
df.Route=df.Route.str.split('->')

df.Route

#In the similar manner, We split the Dep_time column, and create  separate columns for departure hours and minitus-
df.Dep_Time.str.split(':')

df['Dep_Time_Hour']=df.Dep_Time.str[0]
df['Dep_Time_Hour']=df.Dep_Time.str[1]

df.Arrival_Time=df.Arrival_Time.str.split('')

df['Arrival_date'] = df.Arrival_Time.str[1]
df['Time_of_Arrival'] = df.Arrival_Time.str[0]

df['Time_of_Arrival']=df.Time_of_Arrival.str.split(':')

df['Arrival_Time_Hour']=df.Time_of_Arrival.str[0]
df['Arrival_Time_Mins']=df.Time_of_Arrival.str[1]

df.Duration=df.Duration.str.split('')

df['Travel_Hours']=df.Duration.str[0]
df['Travel_Hours']=df['Travel_Hours'].str.split('h')
df['Travel_Hours']=df['Travel_Hours'].str[0]
df.Travel_Hours=df.Travel_Hours
df['Travel_Mins']=df.Duration.str[1]

df.Travel_Mins=df.Travel_Mins.str.split('m')
df.Travel_Mins=df.Travel_Mins.str[0]

df.Total_Stops.replace('non_stop',0,inplace=True)
df.Total_Stops=df.Total_Stops.str.split('')
df.Total_Stops=df.Total_Stops.str[0]

df.Additional_Info.unique()

df.Additional_Info.replace('NO Info','No info',inplace=True)

df.isnull().sum()

df.dropna(inplace=True)

df.isnull().sum()

df.fillna('None',inplace=True)

df.fillna(df,inplace=True)

df.info()

df.rename_axis

index=index_mapper, columns=columns_mapper,axis={'index', 'columns'}

df.Travel_Hours=df.Travel_Hours.astype('int64')

egorical=['Airline','Source','Destination','Additional_Info','City1']
numerical=['Date','Montcath','Year','Dep_Time_Hour','Dep_Time_Mins','Arrival_date','Arrival_Time_Hour','Arrival_Time_Mins','Travel_Hours','Trval_Mins']

df.head()

egorical=['Airline','Source','Destination','Additional_Info','City1']
numerical=['Date','Montcath','Year','Dep_Time_Hour','Dep_Time_Mins','Arrival_date','Arrival_Time_Hour','Arrival_Time_Mins','Travel_Hours','Trval_Mins']

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()

pd.set_option('display.max_columns',33)

df = pd.read_excel('/content/Data_Train.xlsx')

# Applying label encoder
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()

df.head()

df.head()

df.describe()

plt.figure(figsize = (10, 10))
plt.title('Count of flights with different Airlines')
sns.countplot(x = 'Airline', data = df)
plt.xlabel('Airline')
plt.ylabel('Count of flights')
plt.xticks(rotation = 90)

## Number of Flights From Each Source
ax = sns.countplot(data=df,x='Source')
ax.bar_label(ax.containers[0]);

plt.figure(figsize = (10, 10))
plt.title('Count of flights according to departure time')
sns.countplot(x = 'Source', data = df)
plt.xlabel('Flight Time')
plt.ylabel('Count of flights')

# We can make Visualization With Avg. Price for Destination
sns.barplot(x='Destination',y='Price',data=df.sort_values('Price',ascending=False))

plt.figure(figsize=(15,8))
sns.boxplot(x='Total_Stops',y='Price',data=df.sort_values('Price',ascending=False))

#plotting countplots for categorical df

import seaborn as sns
c=1
plt.figure(figsize=(20,45))

import missingno as msno
msno.bar(df)
plt.show

plt.figure(figsize=(15,8))
sns.distplot(df.Price)

from sklearn import datasets  
import pandas as p  
import seaborn  
import matplotlib. pyplot as pt  
dataset = datasets. load_iris ()  
dataframe = p. DataFrame (data = dataset. data, columns = dataset. feature_names)  
dataframe ["relation"] = dataset. target  
correlation = dataframe.corr ()  
heatmap = seaborn. heatmap(correlation, annot = True)  
heatmap.set (xlabel = 'IRIS values on x axis',ylabel = 'IRIS values on y axis\t', title = "Correlation matrix of IRIS dataset\n")  
pt. show ()

sns.boxplot(x= 'Price', data=df);

y=df['Price']
x=df.drop(columns=['Price'],axis=1)

### Scaling the df

from sklearn.preprocessing import StandardScaler
ss=StandardScaler()

def plot(data,col):
    fig,(ax1,ax2)=plt.subplots(2,1)
    sns.distplot(data[col],ax=ax1)
    sns.boxplot(data[col],ax=ax2)

data1=pd.set_option('display.max_columns',33)
df.head()

def plot(data,col):
    fig,(ax1,ax2)=plt.subplots(2,1)
    sns.distplot(data[col],ax=ax1)
    sns.boxplot(data[col],ax=ax2)

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

train_data=pd.read_excel('/content/Data_Train.xlsx')
train_data.head()

test_data=pd.read_excel('/content/Data_Train.xlsx')
test_data.head()

tain_data=train_data[train_data['Total_Stops'].notnull()]

train_data['Total_Stops']=train_data['Total_Stops'].str[0]
test_data['Total_Stops']=test_data['Total_Stops'].str[0]

train_data['Total_Stops']=train_data['Total_Stops'].apply(lambda x : str(x)if str(x).isdigit() else 0 ).astype('int64')
test_data['Total_Stops']=test_data['Total_Stops'].apply(lambda x : str(x)if str(x).isdigit() else 0 ).astype('int64')

from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor
rfr=RandomForestRegressor()
gb=GradientBoostingRegressor()
ad=AdaBoostRegressor()

from sklearn.feature_selection import mutual_info_classif

from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
def predict(ml_model):
    print('Model is: {}'.format(ml_model))
    model= ml_model.fit(X_train,y_train)
    print("Training score: {}".format(model.score(X_train,y_train)))
    predictions = model.predict(X_test)
    print("Predictions are: {}".format(predictions))
    print('\n')
    r2score=r2_score(y_test,predictions) 
    print("r2 score is: {}".format(r2score))
          
    print('MAE:{}'.format(mean_absolute_error(y_test,predictions)))
    print('MSE:{}'.format(mean_squared_error(y_test,predictions)))
    print('RMSE:{}'.format(np.sqrt(mean_squared_error(y_test,predictions))))
    sns.distplot(y_test-predictions)

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import GradientBoostingRegressor,RandomForestRegressor

RandomForestRegressor()

#crwating list of category columns 

category=['Airline','Source','Destination','Additional-Info']
category

df['Date_of_Journey'].unique(),df['Date_of_Journey'].nunique()

from sklearn.feature_selection import mutual_info_classif

# Helper funtion to plot and check parameter values


def test_params_and_plot(param_name,values):
    train_errors , val_errors = [] , []
    for value in values:
        params = {param_name: value}
        train_rmse,test_rmse = test_params(**params)
        train_errors.append(train_rmse)
        val_errors.append(test_rmse)
    plt.figure(figsize=(16,8))
    plt.title('Overfitting curve:  params')
    plt.plot(values, train_errors, 'g-*')
    plt.plot(values, val_errors, 'r-o')
    plt.xlabel(param_name)
    plt.ylabel('rmse')
    plt.legend(['Training', 'Test'])

from sklearn.feature_selection import mutual_info_classif

def get_scores(models,xtrain,ytrain):
    for name,model in models.items():
        model["model"].fit(xtrain,ytrain)

        score_r2 = score_dataset(xtrain, ytrain, model=model["model"])
        score = {'model':"Linear regression", 'score_r2':score_r2}
        print("--- "+name+" ---")
        print("Score r2: {}".format(score_r2))
        print("\n")

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import GradientBoostingRegressor,RandomForestRegressor

RandomForestRegressor()

KNeighborsRegressor()

from sklearn.model_selection import cross_val_score
for i in range(2,5):
    print(rfr,df.mean())

from sklearn.model_selection import RandomizedSearchCV

param_grid={'n_estimators':[10,30,50,70,100],'max_depth':[None,1,2,3],'max_features':['auto','sqrt']}
rfr=RandomForestRegressor()
rf_res=RandomizedSearchCV(estimator=rfr,param_distributions=param_grid,cv=3,verbose=2,n_jobs=-1)


rf_res.fit

gb=GradientBoostingRegressor()
gb_res=RandomizedSearchCV(estimator=gb,param_distributions=param_grid,cv=3,verbose=2,n_jobs=-1)

gb_res.fit

rfr.fit
y_train_pred=rfr.predict
y_test_pred=rfr.predict
print("train accuracy",r2_score)
print("test accuracy",r2_score)

knn=KNeighborsRegressor(n_neighbors=2,algorithm='auto',metric_params=None,n_jobs=-1)
knn.fit
y_train_pred=rfr.predict
y_test_pred=rfr.predict
print("train accuracy",r2_score)
print("test accuracy",r2_score)

rfr=RandomForestRegressor(n_estimators=10,max_features='sqrt',max_depth=None)
rfr.fit
y_train_pred=rfr.predict
y_test_pred=rfr.predict
print("train accuracy",r2_score)
print("test accuracy",r2_score)

price_list=pd.DataFrame({'Price'})

price_list

price_list

import pickle

!pip install flask-ngrok

pickle.dump(rfr,open('model1.pkl','wb'))

from flask import Flask, render_template, request
import numpy as np
import pickle

model = (open(r"model1.pkl",'rb'))

("/home")
def home():
    return render_template('home.html')

("/predict")
def home1():
    return render_template('predict.html')

def predict():

    print(x)

    x = np.array(x)
    print(x.shape)

    print(x)
    pred = model.predict(x)
    print(pred)
    return render_template('submit.html', prediction_text=pred)

!pip install nbconvert

!jupyter nbconvert --to html Untitled1.ipynb