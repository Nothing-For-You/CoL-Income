import pandas as pd
import numpy as np

costofliving = pd.read_csv('cost-of-living.csv')
income = pd.read_excel('Income by Country.xlsx', sheet_name="GNI per capita")
col_values = []
yeah = ["yes", "yeah", "sure", "y", "1", "true"]
nah = ["no", "nah", "no thanks", "n", "0", "false"]

def find_ratio(country):
    inc_val = 0
    for column in costofliving.columns:
        if country.capitalize() in column:
            col_values.append(costofliving.loc[31, column])
        # else:
        #     return "Country not in Database"
    for index, row in income.iterrows():
        if country.capitalize() in row.values:
            inc_val = income.loc[index, 2018]
            break
        # else:
        #     return "Country not in Database"
    ratio = (np.mean(col_values) * 1.0588008 / inc_val) * 100
    return "The Cost of Living/Income score of "+country+" is "+str(round(ratio, 3))


while True:
    run = input("Would you like to run the program (Yes or No): ")
    if run.lower() in yeah:
        print(find_ratio(input("Enter country name: ")))
    elif run.lower() in nah:
        print("Program terminated")
        break
    else:
        print("Please enter a valid option")
