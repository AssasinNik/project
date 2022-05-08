import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow
import random
import math
import argparse
import os
import subprocess

class CurrencyConv(QtWidgets.QMainWindow):
    def __init__(self):
        super(CurrencyConv, self).__init__()
        self.ui= Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()
    def init_UI(self):
        self.setWindowTitle('Генератор вариантов')
        self.setWindowIcon(QIcon('C:/Users/1/Desktop/проект/итог/imgonline-com-ua-Resize-pLA8idXrMUrYrqm-removebg-preview.png'))
        self.ui.lineEdit.setPlaceholderText('Введите количество номеров:')
        self.ui.type.addItem("  Выберите тип задач:", 0)
        self.ui.type.addItem("  Система уравнений и неравенств",1)
        self.ui.type.addItem("  Уравнения и неравенства",2)
        self.ui.type.addItem("  Квадратные уравнения",3)
        self.ui.uroven.addItem("  Выберите сложность:", 0)
        self.ui.uroven.addItem("  Первый уровень – базовый",1)
        self.ui.uroven.addItem("  Второй уровень – промежуточный",2)
        self.ui.uroven.addItem("  Третий уровень – средний",3)
        self.ui.uroven.addItem("  Четвертый уровень – промежуточный",4)
        self.ui.uroven.addItem("  Пятый уровень – сложный",5)
        
        
        
        self.ui.pushButton.clicked.connect(self.variant)

    def variant(self):
        c=CurrencyConv()
        typeof=str(self.ui.type.currentText())[2:]
        kol=int(self.ui.lineEdit.text())
        ur=str(self.ui.uroven.currentText())[2:]
        difficulty=0
        if ur=='Первый уровень – базовый':
            difficulty=1
        if ur=='Второй уровень – промежуточный':
            difficulty=2
        if ur=='Третий уровень – средний':
            difficulty=3
        if ur=='Четвертый уровень – промежуточный':
            difficulty=4
        if ur=='Пятый уровень – сложный':
            difficulty=5
        if typeof=='Система уравнений и неравенств':
            choice=['+','-','*','/']
            choice2=[r'\leq', r'\geq', '<', '>', '=']
            f=open("Variant.tex","w")
            data=[]
            data.append(r'\documentclass{article}')
            data.append(r'\begin{document}')
            data.append(r'\begin{center}')
            data.append(r'{\huge Variant}')
            data.append(r'\end{center}')
            data.append(' ')
            z=1
            if difficulty==1:
                while z<=kol:
                    data.append('Number '+str(z))
                    data.append(' ')
                    data.append('Solve a system of linear equations')
                    data.append(' ')
                    data.append(r'$\left.')
                    data.append(r'\begin{array}{ccc}')
                    data.append(str(random.randint(1,1000))+'x'+random.choice(choice)+str(random.randint(1,1000))+'y'+' '+random.choice(choice2)+' '+str(random.randint(0,1000))+r' \\')
                    data.append(str(random.randint(1,1000))+'x'+random.choice(choice)+str(random.randint(1,1000))+'y'+'='+str(random.randint(1,100))+r' \\')
                    data.append(r'\end{array}')
                    data.append(r'\right\}$')
                    data.append(' ')
                    z+=1
            if difficulty==2:
                while z<=kol:
                    data.append('Number '+str(z))
                    data.append(' ')
                    data.append('Solve a system of linear equations')
                    data.append(' ')
                    data.append(r'$\left.')
                    data.append(r'\begin{array}{ccc}')
                    data.append('('+str(random.randint(1,1000))+'x'+random.choice(choice)+str(random.randint(1,1000))+')'+random.choice(choice)+'('+str(random.randint(1,1000))+'y'+random.choice(choice)+str(random.randint(1,1000))+')'+' '+random.choice(choice2)+' '+str(random.randint(0,1000))+r' \\')
                    data.append(str(random.randint(1,1000))+'x'+random.choice(choice)+str(random.randint(1,1000))+'y'+'='+str(random.randint(1,100))+r' \\')
                    data.append(r'\end{array}')
                    data.append(r'\right\}$')
                    data.append(' ')
                    z+=1
            if difficulty>=3:
                while z<=kol:
                    data.append('Number '+str(z))
                    data.append(' ')
                    data.append('Solve a system of linear equations')
                    data.append(' ')
                    data.append(r'$\left.')
                    data.append(r'\begin{array}{ccc}')
                    data.append(r'\frac{'+str(random.randint(1,1000))+'x'+random.choice(choice)+str(random.randint(1,1000))+'}'+'{'+str(random.randint(1,1000))+'x'+random.choice(choice)+str(random.randint(1,1000))+'}'+' '+random.choice(choice2)+' '+str(random.randint(0,1000))+r' \\')
                    data.append('('+str(random.randint(1,1000))+'x'+random.choice(choice)+str(random.randint(1,1000))+')'+random.choice(choice)+'('+str(random.randint(1,1000))+'y'+random.choice(choice)+str(random.randint(1,1000))+')'+' '+random.choice(choice2)+' '+str(random.randint(0,1000))+r' \\')
                    data.append(r'\end{array}')
                    data.append(r'\right\}$')
                    data.append(' ')
                    z+=1
            data.append(r'\end{document}')
            for element in data:
                f.writelines(element+'\n')
            f.close()
        if typeof=='Уравнения и неравенства':
            choice=['+','-','*','/']
            choice2=[r'\leq', r'\geq', '<', '>', '=']
            f=open("Variant.tex","w")
            data=[]
            data.append(r'\documentclass{article}')
            data.append(r'\begin{document}')
            data.append(r'\begin{center}')
            data.append(r'{\huge Variant}')
            data.append(r'\end{center}')
            data.append(' ')
            z=1
            if difficulty==1:
                while z<=kol:
                    data.append('Number '+str(z))
                    data.append(' ')
                    data.append('Solve the linear equation or inequality')
                    data.append(' ')
                    data.append('$'+ str(random.randint(1,1000))+'x'+random.choice(choice)+str(random.randint(1,1000))+' '+random.choice(choice2)+' '+str(random.randint(0,1000)) +'$')
                    data.append(' ')
                    z+=1
            if difficulty==2:
                while z<=kol:
                    data.append('Number '+str(z))
                    data.append(' ')
                    data.append('Solve the linear equation or inequality')
                    data.append(' ')
                    data.append('$'+ '('+str(random.randint(1,1000))+'x'+random.choice(choice)+str(random.randint(1,1000))+')'+random.choice(choice)+'('+str(random.randint(1,1000))+'x'+random.choice(choice)+str(random.randint(1,1000))+')'+' '+random.choice(choice2)+' '+str(random.randint(0,1000)) +'$')
                    data.append(' ')
                    z+=1
            if difficulty>=3:
                while z<=kol:
                    data.append('Number '+str(z))
                    data.append(' ')
                    data.append('Solve the linear equation or inequality')
                    data.append(' ')
                    data.append('$'+r'\frac{'+str(random.randint(1,1000))+'x'+random.choice(choice)+str(random.randint(1,1000))+'}'+'{'+str(random.randint(1,1000))+'x'+random.choice(choice)+str(random.randint(1,1000))+'}'+' '+random.choice(choice2)+' '+str(random.randint(0,1000)) +'$')
                    data.append(' ')
                    z+=1
            data.append('\end{document}')
            for element in data:
                f.writelines(element+'\n')
            f.close()
        if typeof=='Квадратные уравнения':
            choice=['+','-']
            f=open("Variant.tex","w")
            data=[]
            data.append(r'\documentclass{article}')
            data.append(r'\begin{document}')
            data.append(r'\begin{center}')
            data.append(r'{\huge Variant}')
            data.append(r'\end{center}')
            data.append(' ')
            z=1
            if difficulty==1:
                while z<=kol:
                    data.append('Number '+str(z))
                    data.append(' ')
                    data.append('Solve the quadratic equation')
                    data.append(' ')
                    data.append('$'+ str(random.randint(1,10))+'x'+'^2'+' '+'='+str(random.randint(1,200))+'$')
                    data.append(' ')
                    z+=1
                data.append('\end{document}')
            if difficulty==2:
                while z<=kol:
                    data.append('Number '+str(z))
                    data.append(' ')
                    data.append('Solve the quadratic equation')
                    data.append(' ')
                    data.append('$'+ str(random.randint(1,10))+'x'+'^2'+random.choice(choice)+str(random.randint(1,1000))+'='+str(random.randint(1,100))+'$')
                    data.append(' ')
                    z+=1
                data.append('\end{document}')
            if difficulty==3:
                while z<=kol:
                    data.append('Number '+str(z))
                    data.append(' ')
                    data.append('Solve the quadratic equation')
                    data.append(' ')
                    data.append('$'+ str(random.randint(1,1000))+'x'+'^2'+random.choice(choice)+str(random.randint(1,10))+'x'+' '+'='+str(random.randint(0,1000))+'$')
                    data.append(' ')
                    z+=1
                data.append('\end{document}')
            if difficulty>=4:
                while z<=kol:
                    data.append('Number '+str(z))
                    data.append(' ')
                    data.append('Solve the quadratic equation')
                    data.append(' ')
                    data.append('$'+ str(random.randint(1,100))+'x'+'^2'+random.choice(choice)+str(random.randint(1,100))+'x'+random.choice(choice)+str(random.randint(1,100))+' '+'='+str(random.randint(0,1000))+'$')
                    data.append(' ')
                    z+=1
                data.append('\end{document}')
            for element in data:
                f.writelines(element+'\n')
        f.close()   
        cmd = ['pdflatex', '-interaction', 'nonstopmode', 'Variant.tex']
        proc = subprocess.Popen(cmd)
        proc.communicate()

        retcode = proc.returncode
        if not retcode == 0:
            os.unlink('Variant.pdf')
            raise ValueError('Error {} executing command: {}'.format(retcode, ' '.join(cmd))) 

        os.unlink('Variant.tex')
        os.unlink('Variant.log')

        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Variant.aux')
        os.remove(path)
            
            
app=QtWidgets.QApplication([])
application=CurrencyConv()
application.show()

sys.exit(app.exec())
