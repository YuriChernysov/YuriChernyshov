def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print(f"{'Цельсий (°C)':<15} {'Фаренгейт (°F)':<15}")
print("-" * 30)

for celsius in range(0, 101, 10):
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius:<15} {fahrenheit:<15.2f}")
