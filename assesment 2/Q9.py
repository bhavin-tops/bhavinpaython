#Store all questions in MySQL database create separate file for database
#connection.

CREATE TABLE IF NOT EXISTS questions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    question_text TEXT NOT NULL,
    answer TEXT NOT NULL
);
import mysql.connector

def get_db_connection():
    db_config = {
        'host': 'localhost',
        'user': 'your_username',
        'password': 'your_password',
        'database': 'questions_db'
    }
    
    try:
        connection = mysql.connector.connect(**db_config)
        return connection
    except mysql.connector.Error as err:
        print("Error:", err)
        return None

from db_connection import get_db_connection

def insert_question(question_text, answer):
    connection = get_db_connection()
    
    if connection:
        try:
            cursor = connection.cursor()
            insert_query = "INSERT INTO questions (question_text, answer) VALUES (%s, %s)"
            data = (question_text, answer)
            cursor.execute(insert_query, data)
            connection.commit()
            print("Question inserted successfully!")
        except mysql.connector.Error as err:
            print("Error:", err)
        finally:
            cursor.close()
            connection.close()

if __name__ == "__main__":
    question_text = input("Enter the question: ")
    answer = input("Enter the answer: ")
    insert_question(question_text, answer)
