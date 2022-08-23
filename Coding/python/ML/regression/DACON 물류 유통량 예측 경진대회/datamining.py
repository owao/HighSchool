import pandas as pd

import module.checkPreference as checkPreference
import module.checkData as checkData

train = pd.read_csv('./train.csv')
test = pd.read_csv('./test.csv')
submission = pd.read_csv('sample_submission.csv')

print(train)