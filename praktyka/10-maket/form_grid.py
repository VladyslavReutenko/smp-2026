"""Робота 10: форма реєстрації через GRID.

Запуск:     python praktyka/10-maket/form_grid.py
Перевірка:  python praktyka/10-maket/perevir.py
"""
import tkinter as tk

vikno = tk.Tk()
vikno.title("Реєстрація — grid")

# Колонка 1 (з полями) тягнеться разом із вікном, колонка 0 (з підписами) — ні
vikno.columnconfigure(1, weight=1)

# Заголовок: займає обидві колонки
tk.Label(vikno, text="Реєстрація", font=("Arial", 16, "bold")).grid(
    row=0, column=0, columnspan=2, padx=10, pady=10)

# Чотири рядки «підпис + поле»
pidpysy = ["Імʼя", "Пошта", "Телефон", "Пароль"]
for i, tekst in enumerate(pidpysy, start=1):
    tk.Label(vikno, text=tekst).grid(row=i, column=0, sticky="w", padx=10, pady=5)
    if tekst == "Пароль":
        pole = tk.Entry(vikno, show="•")
    else:
        pole = tk.Entry(vikno)
    pole.grid(row=i, column=1, sticky="ew", padx=10, pady=5)

# Прапорець: теж на обидві колонки, притиснутий ліворуч
tk.Checkbutton(vikno, text="Погоджуюсь з умовами").grid(
    row=5, column=0, columnspan=2, sticky="w", padx=10, pady=5)

# Кнопки: окрема рамка, притиснута праворуч
knopky = tk.Frame(vikno)
knopky.grid(row=6, column=0, columnspan=2, sticky="e", padx=10, pady=10)
tk.Button(knopky, text="Скасувати").pack(side="right", padx=(5, 0))
tk.Button(knopky, text="Зареєструватись").pack(side="right")

vikno.mainloop()