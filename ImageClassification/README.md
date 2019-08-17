### Project Overview

 Our data consists of 5000 handwritten digits (500 images for each digit) which is a 20 x 20 image. The dataset we will using is already available in OpenCV docs which is an image file named as digits.png.




### Learnings from the project

 Load the data and split it
You have been given the image which looks like the image given above that consists of 5000 images (500 for each digit) of dimension 20 x 20 stacked in one image such that 100 images are stacked in one single row and 50 images are stacked in one single column. Your task is to load the image and split all the images individually into train and test data.

Instruction
Load the file digits.png use the variable path and using cv2.imread functionality and save it in a variable named as image.

Convert the default image read in the above step to a grayscale image by using cv2.cvtColor function and save it as image_gray.

Since there are 5000 cells and we want to store them in an individual cell we can do this by using numpy horizontal and vertical split. Perform the numpy horizintal and vertical split the image_gray into 100 rows and 50 columns of images each containing a 20 x 20 handwritten image of digits.



Data Preparation along with model building and testing
Since we have split up each image into an array of single cell , now its time to prepare the data into two halves (Training and testing set of data). KNN will basically capture patterns from the training data and will build a model on top of it.

Instructions
Extract the 250 samples each for training and testing purposes and flatten each sample into a 20 X 20 = 400 single array of pixel intensities in the form of float32 values and save it in the variable train_data.

Extract the remaining 250 images which shall be used as testing data in a similar way as told above and save it in variable named as test_data.

Create the labels of the image digits.png in a similar fashion as they are arranged by creating a numpy array of these 10 digits ( name it as labels) and then repeating these integers across creating 250 labels for each digit and name that as train_labels which will be same for test_labels even.

Instantiate the knn model using opencv and store the model in the variable named as knn and train the model such that each training sample is a row of samples. Also, provide the train labels you have created above.

Find the 5 nearest neighbours on test data using k=5 and store the results in the variable named as result

Match the predicted results to true labels and store it in the variable named as no_of_matches.

Count the number of non-zero matches which can be stored as correct_matches. Find and save the accuracy in the variable accuracy . Print the accuracy when correct matches are compared against total size of the true labels.

Save the above knn model which consists of above training data as train_data and labels as train_labels and with a name as save_path. Note save_path variable is already defined for you with the data path.


Saving the trained model and observing the results
Instructions
Load the saved model(i.e. save_path) created above usign with functionality of python following loading and saving train data and labels as train and train_labels respectively.

Run the knn by instantiating it on the train data which takes each training sample as the row of samples and save it the variable named as knn_saved.

The image path is stored in variable path1 . Load the image and perform the neccessary image processing that is bringing a preferred resolution picture ( such as 1080p or 720p ) to a resized image of 20 X 20.

Preprocessing involves converting the orignal image to grayscale (save the variable named as test_image_gray)
Application of gaussian filter (save the variable named as blur_sg) and then applying thresholding
Crop the previous image (on which thresholding is applied) extracting the required digit from the image leaving the uneccessary background.
Resize the image matching the dimension of training images that is 20 x 20 and save it in the variable named as test_img_resize.
Convert test_img_resize into an array and save it as x
Flatten the resized image(i.e. x)into a single array of (1, 20 x 20) = (1, 400)(store that in a variable named as test_img_reshape) shape and predict the result using saved knn model above.

Create a subplot with 1 row and 2 columns and save it as fig, ax. Plot original test image using axis 0 and preprocessed i.e. resized image using axis 1.




### Approach taken to solve the problem

 Deskewing as preprocessing
Approach 2 :
KNN was an approach that used pixel intensity as the feature vector. In the previous chapter we have studied about the Histogram and the image gradients. What we can do here is make use of these gradients as the features.

Deskewing the images
What is deskewing?

A significant change in performance of the existing algorithms in computer vision is observed when you align the image in the same with reference image which essentially means Image deskewing.

While dealing with the dataset of handwritten images we need to align all images to a base level as there are variations in handwriting that goes from people to people hence we have to account for those slants, style of the digits that are written.

Deskewing as preprocessing
For deskewing we need to find image moments. Image moments are certain particular weighted average of the image pixels intensities. Image moments are useful for finding properties such as area(total intensity), centroid and information about its orientation.

Instructions
Define a function naming as deskew which takes parameter input_image input as image.

Define the size of the deskewed image as 20 and find the moments of the image using cv2.moments.

If the second order moment of the image is less than value 1e-2 then there is no need of deskewing the image. In that case return the copy of image.

Calculate the skewness of the image using the ratio of moments m['mu11'] and m['mu02']. Store it in the variable named as skew.

Create the transformation matrix which will be array of values that is [[1, skew, -0.5 * 20 * skew], [0, 1, 0]].

Use this above transformation matrix to transform the image using warpAffine on our input image given. Also the resulting size of the image should be matching with the default size of the input image.

Note - Flags which will be used in Affine transformation, cv2.WARP_INVERSE_MAP | cv2.INTER_LINEAR flags would be used during the affine transformation.



SVM model using HOG descriptor
Now that we have found out our new feature descriptors its time to use them as an input feeded onto an SVM model which would make some sense out of it and would predict the label.

We can also measure the percentage change of improvement or disimprovement in the prediction power of a machine learning model.

Instructions
Split the cells( which were containing individual image of digits that is created in the first task) into train and test data containing 250 and 250 images respectively. Save this train and test data as train_data and test_data respectively.

Make use of the function deskew and hog_descriptor by passing each row as a sample from the train_data and name it as deskewed_train and hog_desc_train. Do this same procedure with the testing set and save it as deskewed_test and hog_desc_test.

As we saw above each image was divided into 4 section of 10 x 10 window which finally resulted in 16 values of each region therby comprising 64 values for each image. Hence reshape the hog_desc_train and hog_desc_test data to (1, 64) of single array and save it as svm_train_data and svm_test_data

Instatiate the SVM model using cv2.ml.SVM_create.Set the following parameter as follows -

kernel : cv2.ml.SVM_LINEAR
type : cv2.ml.SVM_C_SVC
C value : 2.67
Gamma value : 5.383
Train the model such that each training sample is a row of samples. Also, provide the train labels you have created above. Predict the results using the svm_test_data and store the predicted outcomes in the variable called as result.

Match the predticted results to true labels and store it in the variable named as mask.

Count the number of non-zero matches which can be stored as correct. Find and print the accuracy when correct matches are compared against total size of the true labels.




