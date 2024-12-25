import itertools
import re

# Kiểm tra tính hợp lệ của biểu thức logic
def is_valid_expression(expression):
    valid_chars = set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz∨∧→¬() ')
    return all(c in valid_chars for c in expression)

# Thay thế các biến trong biểu thức với giá trị tương ứng và tính toán kết quả
def evaluate_expression(expression, values):
    # Thay thế các biến trong biểu thức bằng giá trị tương ứng
    for var, val in values.items():
        expression = expression.replace(var, str(val))
    
    # Thay thế các toán tử logic để sử dụng cú pháp Python
    expression = expression.replace('∧', ' and ').replace('∨', ' or ').replace('¬', ' not ').replace('→', '<=')
    
    try:
        # Đánh giá biểu thức logic
        return eval(expression)
    except Exception as e:
        return False

# Hàm tạo bảng chân trị
def generate_truth_table(expression):
    # Tìm tất cả các biến trong biểu thức
    variables = list(set(re.findall(r'[A-Za-z]+', expression)))
    variables.sort()  # Đảm bảo các biến được liệt kê theo thứ tự

    # In tiêu đề bảng chân trị
    print("\t".join(variables) + "\tKết quả")
    
    # Tạo tất cả các tổ hợp giá trị của các biến
    num_variables = len(variables)
    for combo in itertools.product([True, False], repeat=num_variables):
        values = dict(zip(variables, combo))
        
        # In giá trị của các biến
        row = [("T" if values[var] else "F") for var in variables]
        
        # Tính toán kết quả của biểu thức
        result = evaluate_expression(expression, values)
        
        # In kết quả cho mỗi tổ hợp
        print("\t".join(row) + "\t" + ("T" if result else "F"))

# Nhập biểu thức và tạo bảng chân trị
def input_expression_and_generate_table():
    expression = input("Nhập biểu thức logic (ví dụ: (A ∨ ¬B) ∧ C): ")
    
    if is_valid_expression(expression):
        generate_truth_table(expression)
    else:
        print("Biểu thức không hợp lệ.")

# Gọi hàm chính để nhập và tạo bảng chân trị
input_expression_and_generate_table()
