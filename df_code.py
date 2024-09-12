#활용 데이터 : 통계청, 2024 시도별 종별 요양기관 현황
# 수도권vs.지방 의료 혜택의 격차를 파악하고자 함 
# 지역별로 병원과 정신병원 수가 적은 상위 10개 지역이 시각화된 막대 그래프
# 각각의 병원과 정신병원 수는 색깔을 달리해 구분
#

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 데이터 불러오기 (CSV 또는 Excel 파일로 가정)
data = pd.read_csv('hospital_data.csv')
# 또는 엑셀 파일인 경우
# data = pd.read_excel('hospital_data.xlsx')

# 데이터 확인
print(data.head())

# 필요 열 선택
df = data[['지역명', '병원 수', '정신병원 수']]

# 결측치 확인 및 처리 (결측치가 있다면 0으로 채우기)
df.fillna(0, inplace=True)

# 총 병원 수 계산
df['총 병원 수'] = df['병원 수'] + df['정신병원 수']

# 병원 수가 적은 지역 정렬 및 상위 10개 지역 선택
least_hospitals = df.sort_values(by='총 병원 수').head(10)
print(least_hospitals)

# 시각화: 막대 그래프
plt.figure(figsize=(10,6))

# 병원 수와 정신병원 수를 따로 시각화
plt.barh(least_hospitals['지역명'], least_hospitals['병원 수'], color='blue', label='병원 수')
plt.barh(least_hospitals['지역명'], least_hospitals['정신병원 수'], left=least_hospitals['병원 수'], color='red', label='정신병원 수')

plt.xlabel('병원 및 정신병원 수')
plt.ylabel('지역명')
plt.title('병원 및 정신병원이 가장 적은 지역 분포')
plt.legend()

plt.show()
