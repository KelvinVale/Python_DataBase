import PySimpleGUI as sg
#import tkinter as tk

from db_functions import *
# Data Base Manipulation Functions:
#
# Add_member()
# Remove_member()
# Show_members()

sg.theme('DarkAmber')

# Funções BEGIN
def Generate_Add_Window():
	layout_Add = [  [sg.Text('Digite os dados do contato')],
		[sg.Text('Nome'), sg.InputText()],
		[sg.Text('Idade'), sg.InputText()],
		[sg.Button('Salvar'), sg.Button('Cancelar')]]
	janela_Add = sg.Window("Add Contact").layout(layout_Add)
	while True:
		button, values = janela_Add.Read()
		if button == 'Salvar':
			Add_member(nome = values[0], idade = values[1])
			janela_Add.close()
			break
			pass
		if button == 'Cancelar':
			janela_Add.close()
			break
			pass
		pass
	pass

def Generate_Remove_Window():
	layout_Remove = [  [sg.Text('Digite o nome do contato a ser removido')],
		[sg.Text('Nome'), sg.InputText()],
		[sg.Button('Excluir'), sg.Button('Cancelar')]]
	janela_Remove = sg.Window("Remove Contact").layout(layout_Remove)
	while True:
		button, values = janela_Remove.Read()
		if button == 'Excluir':
			Remove_member(nome = values[0])
			janela_Remove.close()
			break
			pass
		if button == 'Cancelar':
			janela_Remove.close()
			break
			pass
		pass
	pass

def Generate_Show_members_Window():
	my_text = Show_members()
	sg.ScrolledTextBox('Lista de membros', my_text)
	pass
# Funções END





# Layouts BEGIN
layout_Menu = [  [sg.Text('Escolha o que queres fazer')],
	[sg.Button('Enviar Contato'), sg.Button('Remover Contato'), sg.Button('Mostar Lista'), sg.Button('Exit')]]

layout_Add = [  [sg.Text('Digite os dados do contato')],
	[sg.Text('Nome'), sg.InputText()],
	[sg.Text('Idade'), sg.InputText()],
	[sg.Button('Salvar'), sg.Button('Cancelar')]]

layout_Remove = [  [sg.Text('Digite o nome do contato a ser removido')],
	[sg.Text('Nome'), sg.InputText()],
	[sg.Button('Excluir'), sg.Button('Cancelar')]]
# Layouts END

janela_Menu = sg.Window("Menu").layout(layout_Menu)

while True:
	button, values = janela_Menu.Read()
	if button == 'Exit':
		break
	else:
		if button == 'Enviar Contato':
			Generate_Add_Window()
			pass

		
		elif button == 'Remover Contato':
			Generate_Remove_Window()
			pass

		elif button == 'Mostar Lista':
			Generate_Show_members_Window()
			pass
		elif button in (None, 'Exit'):
			janela_Menu.close()
			pass
	pass

