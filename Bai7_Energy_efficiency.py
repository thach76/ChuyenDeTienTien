result = '''
X1 Relative Compactness: Độ gọn gàng tương đối của tòa nhà, 
            tỷ lệ  diện tích bề mặt bao quanh nó với giữa thể tích tòa nhà
X2 Surface Area: Tổng diện tích bề mặt của tòa nhà.
X3 Wall Area: Diện tích tường.
X4 Roof Area: Diện tích mái.
X5 Overall Height: Chiều cao của tòa nhà.
X6 Orientation: Hướng của tòa nhà
X7 Glazing Area: Diện tích kính
X8 Glazing Area Distribution: Cách phân bố diện tích kính trên các mặt tường. (ví dụ: 0, 1, 2, 4, 5 có thể đại diện cho các kiểu phân bố khác nhau).
Y1 Heating Load: Tải trọng sưởi ấm, đo bằng năng lượng cần thiết để sưởi ấm tòa nhà.
Y2 Cooling Load: Tải trọng làm mát, đo bằng năng lượng cần thiết để làm mát tòa nhà.
có 8 trường và 768 mẫu

            X1          X2     X3          X4    X5         Y1        Y2
Min   0.620000  514.500000  245.0  110.250000  3.50   6.010000  10.90000
Max   0.980000  808.500000  416.5  220.500000  7.00  43.100000  48.03000
Mean  0.764167  671.708333  318.5  176.604167  5.25  22.307201  24.58776

a. Số lượng mẫu xe có Y1 < 15 và Y2 < 26: 285
b. Số lượng mẫu xe có Y1 < 15 và X1 < 0.7: 157
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
data = pd.read_csv(r"E:\Data\DeCuongOnTap\ChuyenDeTienTien\Bai7_Energy efficiency Data Set\ENB2012_data.csv")

#Bai 2
# Lọc các cột cần tính toán
cols_to_analyze = ['X1','X2','X3','X4','X5', 'Y1','Y2']

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
# Lọc các mẫu xe có Y1 < 15 và Y2 < 26
filtered_data = data[(data['Y1'] < 15) & (data['Y2'] < 26)]
print(f"a. Số lượng mẫu xe có Y1 < 15 và Y2 < 26: {len(filtered_data)}")
# Lọc các mẫu xe có Y1 < 15 và X1 < 0.7
filtered_data = data[(data['Y1'] < 15) & (data['X1'] < 0.7)]
print(f"b. Số lượng mẫu xe có Y1 < 15 và X1 < 0.7: {len(filtered_data)}")

writeFile(r"E:\Data\DeCuongOnTap\ChuyenDeTienTien\Bai7_Energy efficiency Data Set\ketqua.txt", result)

# Bài 4


# Tạo lưới 2x2 subplot
fig, axs = plt.subplots(2, 2, figsize=(15, 7))

# Danh sách các màu sẽ sử dụng cho từng biểu đồ
colors = ['r', 'g', 'b', 'm']  # Màu đỏ, xanh lá, xanh dương, tím

# a. Tải trọng sưởi ấm (Y1) với Độ gọn gàng tương đối của tòa nhà (X1)
axs[0, 0].scatter(data['X1'], data['Y1'], alpha=0.5, c=colors[0])
axs[0, 0].set_title('Tải trọng sưởi ấm (Y1) với Độ gọn gàng tương đối của tòa nhà (X1)')
axs[0, 0].set_xlabel('Độ gọn gàng tương đối của tòa nhà (X1)')
axs[0, 0].set_ylabel('Tải trọng sưởi ấm (Y1)')

# b. Tải trọng sưởi ấm (Y1) với Tổng diện tích bề mặt của tòa nhà (X2)
axs[0, 1].scatter(data['X2'], data['Y1'], alpha=0.5, c=colors[1])
axs[0, 1].set_title('Tải trọng sưởi ấm (Y1) với Tổng diện tích bề mặt của tòa nhà (X2)')
axs[0, 1].set_xlabel('Tổng diện tích bề mặt của tòa nhà (X2)')
axs[0, 1].set_ylabel('Tải trọng sưởi ấm (Y1)')

# c. Tải trọng làm mát (Y2) với Độ gọn gàng tương đối của tòa nhà (X1)
axs[1, 0].scatter(data['X1'], data['Y2'], alpha=0.5, c=colors[2])
axs[1, 0].set_title('Tải trọng làm mát (Y2) với Độ gọn gàng tương đối của tòa nhà (X1)')
axs[1, 0].set_xlabel('Độ gọn gàng tương đối của tòa nhà (X1)')
axs[1, 0].set_ylabel('Tải trọng làm mát (Y2)')

# d. Tải trọng làm mát (Y2) với Tổng diện tích bề mặt của tòa nhà (X2)
axs[1, 1].scatter(data['X2'], data['Y2'], alpha=0.5, c=colors[3])
axs[1, 1].set_title('Tải trọng làm mát (Y2) với Tổng diện tích bề mặt của tòa nhà (X2)')
axs[1, 1].set_xlabel('Tổng diện tích bề mặt của tòa nhà (X2)')
axs[1, 1].set_ylabel('Tải trọng làm mát (Y2)')

# Điều chỉnh khoảng cách giữa các subplot
plt.tight_layout()

plt.show()


