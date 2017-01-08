import pandas as pd
import patsy as ps    
import statsmodels.api as sm
import numpy as np
from sklearn import linear_model, cross_validation, svm
import matplotlib.pyplot as plt
import bsoup_check as bc


def isIpOnUrl(url):
	numbers = sum(c.isdigit() for c in url)
	if numbers>4:
		return -1
	return 1

def isTooBig(url):
	size = len(url)
	if size<54:
		return 1
	if size>54 and size<75:
		return 0
	if size>75:
		return -1

def isShortened(url):
	urlArr = url.split('.')
	if (urlArr[1] == 'bit' and urlArr[2] == 'ly') or (urlArr[1] == 'goo' and urlArr[2] == 'gl') or \
	(urlArr[1] == 'ow' and urlArr[2] == 'ly') or (urlArr[1] == 't' and urlArr[2] == 'co') or \
	(urlArr[1] == 'tinyurl' and urlArr[2] == 'com'):
		return -1
	return 1

def containsAt(url):
	if '@' not in url:
		return 1
	return -1

def hasDash(url):
	if '-' not in url:
		return 1
	return -1

def hasSlashesRedir(url):
	urlArr = url.split('.')[1:]
	newUrl = '.'.join(urlArr)
	if '//' not in newUrl:
		return 1
	return -1

def hasTooManySubDomains(url):
	urlArr = url.split('.')
	size = len(urlArr) - 4
	if size<=1:
		return 1
	if size>1 and size<=2:
		return 0
	if size>2:
		return -1

def hasHttpsOutOfPlace(url):
	print url.count('https')
	if url.count('https')<2:
		return 1
	return -1

def verifyRequests(url):
	percentage = bc.checkItems('img', url, 'src')
	if percentage<=0.22:
		return 1
	if percentage>0.22 and percentage<=0.61:
		return 0
	if percentage>0.61:
		return -1

def anchorUrl(url):
	percentage = bc.checkItems('a', url, 'href')
	if percentage<=0.31:
		return 1
	if percentage>0.31 and percentage<=0.67:
		return 0
	if percentage>0.67:
		return -1

def scriptUrl(url):
	percentage = bc.checkItems('script', url, 'src')
	if percentage<=0.17:
		return 1
	if percentage>0.17 and percentage<=0.81:
		return 0
	if percentage>0.81:
		return -1

def abnormalCheck(url):
	if bc.isOrgOnUrl(url):
		return 1
	return -1

def ageOfDomain(url):
	if bc.isValidFor6Months(url):
		return 1
	return -1


def makeVector(url):
	vector = []
	try:
	  r = isIpOnUrl(url)
	  vector.append(r)
	except:
		print 'error'
		vector.append(0)
	try:
	  r = isTooBig(url)
	  vector.append(r)
	except: 
		print 'error'
		vector.append(0)
	try:
	  r = isShortened(url)
	  vector.append(r)
	except:
		print 'error'
		vector.append(0)
	try:
	  r = containsAt(url)
	  vector.append(r)
	except:
		print 'error'
		vector.append(0)
	try:
	  r = hasSlashesRedir(url)
	  vector.append(r)
	except:
		print 'error'
		vector.append(0)
	try:
	  r = hasDash(url)
	  vector.append(r)
	except:
		print 'error'
		vector.append(0)
	try:
	  r = hasTooManySubDomains(url)
	  vector.append(r)
	except:
		print 'error'
		vector.append(0)
	try:
	  r = hasHttpsOutOfPlace(url)
	  vector.append(r)
	except:
		print 'error'
		vector.append(0)
	try:
	  r = verifyRequests(url)
	  vector.append(r)
	except:
		print 'error'
		vector.append(-1)
	try:
	  r = anchorUrl(url)
	  vector.append(r)
	except:
		print 'error'
		vector.append(-1)
	try:
	  r = scriptUrl(url)
	  vector.append(r)
	except:
		print 'error'
		vector.append(-1)
	try:
	  r = abnormalCheck(url)
	  vector.append(r)
	except:
		print 'error'
		vector.append(-1)
	try:
	  r = ageOfDomain(url)
	  vector.append(r)
	except:
		print 'error'
		vector.append(-1)
	return vector




"""
bit.ly (Bitly)
goo.gl (Google)
ow.ly (Hootsuite)
t.co (Twitter)
TinyURL (Gilby)
Tr.im (Gravity4)
"""