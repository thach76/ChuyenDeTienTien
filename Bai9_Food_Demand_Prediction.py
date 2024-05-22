result = '''
id
week: Tuần trong năm (Số nguyên (1 đến 145))
center_id: ID của trung tâm phân phối nơi sp được cung cấp.
meal_id: ID của sản phẩm.
checkout_price:  Giá mà khách hàng phải trả (giá thanh toán).
base_price: Giá cơ bản của sản phẩm 
emailer_for_promotion: sản phẩm có được quảng cáo qua email hay không?
    0: không
    1: có
homepage_featured: sản phẩm có được hiển thị nổi bật trên trang chủ hay không.
    0: không
    1: có
num_orders: Số lượng đơn đặt hàng cho sản phẩm


có 9 trường và 1999 mẫu

      checkout_price  base_price  emailer_for_promotion  homepage_featured   num_orders
Min        65.020000   93.120000               0.000000           0.000000     13.00000
Max       767.330000  767.330000               1.000000           1.000000  12137.00000
Mean      327.302596  347.972866               0.076538           0.105053    258.34017

a. Số lượng trung tâm có số lượng đơn > 200: 77
b. Loại thực phẩm tiêu thụ nhiều nhất: 2290

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
data = pd.read_csv(r"E:\Data\DeCuongOnTap\ChuyenDeTienTien\Bai9_Food Demand Prediction\Food demand.csv")

#Bai 2
# Lọc các cột cần tính toán
cols_to_analyze = ['checkout_price','base_price','emailer_for_promotion','homepage_featured','num_orders' ]

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
# a. Số lượng trung tâm (center_id) có số lượng đơn (num_orders) > 200
center_orders = data.groupby('center_id')['num_orders'].sum()
center_count = len(center_orders[center_orders > 200])
print(f"a. Số lượng trung tâm có số lượng đơn > 200: {center_count}")

# b. Loại thực phẩm nào (meal_id) tiêu thụ nhiều nhất (num_orders)
top_meal = data.groupby('meal_id')['num_orders'].sum().idxmax()
print(f"b. Loại thực phẩm tiêu thụ nhiều nhất: {top_meal}")

writeFile(r"E:\Data\DeCuongOnTap\ChuyenDeTienTien\Bai9_Food Demand Prediction\ketqua.txt", result)

# Bài 4
import matplotlib.pyplot as plt

# Tạo lưới 2x2 subplot
fig, axs = plt.subplots(2, 2, figsize=(15, 7))

# Danh sách các màu sẽ sử dụng cho từng biểu đồ
colors = ['r', 'g', 'b', 'm']  # Màu đỏ, xanh lá, xanh dương, tím

# a. checkout_price với base_price
axs[0, 0].scatter(data['base_price'], data['checkout_price'], alpha=0.5, c=colors[0])
axs[0, 0].set_title('checkout_price với base_price')
axs[0, 0].set_xlabel('base_price')
axs[0, 0].set_ylabel('checkout_price')

# b. checkout_price với num_orders
axs[0, 1].scatter(data['num_orders'], data['checkout_price'], alpha=0.5, c=colors[1])
axs[0, 1].set_title('checkout_price với num_orders')
axs[0, 1].set_xlabel('num_orders')
axs[0, 1].set_ylabel('checkout_price')

# c. checkout_price với homepage_featured
axs[1, 0].scatter(data['homepage_featured'], data['checkout_price'], alpha=0.5, c=colors[2])
axs[1, 0].set_title('checkout_price với homepage_featured')
axs[1, 0].set_xlabel('homepage_featured')
axs[1, 0].set_ylabel('checkout_price')

# d. base_price với num_orders
axs[1, 1].scatter(data['num_orders'], data['base_price'], alpha=0.5, c=colors[3])
axs[1, 1].set_title('base_price với num_orders')
axs[1, 1].set_xlabel('num_orders')
axs[1, 1].set_ylabel('base_price')

# Điều chỉnh khoảng cách giữa các subplot
plt.subplots_adjust(wspace=0.3, hspace=0.5)

plt.show()
