import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import xgboost as xgb

# download dataset from github repository
df = pd.read_csv('https://raw.githubusercontent.com/MainakRepositor/Datasets/master/water_potability.csv')

# make all columns lowercase
df.columns = df.columns.str.replace(' ', '_').str.lower()

# missing data will be populated with mean values of the dataset split by potability

#split data
df_pot = df[df.potability == 1]
df_non_pot = df[df.potability == 0]

#calculate means
pot_ph = df_pot.ph.mean()
pot_sulfate = df_pot.sulfate.mean()
pot_trihalomethanes = df_pot.trihalomethanes.mean()

non_pot_ph = df_non_pot.ph.mean()
non_pot_sulfate = df_non_pot.sulfate.mean()
non_pot_trihalomethanes = df_non_pot.trihalomethanes.mean()

# populate potable data
df_pot.ph = df_pot.ph.fillna(pot_ph)
df_pot.sulfate = df_pot.sulfate.fillna(pot_sulfate)
df_pot.trihalomethanes = df_pot.trihalomethanes.fillna(pot_trihalomethanes)

# populate non potable data
df_non_pot.ph = df_non_pot.ph.fillna(non_pot_ph)
df_non_pot.sulfate = df_non_pot.sulfate.fillna(non_pot_sulfate)
df_non_pot.trihalomethanes = df_non_pot.trihalomethanes.fillna(non_pot_trihalomethanes)

# split dataset into test and train

#test data will be 15% of the total
#since data was split by potability before, it need to be suffled
# stratify parameter is used to keep proporcion of potability into datasets

df_train, df_test = train_test_split(df,test_size=0.15, shuffle=True, random_state=7, stratify=df.potability)

# split datasets into features and feture to be estimated
x_train = df_train.drop(['potability'], axis = 1)
y_train = df_train.potability

x_test = df_test.drop(['potability'], axis = 1)
y_test = df_test.potability

# train model
model = xgb.XGBClassifier(n_estimators = 100, 
                          max_depth = 6, 
                          learning_rate = 0.2, 
                          random_state = 7)

model.fit(x_train, y_train)

# save model as pickle file
with open('model.bin', 'wb') as f_out:
    pickle.dump(model, f_out)

print('Model was saved as model.bin')