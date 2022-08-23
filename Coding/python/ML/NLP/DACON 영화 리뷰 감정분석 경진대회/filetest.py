import pandas as pd

import module.checkPreference as checkPreference
import module.checkData as checkData

# road csv datas
# train: 학습용 데이터 / test: 실제 데이터 / submission: 제출용 label
train = pd.read_csv("./dataset/train.csv")
test = pd.read_csv("./dataset/test.csv")
submission = pd.read_csv("./dataset/sample_submission.csv")

# check the preference
checkPreference.route()
checkPreference.csvRoad(train, 5)
checkPreference.csvRoad(test, 5)

# check the shape of data
checkData.shape(train)
checkData.shape(test)
checkData.nameofcolumn(train)
checkData.nameofcolumn(test)

# find duplication in csv data
# z 라벨 이름을 알아내서 핸들링하는 방법?
print("find duplication about train data\n")
checkData.kinds(train, 'document')
checkData.kinds(train, 'label')

print("find duplication about test data\n")
checkData.kinds(test, 'document')

# check missing value
print("count missing value of train data\n")
checkData.missingValue(train)
print("\ncount missing value of test data\n")
checkData.missingValue(test)