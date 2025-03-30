turmas = int(input('Digite a quantidade de turmas: '))
alunos_totais = int(input('Digite a quantidade total de alunos: '))

media_alunos = alunos_totais / turmas

print(f'A média de alunos por turma é {media_alunos}.')

if media_alunos > 40:
    print('A média de alunos por turma é maior que 40.')