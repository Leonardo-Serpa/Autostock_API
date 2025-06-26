🚗 Projeto: AutoStock – Sistema de Gestão de Estoque e Vendas para Concessionária
🧩 Descrição:
Desenvolva uma API RESTful com FastAPI para gerenciar o estoque de veículos, vendas e agendamentos de test drives em uma concessionária de carros.

🔧 Funcionalidades:
👤 Módulo de Clientes:
Cadastro e autenticação de clientes

Histórico de compras e test drives

🚙 Módulo de Veículos:
Cadastro de novos carros (marca, modelo, ano, cor, status, preço)

Consulta por filtros (ex: marca, ano, valor máximo)

💰 Módulo de Vendas:
Registrar venda com cliente, carro, data, forma de pagamento

Histórico e relatórios mensais de vendas

📆 Módulo de Test Drive:
Agendamento de test drives por cliente

Limitar horários disponíveis

Cancelamentos

⚙️ Tecnologias sugeridas:
FastAPI (backend)

SQLAlchemy ou Tortoise ORM

PostgreSQL ou SQLite

Docker (containerização)

JWT Auth para login

Swagger UI (já incluso no FastAPI)

🔄 Possíveis Extensões:
Frontend com React/Vue

Integração com API de carros (ex: Fipe)

Notificações por e-mail ao agendar/cancelar test drive

