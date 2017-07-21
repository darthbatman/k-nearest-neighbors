from scipy.spatial import distance

class KNN():
	def fit(self, x_train, y_train):
		self.x_train = x_train
		self.y_train = y_train

	def predict(self, x_test):
		predictions = []
		for row in x_test:
			label = self.closest(row)
			predictions.append(label)
		return predictions

	def closest(self, row):
		closest_distance = distance.euclidean(row, self.x_train[0])
		closest_index = 0
		for i in range(1, len(self.x_train)):
			if distance.euclidean(row, self.x_train[i]) < closest_distance:
				closest_distance = distance.euclidean(row, self.x_train[i])
				closest_index = i
		print self.y_train[closest_index]
		return self.y_train[closest_index]

import random

x = []
y = []

for i in range(0, 10000):
	randomTPH = random.randint(1, 120)
	randomC = random.randint(1, 6)
	randomV = random.randint(1, 20000)
	meaninglessRandomValueOne = random.randint(-13121, 1231)
	meaninglessRandomValueTwo = random.randint(0, 1839)
	meaninglessRandomValueThree = random.randint(312, 316)
	meaninglessRandomValueFour = random.randint(0, 1)
	x.append([randomTPH, randomC, randomV, meaninglessRandomValueOne, meaninglessRandomValueTwo, meaninglessRandomValueThree, meaninglessRandomValueFour])
	if randomTPH > 60:
		y.append(1)
	elif randomV >= 10000:
		y.append(1)
	else:
		y.append(0)

from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.5)

my_classifier = KNN()

my_classifier.fit(x_train, y_train)

predictions = my_classifier.predict(x_test)
print x_test
print predictions

from sklearn.metrics import accuracy_score
print accuracy_score(y_test, predictions)
