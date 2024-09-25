# Enunciado: Crie um programa que receba a nota de 5 alunos e exiba quantos foram aprovados (nota maior ou igual a 7).
# Inicializa o contador de alunos aprovados
aprovados = 0

# Loop para receber as notas dos 5 alunos
for i in range(1, 6):
    nota = float(input(f"Digite a nota do aluno {i}: "))
    
    # Verifica se a nota é maior ou igual a 7
if nota >= 7:
    aprovados += 1
