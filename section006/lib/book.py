class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int

    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date



BOOKS = [
    Book(1, "구조주의언어학", "소쉬르,", "언어학강의", 3, 1950),
    Book(2, "생성문법", "촘스키", "깨부심", 5, 1990),
    Book(3, "문학이론", "테리이글턴", "번역개판", 2, 1980),
    Book(4, "예술미학론", "바흐찐", "잼짐", 5, 2000),
    Book(5, "꿈의해석", "프로이트", "나쁨", 3, 1980),
    Book(6, "언어", "라깡", "존잼", 5, 2026)
]