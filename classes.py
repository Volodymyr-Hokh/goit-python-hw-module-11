from collections import UserDict
from datetime import datetime, date


class Field:
    def __init__(self, value, required=False):
        self.value = value
        self.required = required
        if required and not value:
            raise ValueError("Required field is not provided.")

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if self.__class__ == other.__class__:
            return self.value == other.value
        return False

    def __hash__(self):
        return hash(self.value)


class Name(Field):
    pass


class Phone(Field):
    pass


class Birthday(Field):
    pass


class Record:
    def __init__(self, name, phones=None, birthday=None):
        self.name = name
        self.phones = phones
        self.birthday = birthday

    def __str__(self):
        birthday = f"birthday: {self.birthday}" if self.birthday else ""
        return f"{self.name.value}: {self.phones}, {birthday}"

    def __repr__(self):
        return str(self)

    def add_phone(self, phone: Phone):
        self.phones.append(phone)
        self.phones = list(set(self.phones))
        return f"Phone number {phone} for user {self.name.value} added successfully."

    def change_phone(self, old_number: Phone, new_number: Phone):
        if old_number not in self.phones:
            return f"Number {old_number} not found."
        else:
            phone_number_index = self.phones.index(old_number)
            self.phones[phone_number_index] = new_number
            return f"The phone number {old_number} for the user {self.name} "\
                f"has been changed to {new_number}"

    def delete_phone(self, phone):
        try:
            self.phones.remove(phone)
            return f"Phone number {phone} for user {self.name} deleted successfully."
        except ValueError:
            return f"Phone number {phone} for user {self.name} not found"

    def days_to_birthday(self):
        birthday = datetime.strptime(str(self.birthday), "%d.%m.%Y").date()
        today = date.today()
        birthday = birthday.replace(year=today.year)
        if birthday < today:
            birthday = birthday.replace(year=today.year+1)
        result = (birthday - today).days
        return f"The birthday of user {self.name} will be in {result} days"


class AddressBook(UserDict):
    def add_record(self, record):
        self[record.name.value] = record

    def delete_record(self, name: Name):
        del self[name.value]

    def change_record(self, name, new_record):
        self[new_record.name.value] = new_record


if __name__ == "__main__":
    rec = Record(Name("Ivan"), Phone("12345"), Birthday("16.08.2003"))
    print(rec.days_to_birthday())
