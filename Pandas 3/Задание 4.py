import pandas as pd


rzd = pd.DataFrame(
    {
        'client_id': [111, 112, 113, 114, 115],
        'rzd_revenue': [1093, 2810, 10283, 5774, 981]
    }
)

auto = pd.DataFrame(
    {
        'client_id': [113, 114, 115, 116, 117],
        'auto_revenue': [57483, 83, 912, 4834, 98]
    }
)

air = pd.DataFrame(
    {
        'client_id': [115, 116, 117, 118],
        'air_revenue': [81, 4, 13, 173]
    }
)

client_base = pd.DataFrame(
    {
        'client_id': [111, 112, 113, 114, 115, 116, 117, 118],
        'address': ['Комсомольская 4', 'Энтузиастов 8а', 'Левобережная 1а', 'Мира 14', 'ЗЖБИиДК 1',
                    'Строителей 18', 'Панфиловская 33', 'Мастеркова 4']
    }
)

table=rzd.merge(auto, how='outer', on='client_id')
table=table.merge(air, how='outer', on='client_id')
table.loc[table.rzd_revenue.isnull(), 'rzd_revenue',]=0
table.loc[table.auto_revenue.isnull(), 'auto_revenue',]=0
table.loc[table.air_revenue.isnull(), 'air_revenue',]=0
full_table=table.merge(client_base, how='outer', on='client_id')
print(full_table)