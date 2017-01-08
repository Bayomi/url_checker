import pandas as pd
import patsy as ps    
import statsmodels.api as sm
import numpy as np
from sklearn import linear_model, cross_validation, svm
import matplotlib.pyplot as plt


def getProcessedData(file_name):
    
    data = pd.read_csv(file_name)
    missing_percentage = list()

    #choose the relevant variables
    #data = data_all[['amount_tsh', 'population', 'funder', 'basin', 'region', 'scheme_management', 'permit','construction_year','extraction_type','management','payment','quality_group','source_type','waterpoint_type']]
    
    """
    Working only with the Independent variables first
    """

    ###construction_year
    #construction year -> age
    data['construction_year'] = 2016 - data['construction_year'] 
    data['construction_year'] = data['construction_year'].replace([2016], [0])
    #missing data -> mean of the values
    medianConstructionFrame = data['construction_year'].replace(0, np.NaN)
    data['construction_year'] = data['construction_year'].replace(0, medianConstructionFrame.median())

    #normalize
    data['construction_year'] = data['construction_year']/data['construction_year'].max()

    ###amount_tsh
    medianConstructionFrame = data['amount_tsh'].replace(0, np.NaN)
    data['amount_tsh'] = data['amount_tsh'].replace(0, medianConstructionFrame.median())

    #normalize
    data['amount_tsh'] = data['amount_tsh']/data['amount_tsh'].max()

    ###population
    medianConstructionFrame = data['population'].replace(0, np.NaN)
    data['population'] = data['population'].replace(0, medianConstructionFrame.median())

    #normalize
    data['population'] = data['population']/data['population'].max()

    ###funder
    ###categorical => Government (1); Other(0)
    data.loc[data['funder'] != 'Government Of Tanzania', 'funder'] = 0
    data.loc[data['funder'] == 'Government Of Tanzania', 'funder'] = 1

    ###region
    ###categorical => Iringa (0); Other(1)
    data.loc[data['basin'] == 'Ruvuma / Southern Coast', 'basin'] = 1
    data.loc[data['basin'] == 'Lake Rukwa', 'basin'] = 1
    data.loc[data['basin'] != 1, 'basin'] = 0

    ###region
    ###categorical => Iringa (0); Other(1)
    data.loc[data['region'] != 'Iringa', 'region'] = 1
    data.loc[data['region'] == 'Iringa', 'region'] = 0

    ###scheme management
    ###categorical => VWC (1); Other(0)
    data.loc[data['scheme_management'] != 'VWC', 'scheme_management'] = 0
    data.loc[data['scheme_management'] == 'VWC', 'scheme_management'] = 1

    ###permit
    ###categorical => True (1); False(0) ; Missing()
    data.loc[data['permit'] == True, 'permit'] = 1
    data.loc[data['permit'] == False, 'permit'] = -1
    data['permit'] = data['permit'].replace(np.NaN, 0)

    ###permit
    ###categorical = payment (1); unknown(0); never pay (-1)
    data.loc[data['payment'] == 'never pay', 'payment'] = -1
    data.loc[data['payment'] == 'pay per bucket', 'payment'] = 1
    data.loc[data['payment'] == 'pay when scheme fails', 'payment'] = 1
    data.loc[data['payment'] == 'pay annually', 'payment'] = 1
    data.loc[data['payment'] == 'pay monthly', 'payment'] = 1
    data.loc[data['payment'] == 'other', 'payment'] = 0
    data.loc[data['payment'] == 'unknown', 'payment'] = 0
    data['payment'] = data['payment'].replace(np.NaN, 0)

    ###quality_group
    ###categorical => good (1); Other(0)
    data.loc[data['quality_group'] != 'good', 'quality_group'] = 0
    data.loc[data['quality_group'] == 'good', 'quality_group'] = 1

    #source_type
    data.loc[data['source_type'] == 'spring', 'source_type'] = 1
    data.loc[data['source_type'] == 'rainwater harvesting', 'source_type'] = 1
    data.loc[data['source_type'] == 'river/lake', 'source_type'] = 1
    data.loc[data['source_type'] != 1, 'source_type'] = 0

    #extraction type
    data.loc[data['extraction_type'] == 'gravity', 'extraction_type'] = 0
    data.loc[data['extraction_type'] == 'nira/tanira', 'extraction_type'] = 0
    data.loc[data['extraction_type'] != 0, 'extraction_type'] = 1

    #waterpoint_type
    data.loc[data['waterpoint_type'] == 'communal standpipe', 'waterpoint_type'] = 0
    data.loc[data['waterpoint_type'] == 'hand pump', 'waterpoint_type'] = 0
    data.loc[data['waterpoint_type'] != 0, 'waterpoint_type'] = 1

    #choose the relevant variables
    data = data[['id', 'amount_tsh', 'population', 'funder', 'basin', 'region', 'scheme_management', 'permit','construction_year','extraction_type','payment','quality_group','source_type','waterpoint_type']]

    return data

def getData():
	fileName = "data/trainingSetValues.csv"
	return getProcessedData(fileName)




