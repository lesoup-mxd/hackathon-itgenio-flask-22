class Question:
    max_id = 0
    def __init__(self, name, theQuestion, author, answer=""):
        self.id = Question.max_id
        self.name = name
        self.theQuestion = theQuestion
        self.author = author
        self.answer = answer
        Question.max_id += 1
