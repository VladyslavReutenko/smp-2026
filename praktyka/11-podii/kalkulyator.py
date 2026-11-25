"""Робота 11: калькулятор, який реагує на події.

Запуск:     python praktyka/11-podii/kalkulyator.py
Перевірка:  python praktyka/11-podii/perevir.py
"""
import tkinter as tk

vikno = tk.Tk()
vikno.title("Калькулятор")

# Змінні, повʼязані з віджетами (textvariable)
a_var = tk.StringVar()
b_var = tk.StringVar()
operatsiia = tk.StringVar(value="+")
rezultat = tk.StringVar(value="—")
pomylka = tk.StringVar()

OPERATSII = ["+", "-", "*", "/"]


def porakhuvaty(podiia=None):
    """І для кнопки (podiia=None), і для Enter (podiia=Event)."""
    pomylka.set("")
    try:
        a = float(a_var.get().replace(",", "."))
        b = float(b_var.get().replace(",", "."))
    except ValueError:
        rezultat.set("—")
        pomylka.set("Введіть два числа (не літери й не порожньо)")
        return
    znak = operatsiia.get()
    try:
        if znak == "+":
            r = a + b
        elif znak == "-":
            r = a - b
        elif znak == "*":
            r = a * b
        else:
            r = a / b
    except ZeroDivisionError:
        rezultat.set("—")
        pomylka.set("На нуль ділити не можна")
        return
    rezultat.set(f"{r:g}")


def ochystyty(podiia=None):
    """Esc: очищає форму."""
    a_var.set("")
    b_var.set("")
    operatsiia.set("+")
    rezultat.set("—")
    pomylka.set("")
    pole_a.focus_set()


# Макет
tk.Label(vikno, text="Калькулятор", font=("Arial", 14, "bold")).grid(
    row=0, column=0, columnspan=2, padx=10, pady=10)

tk.Label(vikno, text="Число A").grid(row=1, column=0, sticky="w", padx=10, pady=5)
pole_a = tk.Entry(vikno, textvariable=a_var)
pole_a.grid(row=1, column=1, sticky="ew", padx=10, pady=5)

tk.Label(vikno, text="Дія").grid(row=2, column=0, sticky="w", padx=10, pady=5)
tk.OptionMenu(vikno, operatsiia, *OPERATSII).grid(
    row=2, column=1, sticky="w", padx=10, pady=5)

tk.Label(vikno, text="Число B").grid(row=3, column=0, sticky="w", padx=10, pady=5)
pole_b = tk.Entry(vikno, textvariable=b_var)
pole_b.grid(row=3, column=1, sticky="ew", padx=10, pady=5)

tk.Button(vikno, text="Порахувати", command=porakhuvaty).grid(
    row=4, column=0, columnspan=2, pady=10)

tk.Label(vikno, text="Результат:").grid(row=5, column=0, sticky="w", padx=10)
tk.Label(vikno, textvariable=rezultat, font=("Arial", 12, "bold")).grid(
    row=5, column=1, sticky="w", padx=10)

tk.Label(vikno, textvariable=pomylka, fg="red").grid(
    row=6, column=0, columnspan=2, padx=10, pady=5)

vikno.columnconfigure(1, weight=1)

# Події
vikno.bind("<Return>", porakhuvaty)   # Enter з будь-якого поля
vikno.bind("<Escape>", ochystyty)     # Esc з будь-якого поля

pole_a.focus_set()
vikno.mainloop()