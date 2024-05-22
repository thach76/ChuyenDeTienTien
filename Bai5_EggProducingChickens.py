result = '''
GallusBreed: Giống gà, ví dụ như 'Buff Orpington chicken'.
Day: Một số nguyên cho biết ngày mà quan sát được thực hiện.
Age: Tuổi của con gà, tính bằng tuần.
GallusWeight: Trọng lượng của con gà, tính bằng gam.
GallusEggColor: Màu sắc của quả trứng.
GallusEggWeight: Trọng lượng của quả trứng, tính bằng gam.
AmountOfFeed: Lượng thức ăn (tính bằng gam) mà con gà tiêu thụ trong một ngày.
EggsPerDay: Số lượng trứng mà một con gà đẻ trong một ngày cụ thể.
GallusCombType: mô tả loại mào của gà
SunLightExposure: Số giờ mà một con gà được tiếp xúc với ánh sáng tự nhiên (ánh nắng mặt trời) trong một ngày.
GallusClass: Các lớp gà được phân loại bởi các hiệp hội gia cầm quốc tế.
GallusLegShanksColor: Màu sắc của chân và ống chân của con gà.
GallusBeakColor: Màu sắc của mỏ gà.
GallusEarLobesColor: Màu sắc của vành tai của con gà.
GallusPlumage: Màu sắc của lông vũ trên cơ thể con gà.

có 15 trường và 1000 mẫu

         Age  GallusWeight  GallusEggWeight  EggsPerDay  AmountOfFeed
Min    24.00       1500.00          30.0800       0.000        100.00
Max   990.00       3000.00          58.9300       1.000        129.00
Mean  522.01       2217.85          43.4271       0.965        116.25

Số lượng mẫu gà có trứng màu Brown và trọng lượng trên 3000: 0
Số lượng mẫu gà có trứng màu Brown và Age trên 800: 220
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def writeFile(filepath, data):
    with open(file=filepath, mode='w+', encoding='utf-8', errors='ignore') as f:
        f.write(data)

# Load dữ liệu
data = pd.read_csv(r"E:\Data\DeCuongOnTap\ChuyenDeTienTien\Bai5_Egg Producing Chickens\GallusGallusDomesticus.csv")

#Bai 2
# Lọc các cột cần tính toán
cols_to_analyze = ['Age', 'GallusWeight', 'GallusEggWeight', 'EggsPerDay', 'AmountOfFeed']

# Lọc các cột có kiểu dữ liệu số
numeric_cols = data[cols_to_analyze].select_dtypes(include=['number']).columns

# Tạo DataFrame từ các giá trị tối thiểu, tối đa và trung bình
summary_table = pd.DataFrame({'Min': data[numeric_cols].min(),
                               'Max': data[numeric_cols].max(),
                               'Mean': data[numeric_cols].mean()},
                              index=numeric_cols)

# Hiển thị bảng với các thuộc tính nằm theo hàng ngang (chuyển vị)
summary_table_transposed = summary_table.transpose()
print(summary_table_transposed)


#Bài 3
# 3a. Mẫu gà trên có trứng màu Brown và trọng lượng trên 3000
brown_eggs_over_3000 = data.query("GallusEggColor == 'Brown' and GallusWeight > 3000")
print(f"Số lượng mẫu gà có trứng màu Brown và trọng lượng trên 3000: {len(brown_eggs_over_3000)}")

# 3b. Mẫu gà trên có trứng màu Brown và Age trên 800
brown_eggs_age_over_800 = data.query("GallusEggColor == 'Brown' and Age > 800")
print(f"Số lượng mẫu gà có trứng màu Brown và Age trên 800: {len(brown_eggs_age_over_800)}")


writeFile(r"E:\Data\DeCuongOnTap\ChuyenDeTienTien\Bai5_Egg Producing Chickens\ketqua.txt", result)

# Bài 4
# Tạo 4 biểu đồ trên cùng một hình
fig, axs = plt.subplots(2, 2, figsize=(15, 7))

# 4a. Age với GallusEggWeight
axs[0, 0].scatter(data['Age'], data['GallusEggWeight'], color='r', alpha=0.5)
axs[0, 0].set_xlabel('Age')
axs[0, 0].set_ylabel('GallusEggWeight')
axs[0, 0].set_title('Age với GallusEggWeight')

# 4b. Age với GallusWeight
axs[0, 1].scatter(data['Age'], data['GallusWeight'], color='g', alpha=0.5)
axs[0, 1].set_xlabel('Age')
axs[0, 1].set_ylabel('GallusWeight')
axs[0, 1].set_title('Age với GallusWeight')

# 4c. Age với EggsPerDay
axs[1, 0].scatter(data['Age'], data['EggsPerDay'], color='b', alpha=0.5)
axs[1, 0].set_xlabel('Age')
axs[1, 0].set_ylabel('EggsPerDay')
axs[1, 0].set_title('Age với EggsPerDay')

# 4d. GallusEggWeight với AmountOfFeed
axs[1, 1].scatter(data['GallusEggWeight'], data['AmountOfFeed'], color='m', alpha=0.5)
axs[1, 1].set_xlabel('GallusEggWeight')
axs[1, 1].set_ylabel('AmountOfFeed')
axs[1, 1].set_title('GallusEggWeight với AmountOfFeed')

# Điều chỉnh khoảng cách giữa các biểu đồ
plt.tight_layout()

# Hiển thị biểu đồ
plt.show()
