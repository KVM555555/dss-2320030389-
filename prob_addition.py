def addition_rule(p_a, p_b, p_a_and_b):
    return p_a + p_b - p_a_and_b

p_red = 26 / 52
p_face = 12 / 52
p_red_and_face = 6 / 52

# Applying addition rule
result = addition_rule(p_red, p_face, p_red_and_face)
print(f"P(Red or Face Card): {round(result, 3)}")