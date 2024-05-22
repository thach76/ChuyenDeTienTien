result = '''
make_model: Hãng và model của xe ô tô.
body_type: Loại thân xe (Sedans, SUV, Hatchback, ...).
Body Color: Màu sắc của xe.
km: Số km đã đi (đơn vị: km).
hp: Công suất của động cơ (đơn vị: mã lực, hp).
Gearing Type: Loại hộp số (Automatic, Manual).
Extras: Các tính năng bổ sung của xe.
price: Giá của xe 

có 8 trường và 4800 mẫu

                 km    hp         price
Min        0.000000  85.0   5555.000000
Max   291800.000000  85.0  56100.000000
Mean   31912.910417  85.0  19722.871875

Số lượng xe ô tô Audi mà có giá trên 20000: 2186
Số lượng xe ô tô Audi mà có màu đỏ loại Compact: 92
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
data = pd.read_csv(r"E:\Data\DeCuongOnTap\ChuyenDeTienTien\Bai4_Car Price Prediction\car_price.csv")

#Bai 2
# Lọc các cột có kiểu dữ liệu số
numeric_cols = data.select_dtypes(include=['number']).columns

# Tạo DataFrame từ các giá trị tối thiểu, tối đa và trung bình
summary_table = pd.DataFrame({'Min': data[numeric_cols].min(), 
                               'Max': data[numeric_cols].max(), 
                               'Mean': data[numeric_cols].mean()}, 
                              index=numeric_cols)

# Hiển thị bảng với các thuộc tính nằm theo hàng ngang (chuyển vị)
summary_table_transposed = summary_table.transpose()
print(summary_table_transposed)


# 3a. Xe ô tô Audi mà có giá trên 20000
num_a = ((data['make_model'].str.contains('Audi')) & (data['price'] > 20000)).sum()
print(f"Số lượng xe ô tô Audi mà có giá trên 20000: {num_a}")

# 3b. Xe ô tô Audi mà có màu đỏ loại Compact
num_b = ((data['make_model'].str.contains('Audi')) & (data['Body Color'] == 'Red') & (data['body_type'] == 'Compact')).sum()
print(f"Số lượng xe ô tô Audi mà có màu đỏ loại Compact: {num_b}")


writeFile(r"E:\Data\DeCuongOnTap\ChuyenDeTienTien\Bai4_Car Price Prediction\ketqua.txt", result)

# Bài 4
# Tạo 4 biểu đồ trên cùng một hình
fig, axs = plt.subplots(2, 2, figsize=(15, 7))

# 4a. Giá với HP
axs[0, 0].scatter(data['hp'], data['price'], color='r', alpha=0.5)
axs[0, 0].set_xlabel('Công suất (hp)')
axs[0, 0].set_ylabel('Giá')
axs[0, 0].set_title('Giá với HP')

# 4b. Giá với KM
axs[0, 1].scatter(data['km'], data['price'], color='g', alpha=0.5)
axs[0, 1].set_xlabel('Số km đã đi')
axs[0, 1].set_ylabel('Giá')
axs[0, 1].set_title('Giá với KM')

# 4c. KM với HP
axs[1, 0].scatter(data['km'], data['hp'], color='b', alpha=0.5)
axs[1, 0].set_xlabel('Số km đã đi')
axs[1, 0].set_ylabel('Công suất (hp)')
axs[1, 0].set_title('KM với HP')

# Điều chỉnh khoảng cách giữa các biểu đồ
plt.tight_layout()

# Hiển thị biểu đồ
plt.show()

