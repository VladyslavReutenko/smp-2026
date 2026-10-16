# 1.1. Прочитати data/words.txt і вивести кожен рядок великими літерами
with open("data/words.txt", encoding="utf-8") as f:
    for line in f:
        print(line.strip().upper()) 


        # 1.2. У data/mbox-short.txt знайти рядки з X-DSPAM-Confidence і порахувати середнє
total = 0
count = 0
with open("data/mbox-short.txt", encoding="utf-8") as f:
    for line in f:
        if line.startswith("X-DSPAM-Confidence:"):
            parts = line.split(":")
            value = float(parts[1].strip())
            total += value
            count += 1

print(count, "рядків, середнє", total / count)