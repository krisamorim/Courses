# Data analisys flow
```mermaid
flowchart LR
    A((Início)) --> B[Receber demanda]
    B --> C[Fazer perguntas]
    C --> D{Ficou tudo claro?}

<<<<<<< HEAD
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
=======
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
>>>>>>> cb5398acecc65c9e124c0aee424dfcdcde93f55d
