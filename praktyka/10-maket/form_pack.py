"""Робота 10: форма реєстрації через PACK.

Запуск:     python praktyka/10-maket/form_pack.py
Перевірка:  python praktyka/10-maket/perevir.py
"""
import tkinter as tk

vikno = tk.Tk()
vikno.title("Реєстрація — pack")

# Заголовок
tk.Label(vikno, text="Реєстрація", font=("Arial", 16, "bold")).pack(pady=10)

# Чотири рядки: кожен — окрема рамка, всередині підпис і поле поруч
pidpysy = ["Імʼя", "Пошта", "Телефон", "Пароль"]
for tekst in pidpysy:
    ryadok = tk.Frame(vikno)
    ryadok.pack(fill="x", padx=10, pady=5)
    # однакова width і anchor="w" — щоб усі поля стали в одну колонку
    tk.Label(ryadok, text=tekst, width=10, anchor="w").pack(side="left")
    if tekst == "Пароль":
        pole = tk.Entry(ryadok, show="•")
    else:
        pole = tk.Entry(ryadok)
    pole.pack(side="left", fill="x", expand=True)

# Прапорець, притиснутий ліворуч
tk.Checkbutton(vikno, text="Погоджуюсь з умовами").pack(anchor="w", padx=10, pady=5)

# Кнопки внизу праворуч: рамка на всю ширину, кнопки притиснуті праворуч
knopky = tk.Frame(vikno)
knopky.pack(fill="x", padx=10, pady=10)
tk.Button(knopky, text="Скасувати").pack(side="right", padx=(5, 0))
tk.Button(knopky, text="Зареєструватись").pack(side="right")

vikno.mainloop()