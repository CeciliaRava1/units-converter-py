import pandas as pd

def convertCentimetersToInches(centimeters):
    return centimeters/2.54

# Read furniture_measures.xlsx
dataframe = pd.read_excel('furniture_measures.xlsx')

# Create column 'inches'. Complete it with data from 'convertCentimetersToInches'
dataframe['inches'] = dataframe['centimeters'].apply(convertCentimetersToInches)
dataframe.to_excel('furniture_measures_converted.xlsx', index=False)
print("Conversion completed and saved as 'furniture_measures_converted.xlsx'")