# Работа не доделана до конца
line_number = 0
ans = 0
results = []

with open('3.WCData.txt', 'r') as file:
    for line in file:
        line_number += 1

        if line_number <= 2:
            continue

        parts = line.strip().split()

        if len(parts) == 3:

            time = parts[0]

            air_temp = float(parts[1])
            wind_speed = float(parts[2])

            wc_temp = 35.74 + 0.6125 * air_temp + (0.4275 * air_temp - 35.75) * wind_speed ** 0.16

            wc_effect = wc_temp - air_temp

            ans += wc_temp
            results.append(f"{time:<10}  {wc_temp:^10.1f}  {wc_effect:>10.1f} \n")


with open('3.WindChillReport.txt', 'w') as out:
    out.write(f"{'Time':<{10}}{'WC temp':^{15}}{'WC Effect':>{12}}\n")
    out.write("-" * 45 + '\n')
    for line in results:
        out.write(line)
    out.write("-" * 45 + '\n')
    out.write(f"\nThe average adjusted temperature, based on {line_number - 2} observations, was {round((ans ) /  (line_number - 2),1)}")