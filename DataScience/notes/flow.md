# Data analisys flow
```mermaid
flowchart TD
    A((Início)) --> B[Receber demanda]
    B --> C[Fazer perguntas]
    C --> D{Ficou tudo claro?}

    %% Se não estiver claro
    D -->|Não| E{Pendência tem grande impacto?}
    E -->|Sim| C
    E -->|Não| F[Alinhar expectativa]

    %% Se estiver claro
    D -->|Sim| F

    %% Continuação do fluxo
    F --> G[Descrever como será a entrega]
    G --> H{Solicitante concordou?}

    H -->|Sim| I([Seguir execução])
    H -->|Não| C