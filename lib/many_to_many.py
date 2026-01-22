class Book:
    # Class variable to track all books
    all = []
    
    def __init__(self, title):
        self._title = title
        Book.all.append(self)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise Exception("Title must be a string")
        self._title = value
    
    def contracts(self):
        """Return all contracts for this book"""
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        """Return all authors for this book"""
        return [contract.author for contract in self.contracts()]


class Author:
    # Class variable to track all authors
    all = []
    
    def __init__(self, name):
        self._name = name
        Author.all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be a string")
        self._name = value
    
    def contracts(self):
        """Return all contracts for this author"""
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        """Return all books by this author"""
        return [contract.book for contract in self.contracts()]
    
    def sign_contract(self, book, date, royalties):
        """Create and return a new Contract object"""
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")
        
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        """Return total royalties from all contracts"""
        return sum(contract.royalties for contract in self.contracts())


class Contract:
    # Class variable to track all contracts
    all = []
    
    def __init__(self, author, book, date, royalties):
        self.author = author  # Using property setter
        self.book = book      # Using property setter
        self.date = date      # Using property setter
        self.royalties = royalties  # Using property setter
        Contract.all.append(self)
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("author must be an instance of Author")
        self._author = value
    
    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("book must be an instance of Book")
        self._book = value
    
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception("date must be a string")
        self._date = value
    
    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception("royalties must be an integer")
        self._royalties = value
    
    @classmethod
    def contracts_by_date(cls, date):
        """Return all contracts with the specified date"""
        if not isinstance(date, str):
            raise Exception("date must be a string")
        
        return [contract for contract in cls.all if contract.date == date]