def complement_rule(p_a):
    return 1 - p_a

p_rain = 0.8
p_no_rain = complement_rule(p_rain)
print(f"P(No Rain): {round(p_no_rain, 2)}")