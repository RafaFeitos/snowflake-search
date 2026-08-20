import matplotlib.pyplot as plt

# Tempos medidos no terminal
n_vals = [500, 1000, 2000, 4000, 8000, 16000]
t_ingenua = [0.0302, 0.1312, 0.4932, 1.9606, 7.8572, 31.7856]
t_hash = [0.0007, 0.0013, 0.0068, 0.0053, 0.0107, 0.0216]

# Configuração da figura
plt.figure(figsize=(8, 5))

# Plotando as linhas
plt.plot(n_vals, t_ingenua, marker='o', color='#e74c3c', linewidth=2, label='Solução Ingênua')
plt.plot(n_vals, t_hash, marker='s', color='#2980b9', linewidth=2, label='Tabela Hash')

# Estilização
plt.xlabel('Tamanho da Instância (N)', fontsize=12)
plt.ylabel('Tempo de Execução (s)', fontsize=12)
plt.title('Flocos de Neve: Busca Ingênua vs. Tabela Hash', fontsize=14)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

# Salva a imagem na mesma pasta
plt.savefig('grafico_flocos_final.png', dpi=300)

# Exibe o gráfico na tela
plt.show()