<!-- # Fluxo de Login

Início  
↓  
Usuário insere credenciais  
↓  
Sistema valida dados  
↓  
[Dados válidos?]  
→ Sim → Acesso liberado  
→ Não → Exibir erro  
↓  
Fim -->


# Fluxo de Login

```mermaid
flowchart TD
    A[Início] --> B[Usuário insere credenciais]
    B --> C{Dados válidos?}
    C -->|Sim| D[Acesso liberado]
    C -->|Não| E[Exibir erro]
    D --> F[Fim]
    E --> F