#Manage proper naming conversion – create appropriate objects name.

import mysql.connector

class DatabaseConnector:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
    
    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Connected to the database")
        except mysql.connector.Error as err:
            print("Error:", err)
    
    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Disconnected from the database")
    
    def get_connection(self):
        return self.connection

from database_connection import DatabaseConnector

class QuestionManager:
    def __init__(self, question_text, answer):
        self.question_text = question_text
        self.answer = answer
    
    def insert_question(self):
        db_connector = DatabaseConnector('localhost', 'your_username', 'your_password', 'questions_db')
        db_connector.connect()
        connection = db_connector.get_connection()

        if connection:
            try:
                cursor = connection.cursor()
                insert_query = "INSERT INTO questions (question_text, answer) VALUES (%s, %s)"
                data = (self.question_text, self.answer)
                cursor.execute(insert_query, data)
                connection.commit()
                print("Question inserted successfully!")
            except mysql.connector.Error as err:
                print("Error:", err)
            finally:
                cursor.close()
                db_connector.disconnect()

if __name__ == "__main__":
    question_text = input("Enter the question: ")
    answer = input("Enter the answer: ")
    question_manager = QuestionManager(question_text, answer)
    question_manager.insert_question()
