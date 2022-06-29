weight = 3

#ground shipping
if weight <= 2:
    cost_ground = weight * 4.5 + 20
elif weight > 2 and weight <= 6:
    cost_ground = weight * 9 + 20
elif weight > 6 and weight <= 10:
    cost_ground = weight * 12 + 20
else:
    cost_ground = weight * 14.25 + 20

print(cost_ground)