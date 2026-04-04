# Data analisys flow
```mermaid
flowchart LR
    A((Início)) --> B[Receber demanda]
    B --> C[Fazer perguntas]
    C --> D{Ficou tudo claro?}

    %% Caminho SIM (vai para a direita)
    D -->|Sim| E[Alinhar expectativa]
    E --> F[Descrever como será a entrega]
    F --> G{Solicitante concordou?}
    G -->|Sim| H([Seguir execução])
    G -->|Não| C

    %% Caminho NÃO (desce)
    D -->|Não| I{Pendência tem grande impacto?}
    I -->|Sim| C
    I -->|Não| E
