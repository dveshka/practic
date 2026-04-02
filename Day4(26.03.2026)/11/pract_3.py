import re

string = "22.12.2026 или 24.03.2026 или 55.12.2026 или 12.23.2026 "

sub = re.findall(r"(0[1-9]|[12][0-9]|3[0-1]).(0[1-9]|1[0-2]).(\d{4})", string)

print(sub)

d = ""
for date in sub:
    for i in range(len(date)):
        if i == 2:
            d = d + date[i]
        else:
            d = d + date[i] + "."
    print(d)
    d = ""

