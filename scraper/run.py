import json
from pprint import pprint

dic = {}
with open('datas.json') as data_file:
    data = json.load(data_file)
    lst = []
    n=0
    print len(data)
    for  i in data:
        # print i
        dic[i] = "/".join(data[i]['items'])

c=0
st=""
new_dict={}
check = ["normal","opacity", "cardiomegaly","calcinosis", "lung/hypoinflation","calcified granuloma","thoracic vertebrae/degenerative", "lung/hyperdistention", "spine/degenerative ","catheters, indwelling", "granulomatous disease", "nodule","surgical instruments","scoliosis", "spondylosis"]
for j in dic:
#     print dic[j]
    #     st = st + j
    for i in check:

        if i in dic[j].lower():
            st+=i
#             if i=="nodule":
#                 st="nodule"
#                 break
        
    if st == "":
        st += "missing"
    new_dict[j] = st
    
    st=""
    
#     if "opacity" in dic[j].lower():
#         print dic[j].lower()
#         c+=1
# print c
# print new_dict        

from collections import Counter
c = Counter( (new_dict.values()) )

# print c.items()
c.items().sort(key=lambda x: x[0])
c = dict(c)
print len(c)

from operator import itemgetter
sort = sorted(c.items(), key=itemgetter(1))
# print sort[-40:]
# print sort

labels = sorted([i for i in sort[-4:] if i[0]!="missing"], key=lambda x: x[1])
print labels

from collections import defaultdict

index_list = defaultdict(list)

for key, value in new_dict.iteritems():
    index_list[value].append(key)

train_images_dict = {}
test_images_dict={}
for  i in index_list:
#     print i
    if i== "normal":
        train_images_dict["normal"]=index_list[i][400:500]
        test_images_dict["normal"] = index_list[i][500:550]
#     elif i=="opacity":
#         train_images_dict["abnormal"]=index_list[i][:354]
#         test_images_dict["abnormal"] = index_list[i][354:374]
#     elif i=="cardiomegaly":
#         train_images_dict["abnormal"]=index_list[i][:251]
#         test_images_dict["abnormal"] = index_list[i][251:266]
#     elif i=="lung/hypoinflation":
#         train_images_dict["abnormal"]=index_list[i][:229]
#         test_images_dict["abnormal"] = index_list[i][229:249]
#     elif i=="calcified granuloma":
#         train_images_dict["abnormal"]+=index_list[i][:243]
#         test_images_dict["abnormal"] += index_list[i][243:263]
#     elif i=="thoracic vertebrae/degenerative":
#         train_images_dict["abnormal"]+=index_list[i][:218]
#         test_images_dict["abnormal"] += index_list[i][218:238]
#     elif i=="lung/hyperdistention":
#         train_images_dict["abnormal"]+=index_list[i][:190]
#         test_images_dict["abnormal"] += index_list[i][190:210]
#     elif i=="surgical instruments":
#         train_images_dict["abnormal"]+=index_list[i][:71]
#         test_images_dict["abnormal"] += index_list[i][71:86]
#     elif i=="catheters, indwelling":
#         train_images_dict["abnormal"]+=index_list[i][:100]
#         test_images_dict["abnormal"] += index_list[i][100:112] 
#     elif i=="calcinosis":
#         train_images_dict["abnormal"]+=index_list[i][:146]
#         test_images_dict["abnormal"] += index_list[i][146:166] 
    
    elif i=="nodule" :
        train_images_dict[i]=index_list[i][:54]
        test_images_dict[i] = index_list[i][49:]
    elif i=="calcinosisnodule":
        train_images_dict["nodule"]+=index_list[i][:23]
        test_images_dict["nodule"] += index_list[i][23:]

len(test_images_dict["normal"])

# c=0
# label_dict = {}
# for i in labels[-1::-1]:
# #     print i[0]
#     label_dict[i[0]] = c
#     c+=1
label_dict = {"normal":0,"nodule":1}
print label_dict       

import numpy as np
label_index={}
for i in label_dict:
    a = np.zeros(2)
    a[label_dict[i]]=1
    label_index[i] = a
print label_index

for i in label_index:
    print i
    print label_index[i]

new_image_dict={}
for i in new_dict:
    if new_dict[i] in label_index.keys():
        new_image_dict[i] = label_index[new_dict[i]]

new_image_dict={}
for i in new_dict:
    if new_dict[i] =="normal":
        new_image_dict[i] = np.array([1,0])
    else:
        new_image_dict[i] = np.array([0,1])

print len(new_image_dict)                    

import shutil,os
os.chdir('D:\labswork\Xvision\DeepLearning')

#trainign image list
train_list=[]
test_list=[]
for  i in train_images_dict:
    train_list +=train_images_dict[i]
for  i in test_images_dict:
    test_list +=test_images_dict[i]
print len(train_list)

from random import shuffle

shuffle(train_list)
shuffle(test_list)

len(test_list)
len(train_list)
# print("test list length")
# len(test_list)
# print("train list length")
# len(train_list)
# print("This is train list")
# print(train_list)
# print("This is test list")
# print(test_list)
#copy training data
c=0
train_label={}

# os.mkdir("D://labswork/Xvision/DeepLearning/final_train_images_calc_nodule_only")
for i in train_list:
    print i 
    print "this is train val"
    shutil.copy('D://labswork/Xvision/data/'+str(i)+'.png', 'D://labswork/Xvision/DeepLearning/final_train_images_calc_nodule_only/'+str(c)+'.png')
    train_label[c] = new_image_dict[i]
    c+=1

#copy teasting data
c=0
test_label={}

# os.mkdir("D://labswork/Xvision/DeepLearning/final_test_images_calc_nodule_only")
for i in test_list:
	print i 
	print "this is test val"
	shutil.copy('D://labswork/Xvision/data/'+str(i)+'.png', 'D://labswork/Xvision/DeepLearning/final_test_images_calc_nodule_only/'+str(c)+'.png')
	test_label[c] = new_image_dict[i]
	c+=1    

import pickle
import numpy as np
filename = "training_labels_calc_nodule_only"

fileObject = open(filename,'wb') 
pickle.dump(np.array(train_label.values()),fileObject)
fileObject.close()	

filename = "testing_labels_calc_nodule_only"

fileObject = open(filename,'wb') 
pickle.dump(np.array(test_label.values()),fileObject)
fileObject.close()