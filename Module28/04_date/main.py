class Date:
    def __init__(self, day: int = 0, month: int = 0, year: int = 0) -> None:
        self.day = day
        self.month = month
        self.year = year

    def __str__(self) -> str:
        return f'День: {self.day} Месяц: {self.month} Год: {self.year}'

    @classmethod
    def is_date_valid(cls, new_date: str) -> bool:
        check_date = new_date.split('-')
        day, month, year = int(check_date[0]), int(check_date[1]), int(check_date[2])
        return 0 < day <= 31 and 0 < month <= 12 and 0 < year <= 9999

    @classmethod
    def from_string(cls, new_date: str) -> "Date":
        check_date = new_date.split('-')
        day, month, year = int(check_date[0]), int(check_date[1]), int(check_date[2])
        date_obj = cls(day, month, year)
        return date_obj




date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
