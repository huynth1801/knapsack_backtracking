import tkinter as tk
from knapsack01.BBKnapsack import BBKnapsack

num_items = 0

def knapsack_backtracking(values, weights, capacity):
    n = len(values)

    def backtrack(index, current_weight, current_value):
        nonlocal max_value
        if current_weight <= capacity and current_value > max_value:
            max_value = current_value

        if index == n or current_weight >= capacity:
            return

        # Thử đặt đối tượng tiếp theo vào túi
        backtrack(
            index + 1, current_weight + weights[index], current_value + values[index]
        )

        # Không đặt đối tượng vào túi
        backtrack(index + 1, current_weight, current_value)

    max_value = 0
    backtrack(0, 0, 0)
    return max_value


# Bai toan cai tui vo han
def unbounded_knapsack(W, weights, values):
    n = len(weights)

    def backtrack(current_weight, current_value, index):
        if current_weight == W:
            return current_value

        if index == n or current_weight > W:
            return 0

        max_value = current_value

        for i in range(index, n):
            if current_weight + weights[i] <= W:
                max_value = max(
                    max_value,
                    backtrack(
                        current_weight + weights[i], current_value + values[i], i
                    ),
                )

        return max_value

    return backtrack(0, 0, 0)


# Hàm xử lý sự kiện khi người dùng nhấn nút "Solve"
def solve_knapsack(problem_number):
    values = [int(value_entry.get()) for value_entry in value_entries]
    weights = [int(weight_entry.get()) for weight_entry in weight_entries]
    capacity = int(capacity_entry.get())

    if problem_number == 1:
        result = knapsack_backtracking(values, weights, capacity)
        result_label.config(text=f"Kết quả bài toán {problem_number}: {result}")
    elif problem_number == 2:
        result = unbounded_knapsack(capacity, weights, values)
        result_label.config(text=f"Kết quả bài toán {problem_number}: {result}")


app = tk.Tk()
app.title("Knapsack Solver")

# Tạo các widget trên giao diện
num_items_label = tk.Label(app, text="Số lượng đối tượng:")
num_items_label.grid(row=0, column=0)
num_items_entry = tk.Entry(app)
num_items_entry.grid(row=0, column=1)

value_entries = []
weight_entries = []

def create_input_fields():
    global num_items
    num_items = int(num_items_entry.get())

    # Xóa các trường nhập liệu cũ (nếu có)
    for entry in value_entries:
        entry.destroy()
    for entry in weight_entries:
        entry.destroy()

    value_entries.clear()
    weight_entries.clear()

    # Tạo các trường nhập liệu mới
    for i in range(num_items):
        value_label = tk.Label(app, text=f"Giá trị {i+1}:")
        value_label.grid(row=i+1, column=0)
        value_entry = tk.Entry(app)
        value_entry.grid(row=i+1, column=1)
        value_entries.append(value_entry)

        weight_label = tk.Label(app, text=f"Trọng lượng {i+1}:")
        weight_label.grid(row=i+1, column=2)
        weight_entry = tk.Entry(app)
        weight_entry.grid(row=i+1, column=3)
        weight_entries.append(weight_entry)

# Nút "Tạo trường nhập liệu"
create_fields_button = tk.Button(app, text="Tạo trường nhập liệu", command=create_input_fields)
create_fields_button.grid(row=0, column=2)

capacity_label = tk.Label(app, text="Sức chứa túi:")
capacity_label.grid(row=0, column=4)
capacity_entry = tk.Entry(app)
capacity_entry.grid(row=0, column=5)

# Nút "Giải bài toán"
solve_button = tk.Button(app, text="Giải bài toán", command=lambda: solve_knapsack(1))
solve_button.grid(row=0, column=6)
result_label = tk.Label(app, text="")
result_label.grid(row= 3 + 3, column=0, columnspan=3)

app.mainloop()