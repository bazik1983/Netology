import pandas as pd


power_data = pd.read_csv('power.csv')
sub_data = power_data.query('country in ("Latvia", "Lithuania", "Estonia") '
                            '& category in (4, 12, 21) & 2005 < year < 2010 & quantity >= 0')

print(f"Cуммарное потребление стран Прибалтики: {sub_data['quantity'].sum()}")
