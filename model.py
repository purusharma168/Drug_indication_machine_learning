import warnings

import pandas as pd


from sklearn.preprocessing import StandardScaler
from sklearn.linear_model  import Ridge,Lasso,RidgeCV, LassoCV, ElasticNet, ElasticNetCV, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, roc_curve, roc_auc_score

warnings.filterwarnings('ignore')

df = pd.read_csv('/Users/purusharma/PycharmProjects/Drug_indication_machine_learning/Preprocessed data/final_soltion_drugdata.csv')
# Import train_test_split function
from sklearn.model_selection import train_test_split

X=df[['src_nm', 'src_id', 'cas_cas_no', 'cas_pt','cas_source','cas_match','umls_pt','umls_cui','ind_raw_value','ind_raw_target','ind_raw_match','ind_umls_entry_term_match']]  # Features
y=df['drug_raw_name']  # Labels

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2) # 80% training and 30% test

log_reg = LogisticRegression()
log_reg.fit(X_train,y_train)
y_pred = log_reg.predict(X_test)

log_reg.fit(X_train,y_train)

y_pred =log_reg.predict(X_test)

#
# # Preparing Extra Tree Regression
# #Import Random Forest Model
# from sklearn.ensemble import RandomForestClassifier
#
# #Create a Gaussian Classifier
# clf=RandomForestClassifier(n_estimators=200)
#
# #Train the model using the training sets y_pred=clf.predict(X_test)
# clf.fit(X_train,y_train)
#
# y_pred=clf.predict(X_test)

import pickle

# please use this file to upload for saving model file
# Saving model to disk
pickle.dump(log_reg, open('model.pkl', 'wb'))
# model = pickle.load(open('model.pkl', 'rb'))
print(y_pred)
