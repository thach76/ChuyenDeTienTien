result = '''
MODEL: Năm sản xuất của xe.
MAKE: Hãng sản xuất xe.
MODEL: Tên model của xe.
VEHICLE CLASS: Phân loại xe (Compact, Mid-size, SUV, ...).
ENGINE_SIZE: Dung tích xi-lanh của động cơ (lít).
CYLINDERS: Số xi-lanh của động cơ.
TRANSMISSION: Loại hộp số (A4: Tự động 4 cấp, M5: Số sàn 5 cấp, AS5: Tự động 5 cấp, ...).
FUEL: Loại nhiên liệu (X: Xăng, Z: Xăng cao cấp).
FUEL_CONSUMPTION*: Mức tiêu thụ nhiên liệu
    Cột đầu tiên    City (L/100 km): Mức tiêu thụ nhiên liệu trong điều kiện lái xe trong thành phố.
    Cột thứ hai     Highway (L/100 km): Mức tiêu thụ nhiên liệu trong điều kiện lái xe trên đường cao tốc.
    Cột thứ ba      Combined (L/100 km): Mức tiêu thụ nhiên liệu kết hợp giữa lái xe trong thành phố và trên đường cao tốc.
    Cột thứ tư      Combined (mpg): Mức tiêu thụ nhiên liệu kết hợp, chuyển đổi sang đơn vị miles per gallon (mpg).
CO2_EMISSIONS: Lượng khí thải carbon dioxide (g/km).

có 13 trường và 679 mẫu

      ENGINE_SIZE  CYLINDERS  FUEL_CONSUMPTION* City  FUEL_CONSUMPTION* Highway  FUEL_CONSUMPTION* Combined_L100km  FUEL_CONSUMPTION* Combined_mpg  CO2_EMISSIONS
Min      1.000000   3.000000                  4.9000                   4.000000                           4.500000                       14.000000     104.000000
Max      8.000000  12.000000                 23.2000                  18.000000                          20.800000                       63.000000     478.000000
Mean     3.252577   5.798233                 14.5919                  10.613844                          12.802798                       23.107511     293.656848
Số lượng mẫu xe có 4 xi lanh và có phát thải CO2 trên 200: 184
Số lượng mẫu xe có kích cỡ động cơ dưới 2.0 mà tiêu thụ nhiên liệu dưới 9: 17
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
data = pd.read_csv(r"E:\Data\DeCuongOnTap\ChuyenDeTienTien\Bai6_Emissions by Cars\Sample.csv")

#Bai 2
data['FUEL_CONSUMPTION* City'] = data.iloc[:, 8].copy()
data['FUEL_CONSUMPTION* Highway'] = data.iloc[:, 9].copy()
data['FUEL_CONSUMPTION* Combined_L100km'] = data.iloc[:, 10].copy()
data['FUEL_CONSUMPTION* Combined_mpg'] = data.iloc[:, 11].copy()
# Lọc các cột cần tính toán
cols_to_analyze = ['ENGINE_SIZE', 'CYLINDERS', 'FUEL_CONSUMPTION* City' , 'FUEL_CONSUMPTION* Highway', 'FUEL_CONSUMPTION* Combined_L100km', 'FUEL_CONSUMPTION* Combined_mpg', 'CO2_EMISSIONS']

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
# 3a. Mẫu xe có 4 xi lanh và có phát thải CO2 trên 200
four_cylinders_co2_over_200 = data.query("CYLINDERS == 4 and CO2_EMISSIONS > 200")
print(f"Số lượng mẫu xe có 4 xi lanh và có phát thải CO2 trên 200: {len(four_cylinders_co2_over_200)}")

# 3b. Mẫu xe có kích cỡ động cơ dưới 2.0 mà tiêu thụ nhiên liệu dưới 9
small_engine_low_consumption = data.query("ENGINE_SIZE < 2.0 and `FUEL_CONSUMPTION*` < 9")
print(f"Số lượng mẫu xe có kích cỡ động cơ dưới 2.0 mà tiêu thụ nhiên liệu dưới 9: {len(small_engine_low_consumption)}")


writeFile(r"E:\Data\DeCuongOnTap\ChuyenDeTienTien\Bai6_Emissions by Cars\ketqua.txt", result)

# Bài 4
# Tạo lưới 2x2 subplot
fig, axs = plt.subplots(2, 2, figsize=(15, 7))

# Danh sách các màu sẽ sử dụng cho từng biểu đồ
colors = ['r', 'g', 'b', 'm']  # Màu đỏ, xanh lá, xanh dương, tím

# 4a. CO2_EMISSIONS với ENGINE_SIZE
axs[0, 0].scatter(data['ENGINE_SIZE'], data['CO2_EMISSIONS'], alpha=0.5, c=colors[0])
axs[0, 0].set_title('CO2_EMISSIONS với ENGINE_SIZE')
axs[0, 0].set_xlabel('ENGINE_SIZE')
axs[0, 0].set_ylabel('CO2_EMISSIONS')

# 4b. CO2_EMISSIONS với FUEL_CONSUMPTION
axs[0, 1].scatter(data['FUEL_CONSUMPTION*'], data['CO2_EMISSIONS'], alpha=0.5, c=colors[1])
axs[0, 1].set_title('CO2_EMISSIONS với FUEL_CONSUMPTION')
axs[0, 1].set_xlabel('FUEL_CONSUMPTION*')
axs[0, 1].set_ylabel('CO2_EMISSIONS')

# 4c. CO2_EMISSIONS với CYLINDERS
axs[1, 0].scatter(data['CYLINDERS'], data['CO2_EMISSIONS'], alpha=0.5, c=colors[2])
axs[1, 0].set_title('CO2_EMISSIONS với CYLINDERS')
axs[1, 0].set_xlabel('CYLINDERS')
axs[1, 0].set_ylabel('CO2_EMISSIONS')

# 4d. CYLINDERS với FUEL_CONSUMPTION
axs[1, 1].scatter(data['CYLINDERS'], data['FUEL_CONSUMPTION*'], alpha=0.5, c=colors[3])
axs[1, 1].set_title('CYLINDERS với FUEL_CONSUMPTION')
axs[1, 1].set_xlabel('CYLINDERS')
axs[1, 1].set_ylabel('FUEL_CONSUMPTION*')

# Điều chỉnh khoảng cách giữa các subplot
plt.tight_layout()

plt.show()
