result = '''
CRIM: Tỷ lệ tội phạm bình quân đầu người theo thị trấn.
ZN: Tỷ lệ đất dân cư được quy hoạch cho các lô đất có diện tích trên 25.000 feet vuông.
INDUS: Tỷ lệ diện tích kinh doanh phi bán lẻ trên toàn thị trấn.
CHAS: Biến giả (dummy variable) cho sông Charles, bằng 1 nếu khu vực giáp sông, ngược lại bằng 0.
NOX: Nồng độ khí nitric oxides (phần triệu).
RM: Số phòng ngủ trung bình trên mỗi ngôi nhà.
AGE: Tỷ lệ nhà ở do chủ sở hữu được xây dựng trước năm 1940.
DIS: Khoảng cách có trọng số tới 5 trung tâm việc làm của Boston.
RAD: Chỉ số tiếp cận với các đường cao tốc.
TAX: Tỷ lệ thuế bất động sản đầy đủ trên 10.000 đô la.
PTRATIO: Tỷ lệ học sinh/giáo viên theo thị trấn.
B: 1000(Bk - 0.63)^2 với Bk là tỷ lệ dân da đen theo thị trấn.
LSTAT: Phần trăm dân cư có thu nhập thấp.
MEDV: Giá trị trung vị của nhà ở do chủ sở hữu (nghìn đô la).

có 14 trường và 506 mẫu

           CRIM      INDUS     CHAS        RM         AGE       MEDV
Min    0.006320   0.460000  0.00000  3.561000    2.900000   5.000000
Max   88.976200  27.740000  1.00000  8.780000  100.000000  50.000000
Mean   3.613524  11.136779  0.06917  6.284634   68.574901  22.532806

Số ngôi nhà có tuổi trên 30 và có giá trên 30.000 đô la: 66
Số ngôi nhà có giá dưới 30.000 đô la và tỷ lệ tội phạm dưới 0.1: 107
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
data = pd.read_csv(r"E:\Data\DeCuongOnTap\ChuyenDeTienTien\Bai3_Boston-house-price-data\Boston-house-price-data.csv")

#Bai 2
# Tạo DataFrame từ các giá trị tối thiểu, tối đa và trung bình
summary_table = pd.DataFrame({'Min': data.min(), 'Max': data.max(), 'Mean': data.mean()}, index=['CRIM', 'INDUS', 'CHAS','RM','AGE','MEDV'])

# Hiển thị bảng với các thuộc tính nằm theo hàng ngang (chuyển vị)
summary_table_transposed = summary_table.transpose()
print(summary_table_transposed)

#Bài 3
# a. Ngôi nhà mà có tuổi trên 30 và có giá trên 30.000 đô la
num_a = ((data['AGE'] > 30) & (data['MEDV'] > 30)).sum()
print('Số ngôi nhà có tuổi trên 30 và có giá trên 30.000 đô la:', num_a)

# b. Ngôi nhà mà có giá dưới 30.000 đô la và tỷ lệ tội phạm dưới 0.1
num_b = ((data['MEDV'] < 30) & (data['CRIM'] < 0.1)).sum()
print('Số ngôi nhà có giá dưới 30.000 đô la và tỷ lệ tội phạm dưới 0.1:', num_b)

writeFile(r"E:\Data\DeCuongOnTap\ChuyenDeTienTien\Bai3_Boston-house-price-data\ketqua.txt", result)

# Bài 4

# Tạo 4 biểu đồ trên cùng một hình
fig, axs = plt.subplots(2, 2, figsize=(15, 7))

# a. MEDV với CRIM
axs[0, 0].scatter(data['MEDV'], data['CRIM'], color='red')
axs[0, 0].set_xlabel('Giá trị trung vị nhà ở (MEDV)')
axs[0, 0].set_ylabel('Tỷ lệ tội phạm (CRIM)')
axs[0, 0].set_title('MEDV với CRIM')

# b. MEDV với RM
axs[0, 1].scatter(data['MEDV'], data['RM'], color='green')
axs[0, 1].set_xlabel('Giá trị trung vị nhà ở (MEDV)')
axs[0, 1].set_ylabel('Số phòng trung bình (RM)')
axs[0, 1].set_title('MEDV với RM')

# c. MEDV với AGE
axs[1, 0].scatter(data['MEDV'], data['AGE'], color='blue')
axs[1, 0].set_xlabel('Giá trị trung vị nhà ở (MEDV)')
axs[1, 0].set_ylabel('Tỷ lệ nhà xây trước 1940 (AGE)')
axs[1, 0].set_title('MEDV với AGE')

# d. AGE với RM
axs[1, 1].scatter(data['AGE'], data['RM'], color='purple')
axs[1, 1].set_xlabel('Tỷ lệ nhà xây trước 1940 (AGE)')
axs[1, 1].set_ylabel('Số phòng trung bình (RM)')
axs[1, 1].set_title('AGE với RM')

# Điều chỉnh khoảng cách giữa các biểu đồ
plt.tight_layout()

# Hiển thị biểu đồ
plt.show()
