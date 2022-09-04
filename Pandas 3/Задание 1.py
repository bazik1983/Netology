import pandas as pd


log = pd.read_csv('visit_log.csv', sep=';')


def source_type(row):
    if row['traffic_source'] == 'yandex' or row['traffic_source'] == 'google':
        return 'organic'
    elif (row['traffic_source'] == 'paid' or row['traffic_source'] == 'email') and row['region'] == 'Russia':
        return 'ad'
    elif (row['traffic_source'] == 'paid' or row['traffic_source'] == 'email') and row['region'] != 'Russia':
        return 'other'
    else:
        return row['traffic_source']

log['source_type'] = log.apply(source_type, axis=1)

print(log.head(50))