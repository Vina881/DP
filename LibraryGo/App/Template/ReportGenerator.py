# Template Method Pattern Implementation
from abc import ABC, abstractmethod

class ReportGenerator(ABC):
    def generate(self):
        return {
            'header': self.create_header(),
            'content': self.create_content(),
            'footer': self.create_footer()
        }

    @abstractmethod
    def create_header(self):
        pass

    @abstractmethod
    def create_content(self):
        pass

    @abstractmethod
    def create_footer(self):
        pass

class BookReportGenerator(ReportGenerator):
    def create_header(self):
        return {'title': 'Book Report', 'date': datetime.now()}

    def create_content(self):
        return Book().get_report_data()

    def create_footer(self):
        return {'generated_by': 'LibraryGo System'}
