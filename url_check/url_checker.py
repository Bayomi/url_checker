import test_url as tu
import check as ck
import numpy as np

def checkUrl(url):
	vector = ck.makeVector(url)
	vector = np.array(vector)
	vector = vector.reshape(1, -1)
	print vector
	X, y = tu.getXYModified('url_data.csv')
	result = tu.getSVMFull(X, y, vector)
	return result

url = "http://www.@2345m-w.com"
print checkUrl(url)