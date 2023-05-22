#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

arquivo = float(input('Tamanho do arquivo: '))

mb = int(input('Velocidade da internet (MB): '))

print(f'Para baixar um arquivo de {arquivo}MB, com a velocidade de {mb}MB, levaira cerca de {arquivo/mb}s')