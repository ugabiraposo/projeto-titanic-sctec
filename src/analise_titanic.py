import os
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("graficos", exist_ok=True)

df = pd.read_csv("data/titanic_dataset.csv")

print("Primeiras linhas do dataset:")
print(df.head())

print("\nInformações gerais:")
print(df.info())

print("\nEstatísticas descritivas:")
print(df.describe(include="all"))

print("\nTipos das colunas:")
print(df.dtypes)

print("\nValores nulos por coluna:")
print(df.isnull().sum())

print("\nQuantidade de linhas duplicadas:")
print(df.duplicated().sum())

df = df.drop_duplicates()

if "Age" in df.columns:
    df["Age"] = df["Age"].fillna(df["Age"].median())

if "Embarked" in df.columns:
    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

if "Cabin" in df.columns:
    df["Cabin"] = df["Cabin"].fillna("Nao informado")


def faixa_etaria(idade):
    if idade <= 12:
        return "Crianca"
    elif idade <= 24:
        return "Jovem"
    elif idade <= 59:
        return "Adulto"
    else:
        return "Idoso"


if "Age" in df.columns:
    df["Faixa_Etaria"] = df["Age"].apply(faixa_etaria)

print("\nQuantidade por faixa etaria:")
print(df["Faixa_Etaria"].value_counts())

if {"Name", "Age", "Sex", "Survived"}.issubset(df.columns):
    print("\nPassageiros menores de 18 anos:")
    print(df[df["Age"] < 18][["Name", "Age", "Sex", "Survived"]].head(10))

if {"Name", "Fare"}.issubset(df.columns):
    print("\nMaiores tarifas:")
    print(df.sort_values(by="Fare", ascending=False)[["Name", "Fare"]].head(10))

sobrevivencia_por_sexo = df.groupby("Sex")["Survived"].mean()
print("\nTaxa de sobrevivencia por sexo:")
print(sobrevivencia_por_sexo)

tarifa_por_classe = df.groupby("Pclass")["Fare"].mean()
print("\nTarifa media por classe:")
print(tarifa_por_classe)

sobrevivencia_por_classe = df.groupby("Pclass")["Survived"].mean()
print("\nTaxa de sobrevivencia por classe:")
print(sobrevivencia_por_classe)

pessoas_por_classe = df["Pclass"].value_counts().sort_index()
print("\nQuantidade de pessoas por classe:")
print(pessoas_por_classe)

sobreviventes_por_classe = df[df["Survived"] == 1]["Pclass"].value_counts().sort_index()
print("\nQuantidade de sobreviventes por classe:")
print(sobreviventes_por_classe)

faixas = df["Faixa_Etaria"].value_counts()

sobrevivencia_geral = df["Survived"].value_counts().sort_index()
plt.figure(figsize=(8, 5))
plt.bar(["Nao sobreviveu", "Sobreviveu"], sobrevivencia_geral.values)
plt.title("Distribuicao Geral de Sobrevivencia")
plt.ylabel("Quantidade de passageiros")
plt.tight_layout()
plt.savefig("graficos/01_sobrevivencia_geral.png")
plt.close()

plt.figure(figsize=(8, 5))
plt.bar(sobrevivencia_por_sexo.index, sobrevivencia_por_sexo.values)
plt.title("Taxa de Sobrevivencia por Sexo")
plt.ylabel("Taxa de sobrevivencia")
plt.tight_layout()
plt.savefig("graficos/02_sobrevivencia_por_sexo.png")
plt.close()

plt.figure(figsize=(8, 5))
plt.bar(tarifa_por_classe.index.astype(str), tarifa_por_classe.values)
plt.title("Tarifa Media por Classe")
plt.xlabel("Classe")
plt.ylabel("Tarifa media")
plt.tight_layout()
plt.savefig("graficos/03_tarifa_por_classe.png")
plt.close()

plt.figure(figsize=(7, 7))
plt.pie(faixas.values, labels=faixas.index, autopct="%1.1f%%")
plt.title("Distribuicao por Faixa Etaria")
plt.tight_layout()
plt.savefig("graficos/04_faixa_etaria_pizza.png")
plt.close()

plt.figure(figsize=(8, 5))
plt.bar(pessoas_por_classe.index.astype(str), pessoas_por_classe.values)
plt.title("Quantidade de Pessoas por Classe")
plt.xlabel("Classe")
plt.ylabel("Quantidade")
plt.tight_layout()
plt.savefig("graficos/05_pessoas_por_classe.png")
plt.close()

plt.figure(figsize=(8, 5))
plt.bar(sobreviventes_por_classe.index.astype(str), sobreviventes_por_classe.values)
plt.title("Sobreviventes por Classe")
plt.xlabel("Classe")
plt.ylabel("Quantidade")
plt.tight_layout()
plt.savefig("graficos/06_sobreviventes_por_classe.png")
plt.close()

print("\nAnalise concluida com sucesso.")
print("Os graficos foram salvos na pasta graficos.")


