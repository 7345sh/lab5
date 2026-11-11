import tkinter as tk
from tkinter import messagebox

DEFAULT_FILE = "notes.txt"


def save_note(text_widget: tk.Text, filename_entry: tk.Entry) -> None:
    # Берём имя файла из поля, если пусто — дефолтное
    filename = filename_entry.get().strip()
    if not filename:
        filename = DEFAULT_FILE

    # Если нет расширения .txt — добавляем
    if not filename.endswith(".txt"):
        filename += ".txt"

    # Получаем текст из поля
    text = text_widget.get("1.0", tk.END).strip()

    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(text)
        messagebox.showinfo("Готово", f"Заметка сохранена в {filename}")
    except OSError as e:
        messagebox.showerror("Ошибка", f"Не удалось сохранить файл: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Заметки")
    root.geometry("400x600")

    # Поле для имени файла
    file_frame = tk.Frame(root)
    file_frame.pack(fill="x", padx=10, pady=(10, 0))

    tk.Label(file_frame, text="Имя файла:").pack(side=tk.LEFT)
    filename_entry = tk.Entry(file_frame)
    filename_entry.pack(side=tk.LEFT, fill="x", expand=True, padx=5)
    filename_entry.insert(0, DEFAULT_FILE)

    # Поле для ввода текста
    text = tk.Text(root, wrap="word", font=("Arial", 12))
    text.pack(fill="both", expand=True, padx=10, pady=10)

    # Панель с кнопками
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    tk.Button(
        button_frame, text="Сохранить", width=15,
        command=lambda: save_note(text, filename_entry)
    ).pack(side=tk.LEFT, padx=5)

    root.mainloop()
