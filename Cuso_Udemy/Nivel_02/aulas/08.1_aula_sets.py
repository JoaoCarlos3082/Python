# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Seus valores serão sempre únicos;
# - Não aceitam valores mutáveis;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

s1 = set()  # vazio
s1 = {'Luiz', 1, 2, 3}  # com dados

print(2 in s1)