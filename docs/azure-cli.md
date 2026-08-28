# Azure CLI — Configuração do Ambiente

## Status

**Data:** 28/08/2026  
**Status:** Configurado localmente; assinatura Azure ainda não disponível na conta autenticada.

## Ambiente

Azure CLI instalado no Windows por meio do WinGet.

```powershell
winget install --exact --id Microsoft.AzureCLI
```

Versão instalada:

```text
azure-cli 2.89.1
core 2.89.1
telemetry 1.1.0
```

Python utilizado pelo Azure CLI:

```text
C:\Program Files\Microsoft SDKs\Azure\CLI2\python.exe
```

## Azure Machine Learning CLI

A extensão `ml` foi instalada com:

```powershell
az extension add --name ml
```

Versão registrada:

```text
ml 2.44.1
```

Validação realizada com:

```powershell
az ml --help
az extension show --name ml
```

A extensão está funcional e disponibiliza os comandos necessários para gerenciamento de Azure Machine Learning.

## Autenticação

O login pelo Azure CLI foi executado com:

```powershell
az login
```

Resultado observado em 28/08/2026:

```text
No subscriptions found for Filipe_gimenes@outlook.com.
```

Portanto, a autenticação Microsoft foi realizada, mas **não há assinatura Azure disponível atualmente para essa conta**.

## Limite atual

Sem uma assinatura ativa, não devem ser criados recursos Azure, como:

- Resource Group;
- Storage Account;
- Azure Machine Learning Workspace;
- Compute Instance;
- Endpoints.

O ambiente local, entretanto, já está preparado para a próxima etapa.

## Próxima etapa do projeto

Quando houver uma assinatura Azure disponível, validar novamente:

```powershell
az login
az account list --output table
```

Depois selecionar explicitamente a assinatura, quando aplicável, e somente então iniciar a configuração dos recursos do Azure Machine Learning.

## Segurança

Não armazenar no repositório:

- senhas;
- tokens;
- chaves de API;
- connection strings;
- credenciais do Azure;
- arquivos de configuração contendo segredos.
