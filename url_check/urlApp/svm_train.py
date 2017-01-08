import pandas as pd
import patsy as ps    
import statsmodels.api as sm
import numpy as np
from sklearn import linear_model, cross_validation, svm
import matplotlib.pyplot as plt


def getXY(file_name):

	train_data = pd.read_csv(file_name)
	nameOfTargetVariable='label'
	myColumns=['using_ip','long_url','shortening','symbol_@','redir_slashes','dash_use','multi_domain','https_trust','domain_expiration','favicon','weird_port','domain_https','request_url','url_anchor','links_correl','server_handler','submit_mail','abnormal','forwarding','status_bar','disable_click','popup','iframe','age_domain','dns_record','web_traffic','page_rank','google_index','point_links','stats']
	y=np.ravel(train_data.as_matrix(columns=[nameOfTargetVariable]))
	X=train_data.as_matrix(columns=myColumns)
	return X, y

def getXYModified(file_name):

	train_data = pd.read_csv(file_name)
	nameOfTargetVariable='label'
	myColumns=['using_ip','long_url','shortening','symbol_@','redir_slashes','dash_use','multi_domain','domain_https','request_url','url_anchor','links_correl','abnormal','age_domain']
	#myColumns=['using_ip','long_url','shortening','symbol_@','redir_slashes','dash_use','multi_domain','domain_https']
	y=np.ravel(train_data.as_matrix(columns=[nameOfTargetVariable]))
	X=train_data.as_matrix(columns=myColumns)
	return X, y

def getScoreLogModel(X, y):

    # Linear Regression
    linModel = linear_model.LinearRegression() 
    linModel.fit(X,y) # This line is only necessary if you want to use the parameters
    #print linModel.coef_

    # Source of the implementation Idea: http://scikit-learn.org/stable/modules/cross_validation.html
    X_train, X_test, y_train, y_test = getTrainAndTest(X, y)
    
    # Logistic Regression    
    logModel = linear_model.LogisticRegression().fit(X_train,y_train)
    scoreLogModel=logModel.score(X_test, y_test)
    return scoreLogModel

def getTrainAndTest(X, y):
	
	X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.15, random_state=0)
	return X_train, X_test, y_train, y_test 

def getSVMClassifierResult(X, y):
	classifier = svm.SVC(C=100.0, cache_size=200, class_weight=None, coef0=0.0,
  decision_function_shape=None, degree=3, gamma=0.001, kernel='rbf',
  max_iter=2000, probability=False, random_state=None, shrinking=True,
  tol=0.001, verbose=False)

	X_train, X_test, y_train, y_test = getTrainAndTest(X, y)

	classifier.fit(X_train, y_train)

	expected = y_test
	predicted = classifier.predict(X_test)
	return rateOfError(predicted, expected)

def getSVMFull(X, y, testX):
	classifier = svm.SVC(C=100.0, cache_size=200, class_weight=None, coef0=0.0,
  decision_function_shape=None, degree=3, gamma=0.001, kernel='rbf',
  max_iter=2000, probability=False, random_state=None, shrinking=True,
  tol=0.001, verbose=False)

	classifier.fit(X, y)

	predicted = classifier.predict(testX)
	return predicted

def rateOfError(predicted, expected):
  size = len(predicted)
  count = 0
  for i in range(0, size):
    if predicted[i]==expected[i]:
      count = count + 1
  return count/float(size)


"""
#X, y = getXYModified('url_data.csv')
X, y = getXYModified('url_data.csv')
print X
print y
print getSVMClassifierResult(X, y)
#print getScoreLogModel(X, y)
"""
