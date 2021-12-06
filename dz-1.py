import re


class Date:
    def __init__(self, date):
        self.date = date

    def __str__(self):
        return f'{self.date}'

    @classmethod
    def converter(cls, date):
        instance = cls(cls.validator(date))
        return instance

    @staticmethod
    def validator(date):
        pattern = re.compile(r'(?P<day>\d{2})-(?P<month>\d{2})-(?P<year>\d+)$')
        result = pattern.match(date)
        if not result:
            raise ValueError('Некорректная дата')
        result = result.groupdict()
        for key in result.keys():
            result[key] = int(result[key])
        if result['day'] < 1 or result['day'] > 32:
            raise ValueError('Некорректное число')
        if result['month'] < 1 or result['month'] > 12:
            raise ValueError('Некорректный месяц')
        if result['year'] == 2007:
            raise ValueError('ВЕРНИТЕ 2007й!')
        return result


if __name__ == '__main__':
    my_date = Date('02-10-2021')
    print(my_date)
    my_date2 = Date.converter('06-06-2021')
    print(my_date2)