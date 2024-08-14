import pandas as pd

# Dataframe
data = {
    'furniture': ['bed', 'cot', 'table', 'wardrobe', 'cabinet'],
    'centimeters': [200, 100, 180, 250, 50]
}

dataFrame = pd.DataFrame(data)
dataFrame.to_excel('furniture_measures.xlsx', index=False)