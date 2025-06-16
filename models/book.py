class Book:
  def __init__(self, id, title, author, genre, publication_year) -> None:
    self.id = id
    self.title = title
    self.author = author
    self.genre = genre
    self.publication_year = publication_year
  
  def to_dict(self):
    return {
      "id": self.id,
      "title": self.title,
      "author": self.author,
      "genre": self.genre,
      "publication_year": self.publication_year,
    }