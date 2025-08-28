# data structures

# could define a Contact class or any data models. This is useful to move from simple dictionaries to a more structured system or use an ORM like SQLAlchemy.

class Contact:
    def __init__(self, id, name, email, phone=None):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone
        }