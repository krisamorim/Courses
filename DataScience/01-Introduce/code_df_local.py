import pandas as pd
import matplotlib.pyplot as plt
import os
from pathlib import Path
# os.system('cls' if os.name == 'nt' else 'clear') 
pastaAtual = Path(__file__).resolve().parent
dfLocal = pastaAtual / "df.csv"
df = pd.read_csv(dfLocal)

# #show amount of rows and columns
# print(df.shape[0], df.shape[1])

# print(df.head())

# df["age"].hist()
# df["items_sold_last_30_days"].hist()

#===========================================================
# df["churned"].value_counts().plot(kind="bar") 
# plt.title("Status Cancelado")
# plt.xlabel("Cancelado (0: Não Cancelado, 1: Cancelado)")
# plt.ylabel("Clientes")
# plt.show()

#===========================================================
#show all rows from the column "age" 
# print(df["payment_method"].unique())

#===========================================================
# #group the dataframe by the column "payment_method" and Calculate the average of the "churned" column for each group and print the result

# #first way
# plt.bar(df["payment_method"].unique(), df.groupby("payment_method")["churned"].mean())
# plt.title("Churn Rate by Payment Method")
# plt.xlabel("Payment Method")
# plt.ylabel("Churn Rate")
# plt.show()

# #second way
# df_grp = df.groupby("payment_method")["churned"].mean()
# df_grp.plot(kind="bar")
# plt.title("Churn Rate by Payment Method")
# plt.show()

#===========================================================

# #group the dataframe by the column support_contacts_last_30_days and compute the average of the churned
# df_grp = df.groupby("support_contacts_last_30_days")["churned"].mean()
# df_grp.plot(kind="bar")
# plt.title("Churn Rate by Support Contacts Last 30 Days")
# plt.xlabel("Support Contacts Last 30 Days")
# plt.ylabel("Churn Rate")
# plt.show()

#===========================================================
# #count the number of the registrations canceled by the column "support_contacts_last_30_days" and print the result
# df_grp = df.groupby("support_contacts_last_30_days")["churned"].count()
# df_grp.plot(kind="bar")
# plt.title("Number of Cancellations by Support Contacts Last 30 Days")
# plt.xlabel("Support Contacts Last 30 Days")
# plt.ylabel("Number of Cancellations")
# plt.show()


# df_grp = df.groupby("support_contacts_last_30_days")["churned"].sum()
# df_grp.plot(kind="bar")
# plt.title("Number of Cancellations' sum by Support Contacts Last 30 Days")
# plt.xlabel("Support Contacts Last 30 Days")
# plt.ylabel("Number of Cancellations")
# plt.show()

fig, axes = plt.subplots(1, 2, figsize=(14, 5))  # 1 linha, 2 colunas

# --- Gráfico 1: count ---
df_count = df.groupby("support_contacts_last_30_days")["churned"].count()
df_count.plot(kind="bar", ax=axes[0])
axes[0].set_title("Number of Records by Support Contacts (Last 30 Days)")
axes[0].set_xlabel("Support Contacts Last 30 Days")
axes[0].set_ylabel("Count")

# --- Gráfico 2: sum ---
df_sum = df.groupby("support_contacts_last_30_days")["churned"].sum()
df_sum.plot(kind="bar", ax=axes[1])
axes[1].set_title("Number of Cancellations by Support Contacts (Last 30 Days)")
axes[1].set_xlabel("Support Contacts Last 30 Days")
axes[1].set_ylabel("Churn Sum")

plt.tight_layout()
plt.show()