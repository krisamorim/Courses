# Data analisys flow
```mermaid
flowchart TD
    A((Início)) --> B[Receber demanda] -->
    %%A[Início] B[Usuário insere credenciais] -->
    B --> C{Dados válidos?}
    C -->|Sim| D[Acesso liberado]
    C -->|Não| E[Exibir erro]
    D --> F[Fim]
    E --> F