import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def draw_plot(canvas_holder: tk.Frame) -> None:
    # Рисует график y=x^2 внутри переданного контейнера
    # Создание фигуры
    fig = Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)

    # Данные
    x = list(range(-10, 11))
    y = [i ** 2 for i in x]

    # Рисуем
    ax.plot(x, y, color="blue", linewidth=2, label="y = x²")
    ax.set_title("График функции y = x²")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.axhline(0, color="black", linewidth=0.5)
    ax.axvline(0, color="black", linewidth=0.5)
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.legend()

    # Встраиваем в Tkinter
    canvas = FigureCanvasTkAgg(fig, master=canvas_holder)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("График в Tkinter")
    root.geometry("700x550")

    # Контейнер для графика
    frame = tk.Frame(root)
    frame.pack(fill="both", expand=True, padx=10, pady=10)

    draw_plot(frame)

    root.mainloop()
