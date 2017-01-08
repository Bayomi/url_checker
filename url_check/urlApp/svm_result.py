import svm_train as tu
import url_to_vector as ck
import numpy as np

def checkUrl(url):
	vector = ck.makeVector(url)
	vector = np.array(vector)
	vector = vector.reshape(1, -1)
	print vector
	X, y = tu.getXYModified('data/url_data.csv')
	result = tu.getSVMFull(X, y, vector)
	print result
	return result

"""
url = "http://www.google.com"
print checkUrl(url)
"""