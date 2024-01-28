from pulp import LpProblem, LpMaximize, LpVariable

# Проблема максимізації
problem = LpProblem("Maximize", LpMaximize)

x1 = LpVariable("Лимонад", lowBound=0, cat="Integer")
x2 = LpVariable("Сік", lowBound=0, cat="Integer")

# Функція максимізації
problem += x1 + x2, "Сума"

# Обмеження
problem += 2 * x1 + x2 <= 100, "Вода"
problem += x1 <= 50, "Цукор"
problem += x1 <= 30, "ЛимоннийСік"
problem += 2 * x2 <= 40, "ФруктовеПюре"

# Розв'язання
problem.solve()

print("Лимонад:", x1.varValue)
print("Фруктовий сік:", x2.varValue)
print("Сума:", x1.varValue + x2.varValue)
