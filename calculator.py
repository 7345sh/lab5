import tkinter as tk


def calculate(operation: str) -> None:
    # Выполняет операцию над двумя числами и выводит результат
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())

        if operation == "+":
            result = a + b
        elif operation == "-":
            result = a - b
        elif operation == "*":
            result = a * b
        elif operation == "/":
            if b == 0:
                result_label.config(text="Ошибка: деление на ноль")
                return
            result = a / b
        else:
            result = 0

        result_label.config(text=f"Результат: {result}")
    except ValueError:
        result_label.config(text="Ошибка: введите числа")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Калькулятор")
    root.geometry("320x250")

    tk.Label(root, text="Первое число:").pack()
    entry_a = tk.Entry(root)
    entry_a.pack()

    # Кнопки операций
    frame = tk.Frame(root)
    frame.pack(pady=10)
    tk.Button(
        frame, text="+", width=3, command=lambda: calculate("+")
    ).pack(side=tk.LEFT)
    tk.Button(
        frame, text="-", width=3, command=lambda: calculate("-")
    ).pack(side=tk.LEFT)
    tk.Button(
        frame, text="*", width=3, command=lambda: calculate("*")
    ).pack(side=tk.LEFT)
    tk.Button(
        frame, text="/", width=3, command=lambda: calculate("/")
    ).pack(side=tk.LEFT)

    tk.Label(root, text="Второе число:").pack()
    entry_b = tk.Entry(root)
    entry_b.pack()

    # Метка для результата
    result_label = tk.Label(root, text="Результат: ")
    result_label.pack(pady=10)

    root.mainloop()
