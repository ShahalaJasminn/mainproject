# import pandas as pd
#
# # Path to your CSV file
# csv_file = r"C:\Users\shaha\PycharmProjects\FarmMoni\media\chemicals.csv"
#
# # Read the CSV file
# df = pd.read_csv(csv_file)
#
# # Display the first few rows
# print(df.head())


import pandas as pd

# Load the CSV file
csv_file = r"C:\Users\shaha\PycharmProjects\FarmMoni\media\chemicals.csv"
df = pd.read_csv(csv_file)

a="Apple - Healthy"

recommended_chemical = df.loc[df["Plant - Disease"] == a ,["Recommended Chemical","Application Method"]]

# Display the result
print(recommended_chemical.values[0][0])
print(recommended_chemical.values[0][1])
print("===0000000000")
