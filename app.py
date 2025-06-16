from flask import Flask, request, jsonify
from models.book import Book

app = Flask(__name__)

books = []
book_id_control = 1

@app.route('/books', methods=['POST'])
def create_book():
  global book_id_control
  data = request.get_json()

  if not data or not data.get('title') or not data.get('author'):
    return jsonify({"message": "Dados inválidos fornecidos"}), 400

  new_book = Book(
    id=book_id_control, 
    title=data.get('title'), 
    author=data.get('author'), 
    genre=data.get('genre', ''), 
    publication_year=data.get('publication_year', 0)
  )
  
  book_id_control += 1
  books.append(new_book)
  return jsonify({"message": "Novo livro adicionado com sucesso"})

@app.route('/books', methods=['GET'])
def get_books():
  book_list = [book.to_dict() for book in books]

  output = {
            "books": book_list,
            "total_books": len(book_list)
          }
  return jsonify(output)


if __name__ == "__main__":
  app.run(debug=True)