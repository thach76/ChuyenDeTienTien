kho dữ liệu của bài
E:\Data\DeCuongOnTap\ChuyenDeTienTien

def add_line_numbers(input_string):
    lines = input_string.split('\n')
    numbered_lines = [f"{i+1}. {line}" for i, line in enumerate(lines)]
    return '\n'.join(numbered_lines)
print(add_line_numbers(result))