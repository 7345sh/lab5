import tkinter as tk


def show_greeting() -> None:
    label.config(text="Привет!")


if __name__ == "__main__":
    # Создание главного окна
    root = tk.Tk()
    root.title("Привет")
    root.geometry("300x150")

    # Кнопка, которая вызывает show_greeting
    button = tk.Button(root, text="Привет?", command=show_greeting)
    button.pack(pady=10)

    # Метка для вывода результата
    label = tk.Label(root, text="")
    label.pack()

    # Запускаем цикл обработки событий
    root.mainloop()
