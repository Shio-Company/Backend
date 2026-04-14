# Backend

## Pré-requisitos

Para executar este projeto, você precisará ter o Docker e o Docker Compose instalados em sua máquina. Certifique-se de ter as versões mais recentes para garantir a compatibilidade.

## Como instalar e executar

1. Clone o repositório:

```bash
git clone https://github.com/Shio-Company/Backend.git && cd Backend
```

2. Configure o ambiente:
- Crie um arquivo .env na raiz (use o .env.example como base) e garanta a permissão do script:

```bash
chmod +x entrypoint.sh
```

3. Suba os serviços:

```bash
docker compose up --build
```