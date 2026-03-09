import uuid
from datetime import datetime
from enum import Enum

class Category(Enum):
    WORK = 'WORK'
    SCHOOL = 'SCHOOL'
    PERSONAL = 'PERSONAL'

class Status(Enum):
    TODO = 'TODO'
    PROGRESS = 'PROGRESS'
    DONE = 'DONE'

class Priority(Enum):
    MAXIMUM = 'MAXIMUM'
    LOW = 'LOW'
    NORMAL = 'NORMAL'

class Term(Enum):
    TODAY = "today"
    THIS_WEEK = "this_week"
    THIS_MONTH = "this_month"
    LONG_TERM = "long_term"

class Task:
    counter = 0
    def __init__(self, title, category, description, author, status=Status.TODO, priority=Priority.NORMAL, term=datetime.now()) -> None:
        ""
        Task.counter += 1
        self.id = Task.counter
        self.uuid = str(uuid.uuid4())

        self.title = title
        self.description = description
        self.category = category
        self.author = author
        self.status = status # todo, in-progress, done
        self.priority = priority
        self.term = term

        self.createdAt = datetime.now().strftime("%d/%m/%Y %H:%M")
        self.updatedAt = self.createdAt

        terms = {}
        if self.term == datetime.now():
            terms[Term.TODAY] = self.term
        elif self.term == datetime.now().weekday():
            terms[Term.THIS_WEEK] = self.term
        elif self.term == datetime.now().month:
            terms[Term.THIS_MONTH] = self.term
        elif self.term == datetime.now():
            terms[Term.LONG_TERM] = self.term

    def to_dict(self):
        return self.__dict__