import numpy as np
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
Y = np.array([1, 1, 1, 2, 2, 2])
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(X, Y)
GaussianNB(priors=None)
pred=clf.predict([[-0.8, -1]]).reshape(1,-1)
print(pred)

labels_test = np.array([[1]])

#准确度评估 评估正确/总数  
#方法1  
#accuracy = clf.score(pred, labels_test)  
#方法2  
from sklearn.metrics import accuracy_score  
accuracy2 = accuracy_score(pred,labels_test)

#print(accuracy)
print(accuracy2)

