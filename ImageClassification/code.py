# --------------
# Importing the neccessary packages

import numpy as np 
import cv2

from matplotlib import pyplot as plt

#load the image using opencv
image = cv2.imread(path)

#convert the above image into grayscale
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Now we split the image to 5000 cells, each 20x20 size
cells = [np.hsplit(row, 100) for row in np.vsplit(image_gray, 50)]

cells_array = np.array(cells)


# --------------
# Code starts here
# Preparation of training data and testing data
train_data = cells_array[:, : 50].reshape(-1, 400).astype(np.float32)

test_data = cells_array[:, 50:100].reshape(-1, 400).astype(np.float32)


# creating labels for train and test data

labels = np.arange(10)
train_labels = np.repeat(labels, 250)[:, np.newaxis]

test_labels = train_labels.copy()


# Instatiate the KNN model, train the data 
knn = cv2.ml.KNearest_create()
knn.train(train_data, cv2.ml.ROW_SAMPLE, train_labels)

# testing the model on test data
_, result,_,_ = knn.findNearest(test_data, k=5)

no_of_matches = result == test_labels
correct_matches = np.count_nonzero(no_of_matches)
accuracy = (correct_matches/result.size)*100

print(accuracy)

# save the knn model
save_path = user_data_dir + "knn_data.npz"

np.savez(save_path, train= train_data, train_labels= train_labels)


# Code Ends here




# --------------
# load the saved model 

with np.load(save_path) as data:
    train = data['train']
    train_labels = data['train_labels']

knn_saved = cv2.ml.KNearest_create()
knn_saved.train(train, cv2.ml.ROW_SAMPLE, train_labels) 
  
test_img=cv2.imread(path1)
test_img_gray =cv2.cvtColor(test_img,cv2.COLOR_BGR2GRAY)
blur_sg = cv2.GaussianBlur(test_img_gray, (5,5), 0)
(T, th) =cv2.threshold(blur_sg, 155, 255, cv2.THRESH_BINARY_INV)

th = th[400:880, 200:750]
test_img_resize =cv2.resize(th, (20, 20)) 
x = np.array(test_img_resize)
test_img_reshape = x.reshape(-1,400).astype(np.float32)
_,result,_,_ = knn_saved.findNearest(test_img_reshape,k=1)


fig, ax = plt.subplots(nrows = 1, ncols = 2, figsize=(15, 7))
ax[0].imshow(test_img)
ax[0].title.set_text('Orignal Image')

ax[1].imshow(test_img_resize, 'gray')
ax[1].title.set_text('Preprocessed Image')
fig.show();
#Print the predicted number 
print(int(result))


# --------------
def deskew(input_image):
    SZ = 20
    m = cv2.moments(input_image)
    
    if abs(m['mu02']) < 1e-2:
        # no need of deskewing.
        return input_image.copy()
    skew = m['mu11']/m['mu02']
    M = np.float32([[1, skew, -0.5 * SZ * skew], [0, 1, 0]])
    
    deskewed_image = cv2.warpAffine(input_image, M, (SZ, SZ), flags= cv2.WARP_INVERSE_MAP |  cv2.INTER_LINEAR)
    return deskewed_image


# --------------
def hog_descriptor(input_image):
    bin_n = 16
    g_x = cv2.Sobel(input_image, cv2.CV_32F, 1, 0) # derivative in x - direction.
    g_y = cv2.Sobel(input_image, cv2.CV_32F, 0, 1) # derivative in y - direction.
    
    magnitude, angle = cv2.cartToPolar(g_x, g_y)
    
    hist_bins = np.int32(bin_n * angle / (2 * np.pi)) # quantizing binvalues in (0....16)
    angle_cells = hist_bins[:10, :10], hist_bins[10:,:10], hist_bins[:10,10:], hist_bins[10:,10:]
    mag_cells = magnitude[:10,:10], magnitude[10:,:10], magnitude[:10,10:], magnitude[10:,10:]
    hists = [np.bincount(b.ravel(), m.ravel(), bin_n) for b, m in zip(angle_cells, mag_cells)]
    hist = np.hstack(hists)     # hist is a 64 bit vector
    
    return hist


# --------------
# code starts here

train_data = [ i[:50] for i in cells ]
test_data = [ i[50:] for i in cells]
deskewed_train = [list(map(deskew, row)) for row in train_data]
hog_desc_train = [list(map(hog_descriptor, row)) for row in deskewed_train]

deskewed_test = [list(map(deskew,row)) for row in test_data]
hog_desc_test = [list(map(hog_descriptor,row)) for row in deskewed_test]

svm_train_data = np.float32(hog_desc_train).reshape(-1,64)
responses = np.repeat(np.arange(10),250)[:,np.newaxis]


svm_test_data = np.float32(hog_desc_test).reshape(-1, 64)


svm_model = cv2.ml.SVM_create()
svm_model.setKernel(cv2.ml.SVM_LINEAR)
svm_model.setType(cv2.ml.SVM_C_SVC)
svm_model.setC(2.67)
svm_model.setGamma(5.383)
svm_model.train(svm_train_data, cv2.ml.ROW_SAMPLE, responses)
save_path1 = user_data_dir + "svm_data.dat"
svm_model.save(save_path1)
result = svm_model.predict(svm_test_data)[1]

mask = result==responses
correct = np.count_nonzero(mask)
print(correct*100.0/result.size)

# code ends here


# --------------
""" After filling and submitting the feedback form, click the Submit button of the codeblock"""


