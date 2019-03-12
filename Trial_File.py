#Begin Tejas
import json
with open("Data/Patient1_JSON.json", "r") as read_file:
    patient_data = json.load(read_file)

#print(type(data))
#print(data['1'])
#print(data['2'])
#print(data['3'])

ls_ptype = []
ls_ptype_weight = []
ls_ptype_seq = []
ls_ptype_los = []
for each_patient in patient_data.items():
    #print(each_patient[0])  # Each row Key
    #print(each_patient[1]['ptype_num'])  # Each Row Value
    #ls_ptype.append(each_patient[1]['ptype_num'])
    ls_ptype.append(each_patient[0])
    ls_ptype_seq.append(each_patient[1]['sequence'])
    ls_ptype_weight.append(each_patient[1]['probability'])
    ls_ptype_los.append(each_patient[1]['los'])


print(ls_ptype)
print(ls_ptype_seq)
print(ls_ptype_weight)
print(ls_ptype_los)
print(patient_data['1']['sequence'])

route_length = len(patient_data['2']['sequence']) - 1
print(route_length)

planned_route_stop = [None]
#planned_route_stop.append(None)
planned_route_stop +=  patient_data['2']['sequence']
print(planned_route_stop)
