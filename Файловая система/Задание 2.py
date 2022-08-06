import json
pur_dict = {}

with open('Visit_log.csv') as log:
    with open('funnel.csv', 'w', encoding='utf-8') as out:
        purchase = open('purchase_log.txt', encoding='utf-8').readlines()
        for element in purchase:
            my_dict = json.loads(element)
            pur_dict.update({my_dict.values()})
        for line in log:
            line = line.strip().split(',')
            if line[0] in pur_dict.keys():
                out.write(line[0] + ',' + line[1] + ',' + str(pur_dict.get(line[0])) + '\n')