from tkinter import *
from tkinter import filedialog
import os

# создаем окно
root = Tk()

# заголовок приложения
root.title("Создатель проектов")

# функция, которая будет создавать проект
def create_project():
    # создаем переменную для хранения имени проекта
    project_name = project_name_entry.get()
    # получаем путь, куда нужно создать проект
    project_path = filedialog.askdirectory()
    # создаем папку проекта
    os.mkdir(project_path + '/' + project_name)
    # если пользователь отметил создание виртуального окружения, то создаем его
    if venv_checkbox_value.get() == 1:
        os.system('python -m venv ' + project_path + '/' + project_name + '/venv')
    # создаем файл main.py
    with open(project_path + '/' + project_name + '/main.py', 'w') as file:
        file.write('# Your code here!')
    # если пользователь отметил автоматическое открывание IDE, то открываем vscode
    if vscode_checkbox_value.get() == 1:
        os.system('code ' + project_path + '/' + project_name)

# функция, которая будет удалять проект
def delete_project():
    # получаем путь до папки проекта
    project_path = filedialog.askdirectory()
    # удаляем папку проекта
    os.system('rm -rf ' + project_path)

# создаем label и entry для ввода имени проекта
project_name_label = Label(root, text="Имя проекта:")
project_name_label.grid(row=0, column=0)
project_name_entry = Entry(root)
project_name_entry.grid(row=0, column=1)

# создаем checkbox для выбора создания виртуального окружения
venv_checkbox_value = IntVar()
venv_checkbox = Checkbutton(root, text="Создать виртуальное окружение (venv)", variable=venv_checkbox_value)
venv_checkbox.grid(row=1, column=0, columnspan=2)

# создаем checkbox для автоматического открывания IDE
vscode_checkbox_value = IntVar()
vscode_checkbox = Checkbutton(root, text="Автоматически открыть IDE (vscode)", variable=vscode_checkbox_value)
vscode_checkbox.grid(row=2, column=0, columnspan=2)

# создаем кнопку для создания проекта
create_button = Button(root, text="Создать проект", command=create_project)
create_button.grid(row=3, column=0, columnspan=2)

# создаем кнопку для удаления проекта
delete_button = Button(root, text="Удалить проект", command=delete_project)
delete_button.grid(row=4, column=0, columnspan=2)

# запускаем приложение
root.mainloop()