#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

def generate_car_matrix(file):
    df = pd.read_csv(file)
    
    # Pivot the dataframe to reshape it
    df_pivot = df.pivot(index='id_1', columns='id_2', values='car')
    
    # Make diagonal values 0
    df_pivot.values[[np.arange(len(df_pivot))] * 2] = 0
    
    return df_pivot

# Example usage:
file = 'dataset-1.csv'
car_matrix = generate_car_matrix(file)
print(car_matrix)


# In[2]:


import pandas as pd

def generate_car_matrix(file):
    # Read file
    df = pd.read_csv(file)

    # Pivot the DataFrame
    car_matrix = df.pivot(index='id_1', columns='id_2', values='car').fillna(0)

    # Setting diagonal values to zero
    for i in car_matrix.index:
        if i in car_matrix.columns:
            car_matrix.at[i, i] = 0

    return car_matrix

file = 'dataset-1.csv'
result_matrix = generate_car_matrix(file)
print(result_matrix)


# In[3]:


import pandas as pd

def get_type_count(file_path):
    
    df = pd.read_csv(file_path)

    df['car_type'] = pd.cut(df['car'], bins=[-float('inf'), 15, 25, float('inf')], labels=['low', 'medium', 'high'])

    type_counts = df['car_type'].value_counts().to_dict()

    sorted_type_counts = dict(sorted(type_counts.items()))

    return sorted_type_counts

file_path = 'dataset-1.csv'
result_type_counts = get_type_count(file_path)
print(result_type_counts)


# In[4]:


import pandas as pd

def get_bus_indexes(file_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Calculate the mean value of the 'bus' column
    mean_bus = df['bus'].mean()

    # Identify indices where 'bus' values are greater than twice the mean
    bus_indexes = df[df['bus'] > 2 * mean_bus].index.tolist()

    # Sort the indices in ascending order
    bus_indexes.sort()

    return bus_indexes

# Example usage:
file_path = 'dataset-1.csv'
result_bus_indexes = get_bus_indexes(file_path)
print(result_bus_indexes)


# In[5]:


import pandas as pd

def filter_routes(file_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Filter routes based on the average of values in the 'truck' column
    filtered_routes = df.groupby('route')['truck'].mean().loc[lambda x: x > 7].index.tolist()

    # Sort the list of filtered routes in ascending order
    filtered_routes.sort()

    return filtered_routes

# Example usage:
file_path = 'dataset-1.csv'
result_filtered_routes = filter_routes(file_path)
print(result_filtered_routes)


# In[6]:


def multiply_matrix(car_matrix):
    # Create a copy of the car matrix to avoid modifying the original DataFrame
    modified_matrix = car_matrix.copy()

    # Apply the specified logic to modify values
    modified_matrix[modified_matrix > 20] *= 0.75
    modified_matrix[modified_matrix <= 20] *= 1.25

    # Round the values to 1 decimal place
    modified_matrix = modified_matrix.round(1)

    return modified_matrix

# Example usage:
file_path = 'dataset-1.csv'
car_matrix = generate_car_matrix(file_path)
modified_matrix = multiply_matrix(car_matrix)
print(modified_matrix)


# In[ ]:




