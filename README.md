# Xvision

Chest Xray image analysis using **Deep Learning** and  exploiting **Deep Transfer Learning** technique for it with Tensorflow.

The **maxpool-5** layer of a pretrained **VGGNet-16(Deep Convolutional Neural Network)** model has been used as the feature extractor here and then further trained on a **2-layer Deep neural network** with **SGD optimizer** and **Batch Normalization** for classification of **Normal vs Nodular** Chest Xray Images.

## Nodular vs Normal Chest Xray
<img src="https://github.com/ayush1997/Xvision/blob/master/image/node.jpg" width="300" height="300" />
<img src="https://github.com/ayush1997/Xvision/blob/master/image/normal.jpg" width="300" height="300" />

## Some specifications

| Property      |Values         |
| ------------- | ------------- |
| Pretrained Model | VggNet-16  |
| Optimizer used  | stochastic gradient descent(SGD)  |
| Learning rate  | 0.01|  
|Mini Batch Size| 20 |
| Epochs | 20 |
|2 Layers| 512x512 |
|GPU trained on| Nvidia GEFORCE 920M|

## Evaluation
### Confusion Matrix and Training Error Graph

<img src="https://github.com/ayush1997/Xvision/blob/master/image/cfm.jpg" width="450" height="400" />
<img src="https://github.com/ayush1997/Xvision/blob/master/image/nodule.jpg" width="400" height="400" />

|     |  **Normal** | **Nodule** |
|------|---------|---------|
| **Precision**| 0.7755102| 0.55555556 |
|**Recall**| 0.76 | 0.57692308 |

**Accuracy** : **69.3333 %**

## DataSet
[openi.nlm.nih.gov](https://openi.nlm.nih.gov/gridquery.php?q=&it=x,xg&sub=x&m=1&n=101) has a large base of Xray,MRI, CT scan images publically available.Specifically Chest Xray Images have been scraped, Normal and Nodule labbeled images are futher extrated for this task.

## How to use ?
The above code can be used for **Deep Transfer Learning** on any Image dataset to train using VggNet as the PreTrained network. 
### Steps to follow 

1. Download Data- the script download images and saves corresponding disease label in json format.

  ```python scraper.py <path/to/folder/to/save/images>```
  For eg python scraper.py "D://Xvision/data" ,this will save the images dataset into data folder of Xvision project.You can run python scraper.py parallely also to generate images set faster by giving the range from 0 to 75 or (0-30,30-50,50-75)or based on your preference to generate images fast.

2. Follow the ```scraper/process.ipynb``` notebook for Data processing and generate.You can refer run.py in scraper folder or follow the ```scraper/process.ipynb``` and run each step individually and generate the below dataset.All the steps of ```scraper/process.ipynb``` are done in run.py.You just need to change the folder destination based on your path.
After running run.py you should be able to generated below folders.

  * Training images folder - All images for training(Eg - final_train_images_calc_nodule_only(folder name))
  * Testing images Folder - All images for testing(Eg - final_test_images_calc_nodule_only(folder name))
  * Training image labels file - Pickled file with training labels(Eg - training_labels_calc_nodule_only(file name))
  * Testing image labels file - Pickled file with testing labels(Eg - testing_labels_calc_nodule_only(file name))

3. Extract features(**CNN Codes**) from the **maxpool:5** layer of PreTrained CovNet(VggNet) and save them beforehand for faster training of Neural network.

    ```python train.py <Training images folder> <Testing image folder> <Train images codes folder > <Test images codes folder>```

    For eg python train.py final_train_images_calc_nodule_only final_test_images_calc_nodule_only train-code test-code

4.  The extracted features are now used for training our **2-Layer Neural Network** from scratch.The computed models are saved as tensorflow checkpoint after every **Epoch**.

    ```python train_model.py <Training images folder> <Train images codes folder> <Training image labels file> <Folder to         save models>```

    For eg python train_model.py final_train_images_calc_nodule_only train-code training_labels_calc_nodule_only train-model

5.  Finally the saved models are used for making predictions.Confusion Matrix is used as the Performance Metrics for this classifcation task.

    ```python test_model.py final_test_images_calc_nodule_only test-code testing_labels_calc_nodule_only train-model```
    
    
    
## Some Predictions

![Alt text](https://github.com/ayush1997/Xvision/blob/master/image/pred.jpg "Optional Title")

## References

> 1. [Learning to Read Chest X-Rays: Recurrent Neural Cascade Model for Automated Image Annotation](https://arxiv.org/pdf/1603.08486.pdf)

> 2. [Deep Convolutional Neural Networks for Computer-Aided Detection: CNN Architectures,
Dataset Characteristics and Transfer Learning](https://arxiv.org/pdf/1602.03409.pdf)

## Contribute

If you want to contribute and add new feature feel free to send Pull request [here](https://github.com/ayush1997/Xvision/pulls) :D

To report any bugs or request new features, head over to the [Issues page](https://github.com/ayush1997/Xvision/issues)

## To-do

- [ ] Implement saliency map or use Deconv for better visualizations. 
