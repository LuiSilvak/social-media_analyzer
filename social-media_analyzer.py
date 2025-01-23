# Analisador de Dados de Redes Sociais

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Dados simulados de interações em redes sociais
data = {
    "Post-ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Date": [
        "2025-01-01", "2025-01-02", "2025-01-03", "2025-01-04", "2025-01-05", 
        "2025-01-06", "2025-01-07", "2025-01-08", "2025-01-09", "2025-01-10" 
    ],
    "Likes": [150, 300, 250, 400, 350, 500, 450, 300, 200, 100],
    "Comments": [15, 30, 25, 40, 35, 50, 45, 30, 20, 10],
    "Shares": [10, 20, 15, 25, 20, 30, 25, 20, 15, 5],
}


# Criando um DataFrame
df = pd.DataFrame(data)

# Convertendo a coluna Date para o formato datetime
df["Date"] = pd.to_datetime(df["Date"])

# Adicionando uma coluna de engajamento total
df["Total_Engagement"] = df["Likes"] + df["Comments"] + df["Shares"]

# Resumo estatístico dos dados
print("Resumo Estatístico:")
print(df.describe())

# Identificando a postagem com maior engajamento
most_engaging_post = df.loc[df["Total_Engagement"].idxmax()]
print("\n Postagem com maior engajamento: ")
print(most_engaging_post)


# Visualização: Gráfico de engajamento total ao longo do tempo
plt.figure(figsize=(10, 6))
sns.lineplot(x="Date", y="Total_Engagement", data=df, marker="o", label="Engajamento Total")
plt.title("Engajamento Total por Data")
plt.xlabel("Data")
plt.ylabel("Engajamento Total")
plt.grid()
plt.legend()
plt.show()


# Visualização: Gráfico de barras para curtidas, comentários e compartilhamentos
df_plot = df.melt(id_vars=["Post_ID"], value_vars=["Likes", "Comments", "Shares"],
                  var_name="Interaction_Type", value_name="Count")

plt.figure(figsize=(10, 6))
sns.barplot(x="Post_ID", y="Count", hue="Interaction_Type", data=df_plot)
plt.title("Interações por Tipo e Postagem")
plt.xlabel("ID da Postagem")
plt.ylabel("Quantidade")
plt.legend(title="Tipo de Interação")
plt.grid(axis="y")
plt.show()