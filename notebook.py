import tkinter as tk
from tkinter import ttk


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Интересные факты")
    root.geometry("400x300")

    # Создаём Notebook (контейнер для вкладок)
    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True, padx=10, pady=10)

    # Вкладка 1
    tab1 = tk.Frame(notebook)
    tk.Label(
        tab1, text="Python назван в честь комедийного шоу Монти Пайтон"
    ).pack(pady=20)
    notebook.add(tab1, text="Первый")

    # Вкладка 2
    tab2 = tk.Frame(notebook)
    tk.Label(
        tab2, text="Если ввести import this, Python выведет Дзен Python"
    ).pack(pady=20)
    notebook.add(tab2, text="Второй")

    # Вкладка 3
    tab3 = tk.Frame(notebook)
    tk.Label(
        tab3, text="В Python принято называть переменные в snake_case"
    ).pack(pady=20)
    notebook.add(tab3, text="Третий")

    root.mainloop()
