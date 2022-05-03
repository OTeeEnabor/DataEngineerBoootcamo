import numpy as np
import pandas as pd
import pytest
from getoccupancy import getOccupancy

def test_with_missing_column():
    dataFrame = pd.DataFrame({'Temperature':[10,20,30,40],'notHumidity':[20,26,25,27]})
    testInput = [1,2]
    with pytest.raises(ValueError) as exception_info:
        getOccupancy(dataFrame,testInput)
        assert exception_info.match('Missing column')

def test_wrong_datatype_in_input():
    dataFrame = pd.DataFrame({'Temperature':[10,20,30,40],'notHumidity':[20,26,25,27]})
    testInput = ['1', '2']
    with pytest.raises(ValueError) as exception_info:
        getOccupancy(dataFrame,testInput)
        assert exception_info.match('Only int or float as datatype will work as an input.')

def test_missing_value():
    dataFrame = pd.DataFrame({'Temperature':[10,np.nan,30,40],'notHumidity':[20,26,np.nan,27]})
    testInput = [17, 25]
    with pytest.raises(ValueError) as exception_info:
        getOccupancy(dataFrame, testInput)
        assert exception_info.match('Missing value in dataframe column.')

# test on error cases
# test
