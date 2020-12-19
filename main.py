import pandas as pd

#  # Create a dataframe
#  raw_data = {'first_name': ['Sam','Ziva','Kia','Robin'],
#                      'degree': ['PhD','MBA','','MS'],
#                      'age': [25, 29, 19, 21]}
#  df = pd.DataFrame(raw_data)
#
#  df
#
#  #Save the dataframe
#  df.to_csv(r'/csv/Example1.csv')

df = pd.read_csv("/mnt/c/Users/henry/Desktop/workspaces/HACA-repositories/data-science-learning/csv/Example1.csv")

#  new csv file from google
#  df2 = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
#
#  #  saving a url csv cause I only find useless examples
#  df2.to_csv(r"csv/irs.csv")

df2 = pd.read_csv("/mnt/c/Users/henry/Desktop/workspaces/HACA-repositories/data-science-learning/csv/irs.csv", names=['id','firts_date','second_date','thrird_date','four_date','five_date'])

#  name_setosa = df2['five_date'] == 'Iris-setosa'
#
#  only_setosa_df = df2[name_setosa]
#  print(only_setosa_df)

only_setosa_df = df2[df2['five_date'] == 'Iris-setosa']
print(only_setosa_df.head(10))


