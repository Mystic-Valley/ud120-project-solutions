#!/usr/bin/python

import numpy as np
def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    temp_data = []
    ### your code goes here
    
    error = []
    error = abs(np.subtract(predictions, net_worths))
    l = len(ages)
    
    for i in range(l):
        temp_t = (ages[i], net_worths[i], error[i])
        temp_data.append(temp_t)
    
    temp_data.sort(key=lambda tup: tup[2])
    cleaned_data = temp_data[:int(0.9*l)]
    

    return cleaned_data

