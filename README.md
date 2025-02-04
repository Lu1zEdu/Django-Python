# Site de Receitas em Django

## 📌 Sobre o Projeto
Este repositório contém um site completo de receitas desenvolvido com Django. O objetivo é oferecer uma plataforma onde usuários possam visualizar, cadastrar e compartilhar receitas culinárias.

## 📖 Funcionalidades
- 📌 **Cadastro e Login de Usuários**: Sistema de autenticação para que os usuários possam gerenciar suas receitas.
- 🍽 **Gerenciamento de Receitas**: Adicionar, editar e excluir receitas.
- 🔎 **Busca Avançada**: Filtragem de receitas por nome, ingredientes ou categorias.
- 📸 **Upload de Imagens**: Permite adicionar imagens às receitas.
- ⭐ **Favoritos e Avaliações**: Usuários podem favoritar e avaliar receitas.

## 🛠 Tecnologias Utilizadas
- **Django** (Framework Web em Python)
- **SQLite / PostgreSQL** (Banco de Dados)
- **Bootstrap / Tailwind CSS** (Estilização e layout responsivo)
- **JavaScript** (Interatividade no frontend)
- **Git e GitHub** (Versionamento de código)

## 🚀 Como Utilizar
1. Clone este repositório:
   ```bash
   git clone https://github.com/Lu1zEdu/Django-Python
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd AluraReceitas
   ```
3. Crie um ambiente virtual e instale as dependências:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use: venv\Scripts\activate
   pip install -r requirements.txt
   ```
4. Execute as migrações do banco de dados:
   ```bash
   python manage.py migrate
   ```
5. Inicie o servidor local:
   ```bash
   python manage.py runserver
   ```
6. Acesse o site em `http://127.0.0.1:8000/`

## 🤝 Contribuição
Sinta-se à vontade para contribuir com melhorias, novos recursos e correções. Para isso:
1. Faça um fork do repositório.
2. Crie um branch para suas alterações (`git checkout -b minha-contribuicao`).
3. Faça o commit (`git commit -m 'Adicionando nova funcionalidade'`).
4. Envie um push para o branch (`git push origin minha-contribuicao`).
5. Abra um Pull Request.

---
💡 **Dica**: Caso tenha dúvidas ou sugestões, sinta-se à vontade para abrir uma issue!
