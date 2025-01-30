from pulp import LpMaximize, LpProblem, LpVariable

model = LpProblem(name="Maximize Production", sense=LpMaximize)

L = LpVariable(name="Lemonade", lowBound=0, cat="Integer")
F = LpVariable(name="Fruit Juice", lowBound=0, cat="Integer")

# Функція цілі: максимізація загальної кількості вироблених продуктів
model += L + F, "Total Products"

# Обмеження ресурсів
model += 2 * L + F <= 100, "Water Constraint"
model += L <= 50, "Sugar Constraint"
model += L <= 30, "Lemon Juice Constraint"
model += 2 * F <= 40, "Fruit Puree Constraint"

model.solve()

print(f"Оптимальне виробництво Лемонаду: {L.varValue}")
print(f"Оптимальне виробництво Фруктового соку: {F.varValue}")
