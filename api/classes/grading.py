from mysql.connector import connect, Error
from flask import current_app
from dataclasses import dataclass

@dataclass(frozen=True)
class GradingConstants:
    DENMARK = 'Denmark'
    USA = 'USA'

class Grading(GradingConstants):

    def convert(self, grade: str, system: str) -> str: 
        with connect(
            host=current_app.config['HOST'],
            user=current_app.config['USER'],
            password=current_app.config['PASSWORD'],
            database=current_app.config['DATABASE']
        ) as connection:
            with connection.cursor() as cursor:
                destination_system = f'c{self.DENMARK if system == self.USA else self.USA}'
                sql = f'''
                    SELECT {destination_system} AS 'Grade'
                    FROM grades
                    WHERE c{system} = %s;
                '''
                try:
                    cursor.execute(sql, (grade,))
                    return cursor.fetchall()[0][0]
                except Exception as e:
                    print('--- ERROR ---')
                    print(e)