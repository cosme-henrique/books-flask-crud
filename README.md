# 📚 Biblioteca API

API REST simples para gerenciar livros em uma biblioteca.

## 🚀 Funcionalidades

- Adicionar novos livros
- Listar todos os livros
- Buscar livro por ID
- Atualizar informações dos livros
- Remover livros

## 📡 Endpoints

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/books` | Listar todos os livros |
| POST | `/books` | Adicionar novo livro |
| GET | `/books/{id}` | Buscar livro por ID |
| PUT | `/books/{id}` | Atualizar livro |
| DELETE | `/books/{id}` | Remover livro |

## 📋 Campos do Livro

- **id**: Identificador único (auto)
- **title**: Título do livro (obrigatório)
- **author**: Nome do autor (obrigatório)
- **publication_year**: Ano de publicação
- **genre**: Gênero literário