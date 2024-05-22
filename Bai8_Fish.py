result = '''
Species (Loài): loài cá
Weight (Trọng lượng): gram
Length1 (Chiều dài 1): Vertical length: Chiều dài dọc (cm)
length2 (chiều dài 2): Diagonal length: đầu đến đuôi đường chéo
length3 (chiều dài 3): Cross length từ một bên của cá đến bên kia theo chiều ngang.
Height (Chiều cao): cm
Width (Chiều rộng): cm

có 7 trường và 159 mẫu

           Weight   Length1    Length2    Length3     Height     Width
Min      0.000000   7.50000   8.400000   8.800000   1.728400  1.047600
Max   1650.000000  59.00000  63.400000  68.000000  18.957000  8.142000
Mean   398.326415  26.24717  28.415723  31.227044   8.970994  4.417486

a. Số lượng mẫu cá Bream có Weight > 600: 18
b. Số lượng mẫu cá Parkiki có Weight > 150: 0
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
data = pd.read_csv(r"E:\Data\DeCuongOnTap\ChuyenDeTienTien\Bai8_Fish\Fish.csv")

#Bai 2
# Lọc các cột cần tính toán
cols_to_analyze = ['Weight', 'Length1', 'Length2', 'Length3', 'Height', 'Width']

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
# a. Số lượng mẫu cá Bream có Weight > 600
bream_count = len(data[(data['Species'] == 'Bream') & (data['Weight'] > 600)])
print(f"a. Số lượng mẫu cá Bream có Weight > 600: {bream_count}")

# b. Số lượng mẫu cá Parkiki có Weight > 150
parkiki_count = len(data[(data['Species'] == 'Parkiki') & (data['Weight'] > 150)])
print(f"b. Số lượng mẫu cá Parkiki có Weight > 150: {parkiki_count}")

writeFile(r"E:\Data\DeCuongOnTap\ChuyenDeTienTien\Bai8_Fish\ketqua.txt", result)

# Bài 4
# Tạo lưới 2x2 subplot
fig, axs = plt.subplots(2, 2, figsize=(15, 7))

# Danh sách các màu sẽ sử dụng cho từng biểu đồ
colors = ['r', 'g', 'b', 'm']  # Màu đỏ, xanh lá, xanh dương, tím

# a. Weight với Width
axs[0, 0].scatter(data['Width'], data['Weight'], alpha=0.5, c=colors[0])
axs[0, 0].set_title('Weight với Width')
axs[0, 0].set_xlabel('Width')
axs[0, 0].set_ylabel('Weight')

# b. Weight với Lenght1
axs[0, 1].scatter(data['Length1'], data['Weight'], alpha=0.5, c=colors[1])
axs[0, 1].set_title('Weight với Length1')
axs[0, 1].set_xlabel('Length1')
axs[0, 1].set_ylabel('Weight')

# c. Weight với Length2
axs[1, 0].scatter(data['Length2'], data['Weight'], alpha=0.5, c=colors[2])
axs[1, 0].set_title('Weight với Length2')
axs[1, 0].set_xlabel('Length2')
axs[1, 0].set_ylabel('Weight')

# d. Height với Width
axs[1, 1].scatter(data['Width'], data['Height'], alpha=0.5, c=colors[3])
axs[1, 1].set_title('Height với Width')
axs[1, 1].set_xlabel('Width')
axs[1, 1].set_ylabel('Height')

# Điều chỉnh khoảng cách giữa các subplot
plt.subplots_adjust(wspace=0.3, hspace=0.5)

plt.show()
