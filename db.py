import sqlite3
con = sqlite3.connect('users.db')
cursor = con.cursor()

def CreateUserDB():
	cursor = con.cursor()
	cursor.execute("CREATE TABLE IF NOT EXISTS users(name TEXT, id INT, reputation INT, money INT)")
	con.commit()

def CreateChatDB():
	cursor = con.cursor()
	cursor.execute("CREATE TABLE IF NOT EXISTS chats(chat_name TEXT, chat_id INT)") 
	con.commit()
