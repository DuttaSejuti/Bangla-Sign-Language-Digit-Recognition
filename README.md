# Bangla-Sign-Language-Digit-Recognition-using-CNN
This is a final project that is done for my last semester of graduation from JU. It is a SLR that can detect bangla 0-9 sign digits from real time video.  

## Requirements
  1. Tensorflow 2.4.1
  2. python 3.8.6
  3. can run without GPU support
  
  
  #### collect-data.py
  this file collects data from the user to create a dataset. After running this file a window will pop up and for each digit click the corresponding button.For example: for collecting data of 1;after positioning the hand click 1 and a picture of the hand will be stored in the corresponding folder.
  
  #### flip-images.py
  this file will flip each images of the dataset for each class of the dataset.
  
  #### display-all-gestures.py
  this file creates an image file showing random picture of the sample images for each class.
  
  #### train1.py
  this file simply train the model.
  
  #### predict1.py
  this file predicts the signs from the user and shows the correnponding digit.
  
  
  

