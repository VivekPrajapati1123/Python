dict1 = {1:2,2:3,3:4}
dict2 = {4:5,5:6,6:7}
dict3 = {8:9,9:10,11:12}
dict4 = {13:14,15:16,17:18}
dict5 = {}
for i in (dict1,dict2,dict3,dict4):
    dict5.update(i)
print(dict5)