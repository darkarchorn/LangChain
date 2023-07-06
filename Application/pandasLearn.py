import numpy as np
import pandas as pd

datas = np.array([[1,2], [3,4], [5,6]])
column_names = np.array(["hang_chuc", "hang tram"])
my_dataframe = pd.DataFrame(columns=column_names, data=datas)
print(my_dataframe)

my_dataframe["adjusted"] = my_dataframe["hang tram"] *100
print(my_dataframe)

print("Rows #0, #1, and #2:")
print(my_dataframe.head(3), '\n')

print("Row #2:")
print(my_dataframe.iloc[[2]], '\n')

print("Rows #1, #2, and #3:")
print(my_dataframe[1:4], '\n')

print("Column 'hang tram':")
print(my_dataframe['hang tram'])

# Task 1
names = ["Eleanor", "Chidi", "Tahani", "Jason"]
data = np.random.randint(low=0, high=101, size=(3, 4))
my_dataframe_2 = pd.DataFrame(columns=names, data=data)
print(my_dataframe_2)
print(my_dataframe_2["Eleanor"][1])
my_dataframe_2["Janet"] = my_dataframe_2['Tahani'] + my_dataframe_2["Jason"]
print(my_dataframe_2)

#Referencing
my_reference_dataframe = my_dataframe
#Copying
my_copying_dataframe = pd.DataFrame.copy(my_dataframe)
my_reference_dataframe["new column"] = my_dataframe["adjusted"] +50
print(my_dataframe) # has the new column
print(my_copying_dataframe) #doesnt have the new column
