# Decisões do projeto

## Porta do Postgres: 5433
- Motivo: a 5432 já estava em uso na minha máquina.

## Pasta de rascunhos: exploration/
- Motivo: manter ingestion/ só para o que roda de verdade.
- Nomes de código e documentação em inglêS.

## Fonte dos dados do PySUS (a decidir)
- Padrão: espelho em S3 (source='catalog'), arquivos em Parquet.
- Alternativa: source='origin' (servidor do DATASUS).
- Hipótese: camada raw guarda tudo como texto e converte tipos na staging. A validar.
