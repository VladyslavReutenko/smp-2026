import re
from collections import Counter

pattern = re.compile(
    r'^(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<time>[^\]]+)\] '
    r'"(?P<method>[A-Z]+) (?P<path>\S+) (?P<protocol>HTTP/\d\.\d)" '
    r'(?P<status>\d{3})'
)

rozibrano = 0
propushcheno = 0
ip_counter = Counter()
status_counter = Counter()
pomylky_5xx = []

with open("data/access.log", encoding="utf-8") as f:
    for line in f:
        m = pattern.match(line)
        if not m:
            propushcheno += 1
            continue
        rozibrano += 1

        ip_counter[m["ip"]] += 1
        status_counter[m["status"]] += 1

        if m["status"].startswith("5"):
            pomylky_5xx.append((m["time"], m["path"]))

# 1. Скільки розібрано і пропущено
print(f"Розібрано: {rozibrano}, пропущено: {propushcheno}")
print()

# 2. Топ-5 IP-адрес
print("Топ-5 IP-адрес:")
for ip, cnt in ip_counter.most_common(5):
    print(f"  {ip}: {cnt}")
print()

# 3. Кількість кожного коду відповіді
print("Коди відповіді:")
for status, cnt in sorted(status_counter.items()):
    print(f"  {status}: {cnt}")
print()

# 4. Усі запити з помилкою 5xx
print(f"Запити з помилкою 5xx ({len(pomylky_5xx)}):")
for time, path in pomylky_5xx:
    print(f"  [{time}] {path}")