Desafio Técnico - Vaga de Desenvolvedor Python | C2S

Objetivos:
- Criar um modelo para representar automóveis com pelo menos 10 atributos relevantes;
- Popular o banco com dados fictícios;
- Realizar comunicação cliente-servidor via protocolo MCP;
- Montar uma aplicação que roda direto no terminal com interação via agente virtual;
- Criar testes automatizados;

### INSTRUÇÕES ###

Todos os comandos devem ser executados à partir da raíz do projeto

1. Instalar dependências com o comando "pip install -r app/requirements.txt"
2. Criar um banco PostgreSQL chamado c2s com seu usuário e senha;
3. criar um arquivo chamado ".env" na pasta app com o seguinte conteúdo:
DATABASE_URL=postgresql://SEU_USUARIO:SUA_SENHA@localhost:5432/c2s;
4. Inicializar as tabelas de dados com o comando "python -m app.init_db";
5. Popular o banco com dados fictícios usando "$env:PYTHONPATH="."; python -m app.scripts.populate_auto";
6. Iniciar o servidor FastAPI com "uvicorn app.main:app --reload";
7. Rodar o programa com o comando "python client/agent.py" à partir de sua pasta raíz (em um terminal diferente do passo 6);
8. Informar o carro que deseja usando linguagem natural;
