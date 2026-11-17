"""Робота 10: форма реєстрації через PLACE.

Запуск:     python praktyka/10-maket/form_place.py
Перевірка:  python praktyka/10-maket/perevir.py
"""
import tkinter as tk

vikno = tk.Tk()
vikno.title("Реєстрація — place")
vikno.geometry("360x300")

# Заголовок
tk.Label(vikno, text="Реєстрація", font=("Arial", 16, "bold")).place(x=120, y=10)

# Чотири рядки: підпис на x=10, поле на x=100; крок по вертикалі 40 px
pidpysy = ["Імʼя", "Пошта", "Телефон", "Пароль"]
for i, tekst in enumerate(pidpysy):
    y = 55 + i * 40
    tk.Label(vikno, text=tekst).place(x=10, y=y)
    if tekst == "Пароль":
        pole = tk.Entry(vikno, show="•")
    else:
        pole = tk.Entry(vikno)
    pole.place(x=100, y=y, width=240)

# Прапорець
tk.Checkbutton(vikno, text="Погоджуюсь з умовами").place(x=10, y=215)

# Кнопки внизу праворуч
tk.Button(vikno, text="Скасувати").place(x=270, y=260)
tk.Button(vikno, text="Зареєструватись").place(x=150, y=260)

vikno.mainloop()