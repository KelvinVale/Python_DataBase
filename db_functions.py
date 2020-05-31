import sqlite3

def Add_member(nome, idade):
	conn = sqlite3.connect('company.db')
	curs = conn.cursor()
	
	exec_line = "insert into employee values (\'"+ nome + "\'," + idade + ");"
	
	curs.execute(exec_line)
	
	conn.commit()
	conn.close()
	pass


def Remove_member(nome):
	conn = sqlite3.connect('company.db')
	curs = conn.cursor()
	
	#nome = input('Digite o nome do membro a ser excluido:	')
	exec_line = "DELETE FROM employee WHERE ('" + nome + "' = name)"
	conn.execute(exec_line)

	conn.commit()
	conn.close()
	pass

def Show_members():
	conn = sqlite3.connect('company.db')
	curs = conn.cursor()

	exec_line = "SELECT name, age from employee"

	cursor = conn.execute(exec_line)

	List_Of_Members = ""
	for row in cursor:
		List_Of_Members = List_Of_Members + "NAME = " + row[0] + "				"
		List_Of_Members = List_Of_Members + "AGE = " + str(row[1]) + "\n"

	conn.commit()
	conn.close()

	return List_Of_Members
	pass


