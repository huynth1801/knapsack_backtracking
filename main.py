import tkinter as tk


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
def solve_knapsack():
    values = [int(value_entry.get()) for value_entry in value_entries]
    weights = [int(weight_entry.get()) for weight_entry in weight_entries]
    capacity = int(capacity_entry.get())

    result = knapsack_backtracking(values, weights, capacity)
    result_label.config(text=f"Giá trị lớn nhất có thể đạt được: {result}")


# Ví dụ minh họa
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
result = knapsack_backtracking(values, weights, capacity)
print("Tổng giá trị lớn nhất có thể đạt được là:", result)
print("*" * 50)
W = 10
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
print(unbounded_knapsack(W, weights, values))

app = tk.Tk()
app.title("Knapsack with backtracking")

# Tạo các widget trên giao diện
value_entries = []
weight_entries = []

num_items = 3  # Số lượng đối tượng
for i in range(num_items):
    tk.Label(app, text=f"Đối tượng {i + 1}").grid(row=i, column=0)
    value_entry = tk.Entry(app)
    weight_entry = tk.Entry(app)
    value_entry.grid(row=i, column=1)
    weight_entry.grid(row=i, column=2)
    value_entries.append(value_entry)
    weight_entries.append(weight_entry)

tk.Label(app, text="Sức chứa túi:").grid(row=num_items, column=0)
capacity_entry = tk.Entry(app)
capacity_entry.grid(row=num_items, column=1)

solve_button = tk.Button(app, text="Solve", command=solve_knapsack)
solve_button.grid(row=num_items + 1, column=0, columnspan=3)

result_label = tk.Label(app, text="")
result_label.grid(row=num_items + 2, column=0, columnspan=3)

# Chạy ứng dụng
app.mainloop()
