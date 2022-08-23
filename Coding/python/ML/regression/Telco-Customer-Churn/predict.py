import pandas as pd
import matplotlib as plt
import numpy as np
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("./Telco-Customer-Churn.csv")

#zzz 결측치 확인
#데이터 확인
print(df.info)
print(df.columns)

#데이터 전처리: 사용하지 않는 컬럼 없애기

#zzz
#데이터 전처리: 텍스트를 정형데이터로 변환
df.replace(['Yes'], 1, inplace=True)
df.replace(['No'], 0, inplace=True)
df['column name'].value_counts() #각 컬럼별 값 확인 후 결측치 NA로 변환

print(df)

#예측할 목적변수(churn)를 데이터에서 분리
train_x = df.drop(['Churn'], axis=1)
train_y = df['Churn']

#학습 데이터와 검증 데이터 나누기(전처리된 데이터) + 목적변수(churn)을 분리
#train: 학습 데이터, train_predict: 학습 데이터의 목적변수, test: 검증 데이터, test_predict: 검증 데이터의 목적변수
kf=KFold(n_splits=4, shuffle=True, random_state=71)
tr_idx, va_idx = list(kf.split(train_x))[0]
train, test = train_x.iloc[tr_idx], train_x.iloc[va_idx]
train_predict, test_predict = train_y.iloc[tr_idx], train_y.iloc[va_idx]

#학습 데이터 시각화

#모델 분석

#검증 데이터와 비교