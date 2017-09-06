print("Permorming Step 1")
import json
from pprint import pprint

dic = {}
with open('datas.json') as data_file:
    data = json.load(data_file)
    lst = []
    n=0
    print (len(data))
    for  i in data:
        # print i
        dic[i] = "/".join(data[i]['items'])
print("Executed Step 1")

print("Permorming Step 2")
print("Labeling the data and forming a distionary")
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
print("Executed Step 2")

print("Permorming Step 3")
print("Calculate unique combinations of above diseases")
from collections import Counter
c = Counter( (new_dict.values()) )

# print c.items()
c.items().sort(key=lambda x: x[0])
c = dict(c)
print (len(c))
print("Executed Step 3")

print("Permorming Step 4")
print("The dictionary is sorted according to number of cases in each disease.")
from operator import itemgetter
sort = sorted(c.items(), key=itemgetter(1))
# print (sort[-40:])
# print (sort)
print("Executed Step 5")

print("Permorming Step 5")
print("Generating Labels.")
labels = sorted([i for i in sort[-4:] if i[0]!="missing"], key=lambda x: x[1])
print (labels)
print("Executed Step 5")

print("Permorming Step 6")
print("Dictionary with list of indexes of every disease")
from collections import defaultdict

index_list = defaultdict(list)

for key, value in new_dict.iteritems():
    index_list[value].append(key)
print("Executed Step 6")

print("Permorming Step 7")
print("Dictionary with list of indexes of every disease")
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
print("Executed Step 7")

print("Permorming Step 8")
print("Length of test images")
print(len(test_images_dict["normal"]))
print(len(test_images_dict["nodule"]))
print("Executed Step 8")

print("Permorming Step 9")
print("Encoding the classes")
# c=0
# label_dict = {}
# for i in labels[-1::-1]:
# #     print i[0]
#     label_dict[i[0]] = c
#     c+=1
label_dict = {"normal":0,"nodule":1}
print (label_dict)
print("Executed Step 9")

print("Permorming Step 10")
print("Numpy Array Classes")
import numpy as np
label_index={}
for i in label_dict:
    a = np.zeros(2)
    a[label_dict[i]]=1
    label_index[i] = a
print (label_index)
print("Executed Step 10")

print("Permorming Step 11")
print("Printing Numpy Array Classes One by One")
for i in label_index:
    print i
    print (label_index[i])
print("Executed Step 11")

print("Permorming Step 12")
new_image_dict={}
for i in new_dict:
    if new_dict[i] in label_index.keys():
        new_image_dict[i] = label_index[new_dict[i]]
print("Executed Step 12")

print("Permorming Step 13")
new_image_dict={}
for i in new_dict:
    if new_dict[i] =="normal":
        new_image_dict[i] = np.array([1,0])
    else:
        new_image_dict[i] = np.array([0,1])
print (len(new_image_dict))        
print("Executed Step 13")

print("Permorming Step 14")
print("trainign image list")
train_list=[]
test_list=[]
for  i in train_images_dict:
    train_list +=train_images_dict[i]
for  i in test_images_dict:
    test_list +=test_images_dict[i]
print (len(train_list))
print("Executed Step 14")

print("Permorming Step 15")
print("Shuffling train list and test list to get random data of train and test")
from random import shuffle

shuffle(train_list)
shuffle(test_list)

# for  i in train_list:
#     print new_dict[i]
# for i in train_list:
#     print new_dict[i]
print (len(test_list))
print("Executed Step 15")


print("Permorming Step 16")
print("Folder with all training images is formed")
#copy training data
import config as cfg
import os
import shutil, sys 
c=0
train_label={}
print(os.path.isdir(cfg.config['train-images']))
checkTrainImageExists = os.path.isdir(cfg.config['train-images'])

if (checkTrainImageExists == False):
	os.mkdir(cfg.config['train-images'])

for i in train_list:
#     print i
    
    shutil.copy(cfg.config['data']+i+'.png', cfg.config['train-images']+str(c)+'.png')
    train_label[c] = new_image_dict[i]
    c+=1
print len(train_label)    
print("Executed Step 16")

print("Permorming Step 17")
print("Folder with all testing images in made")
#copy testing data
#copy teasting data
c=0
test_label={}
print(os.path.isdir(cfg.config['test-images']))
checkTestImageExists = os.path.isdir(cfg.config['test-images'])

if (checkTestImageExists == False):
	os.mkdir(cfg.config['test-images'])

for i in test_list:
    shutil.copy(cfg.config['data']+i+'.png', cfg.config['test-images']+str(c)+'.png')
    test_label[c] = new_image_dict[i]
    c+=1
print len(test_label)    
print("Executed Step 17")

print("Permorming Step 18")
print("All the training and testing labels are stored as Pickled files")
import pickle
import numpy as np
filename = cfg.config['train-label']

fileObject = open(filename,'wb') 
pickle.dump(np.array(train_label.values()),fileObject)
fileObject.close()

filename = cfg.config['test-label']

fileObject = open(filename,'wb') 
pickle.dump(np.array(test_label.values()),fileObject)
fileObject.close()
print("Executed Step 18")