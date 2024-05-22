'''
    No : ID

    X1 transaction date: Ngày giao dịch, với định dạng năm.phần_thập_phân

    X2 house age: Tuổi của ngôi nhà (đơn vị: năm)

    X3 distance to the nearest MRT station: Khoảng cách đến trạm MRT (tàu điện ngầm) gần nhất (đơn vị: mét)

    X4 number of convenience stores: Số lượng cửa hàng tiện lợi nằm trong khu vực lân cận của bất động sản. (số nguyên)

    X5 latitude:  vĩ độ (đơn vị: độ)

    X6 longitude:  kinh độ (đơn vị: độ)

    Y house price of unit area:  Giá bất động sản trên đơn vị diện tích 
    (10.000 Đô la Đài Loan mới/Ping, với Ping là đơn vị diện tích địa phương, 1 Ping = 3,3 mét vuông)

    có 7 trường và 414 mẫu

          X2 house age  X3 distance to the nearest MRT station  X4 number of convenience stores  Y house price of unit area
    Min        0.00000                               23.382840                         0.000000                    7.600000
    Max       43.80000                             6488.021000                        10.000000                  117.500000
    Mean      17.71256                             1083.885689                         4.094203                   37.980193
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
data = pd.read_csv(r"E:\Data\DeCuongOnTap\ChuyenDeTienTien\Bai2_Real estate valuation data set Data Set\Real estate valuation data set.csv")

# Đổi tên các thuộc tính trong DataFrame ban đầu
data.rename(columns={
    'X1 transaction date': 'X1',
    'X2 house age': 'X2',
    'X3 distance to the nearest MRT station': 'X3',
    'X4 number of convenience stores': 'X4',
    'X5 latitude': 'X5',
    'X6 longitude': 'X6',
    'Y house price of unit area': 'Y'
}, inplace=True)

#Bai 2
# Tạo DataFrame từ các giá trị tối thiểu, tối đa và trung bình
summary_table = pd.DataFrame({'Min': data.min(), 'Max': data.max(), 'Mean': data.mean()}, index=['X2', 'X3', 'X4', 'Y'])

# Hiển thị bảng với các thuộc tính nằm theo hàng ngang (chuyển vị)
summary_table_transposed = summary_table.transpose()
print(summary_table_transposed)

#Bai 3
# a. Ngôi nhà mà có tuổi trên 30 và có giá trên 50
num_a = ((data['X2'] > 30) & (data['Y'] > 50)).sum()
print('Số ngôi nhà có tuổi trên 30 và có giá trên 50:', num_a)

# b. Ngôi nhà mà có giá dưới 30 và cách xa ga tàu dưới 1km
num_b = ((data['Y'] < 30) & (data['X3'] < 1000)).sum()
print('Số ngôi nhà có giá dưới 30 và cách xa ga tàu dưới 1km:', num_b)

result = f'''
    1.
    X1 transaction date: Ngày giao dịch, với định dạng năm.phần_thập_phân

    X2 house age: Tuổi của ngôi nhà (đơn vị: năm)

    X3 distance to the nearest MRT station: Khoảng cách đến trạm MRT (tàu điện ngầm) gần nhất (đơn vị: mét)

    X4 number of convenience stores: Số lượng cửa hàng tiện lợi nằm trong khu vực lân cận của bất động sản. (số nguyên)

    X5 latitude:  vĩ độ (đơn vị: độ)

    X6 longitude:  kinh độ (đơn vị: độ)

    Y house price of unit area:  Giá bất động sản trên đơn vị diện tích 
    (10.000 Đô la Đài Loan mới/Ping, với Ping là đơn vị diện tích địa phương, 1 Ping = 3,3 mét vuông)

    có 7 trường và 414 mẫu
    2.
{summary_table_transposed}
    3. 
    Số ngôi nhà có tuổi trên 30 và có giá trên 50: {num_a}
    Số ngôi nhà có giá dưới 30 và cách xa ga tàu dưới 1km: {num_b}
'''

filePath = r'E:\Data\DeCuongOnTap\ChuyenDeTienTien\Bai2_Real estate valuation data set Data Set\ketqua.txt'

writeFile(filePath, result)

#Bai 4
# Tạo 4 biểu đồ trên cùng một hình
fig, axs = plt.subplots(2, 2, figsize=(15, 7))

# a. Tuổi ngôi nhà với giá nhà
axs[0, 0].scatter(data['X2'], data['Y'], color='red')
axs[0, 0].set_xlabel('Tuổi ngôi nhà')
axs[0, 0].set_ylabel('Giá nhà')
axs[0, 0].set_title('Tuổi ngôi nhà với giá nhà')

# b. Giá nhà với khoảng cách tới ga tàu
axs[0, 1].scatter(data['Y'], data['X3'], color='green')
axs[0, 1].set_xlabel('Giá nhà')
axs[0, 1].set_ylabel('Khoảng cách tới ga tàu')
axs[0, 1].set_title('Giá nhà với khoảng cách tới ga tàu')

# c. Giá nhà với số cửa hàng tiện lợi
axs[1, 0].scatter(data['Y'], data['X4'], color='blue')
axs[1, 0].set_xlabel('Giá nhà')
axs[1, 0].set_ylabel('Số cửa hàng tiện lợi')
axs[1, 0].set_title('Giá nhà với số cửa hàng tiện lợi')

# d. Số cửa hàng tiện lợi với khoảng cách tới ga tàu
axs[1, 1].scatter(data['X4'], data['X3'], color='purple')
axs[1, 1].set_xlabel('Số cửa hàng tiện lợi')
axs[1, 1].set_ylabel('Khoảng cách tới ga tàu')
axs[1, 1].set_title('Số cửa hàng tiện lợi với khoảng cách tới ga tàu')

# Điều chỉnh khoảng cách giữa các biểu đồ
plt.tight_layout()

# Hiển thị biểu đồ
plt.show()
