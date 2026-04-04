# Flowchart for receiving demand (summary)
```mermaid
flowchart LR
    A((Start)) --> B[Receive request]
    B --> C[Clarify requirements]
    C --> D{Are requirements clear?}

    %% YES path (to the right)
    D -->|Yes| E[Align expectations]
    E --> F[Outline delivery approach]
    F --> G{Does the requester agree?}
    G -->|Yes| H([Proceed with execution])
    G -->|No| C

    %% NO path (down)
    D -->|No| I{Does the gap have significant impact?}
    I -->|Yes| C
    I -->|No| E

# Flowchart for data analisys
```mermaid
flowchart TD
    A((Start)) --> B[Understand business context]
    B --> C[Identify data sources]
    C --> D[Map tables and relationships]

    D --> E[Perform data profiling]
    E --> F[Validate data types and schema]

    F --> G{Data quality issues?}

    G -->|Yes| H[Clean and standardize data]
    H --> I[Handle missing values, duplicates, outliers]
    I --> J[Re-validate data quality]

    J --> K{Data ready for analysis?}
    K -->|No| H
    K -->|Yes| L[Create curated dataset]

    G -->|No| L

    L --> M[Define metrics and KPIs]
    M --> N[Perform exploratory data analysis (EDA)]
    N --> O[Generate insights]

    O --> P[Validate findings with stakeholders]
    P --> Q[Prepare report or dashboard]

    Q --> R([End])