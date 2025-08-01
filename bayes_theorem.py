def bayes_theorem(p_b_given_a, p_a, p_b):
    return (p_b_given_a * p_a) / p_b

p_disease = 0.01
p_positive_given_disease = 0.99
p_positive = 0.05

p_disease_given_positive = bayes_theorem(p_positive_given_disease, p_disease, p_positive)
print(f"P(Disease | Positive Test): {round(p_disease_given_positive, 3)}")
