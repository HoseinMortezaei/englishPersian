from PySide2 import QtGui
from PySide2.QtWidgets import QMainWindow ,QApplication ,QSystemTrayIcon ,QAction ,QMenu ,QFileDialog ,QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from PySide2.QtGui import QClipboard,QIcon
from dictin import getit
from voice_net import speak
from voice import text_to_voice
import os
import re
try :
    from deep_translator import GoogleTranslator
except:
    pass
import threading
import sys

path = os.path.realpath(__file__)
path = re.findall(r'(.*)\\',path)[0]
os.chdir(path)

class GUI(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.check_file()
        self.text2=''
        loader = QUiLoader()
        self.win = loader.load('light_ui.ui')
        self.text_win = loader.load('text.ui')
        if self.lines[0] == '1':
            self.win.setStyleSheet(open('dark.qss').read())
            self.text_win.setStyleSheet(open('dark.qss').read())
            self.win.dark_radio.setChecked(True)
        if self.lines[1]=='0':
            self.win.taskbar.setChecked(0)
            app.setQuitOnLastWindowClosed(True)
        else:
            app.setQuitOnLastWindowClosed(False)
        self.win.setWindowIcon(QIcon('icon.png'))
        self.set_com()
        self.init_tray()
        try:
            self.win.entry.paste()
            self.win.entry_3.paste()
            self.win.entry_5.paste()
            self.win.entry_7.paste()
        except:
            pass

        self.win.show()
        
        sys.exit(app.exec_())
        
    def translate(self,first,second,text):
        try :
            def translate_1(first,second,text):
                translated = GoogleTranslator(source=first, target=second).translate(text)
                self.win.trans_label.setText(translated)
                self.win.copy_bbtn.setText('Copy')
            t = threading.Thread(target = translate_1,args=[first,second,text])
            t.start()
        except:
            pass
            
    def set_com(self):

        def savebtn():
            myfile=open('setting.txt','w')
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowIcon(QIcon('icon.png'))
            msg.setText('Successfully save changes')
            msg.setWindowTitle('Success ')
            msg.setStandardButtons(QMessageBox.Ok)
            if self.win.light_radio.isChecked():
                myfile.write('0\n')
                self.win.setStyleSheet("")
                self.text_win.setStyleSheet("")
                msg.show()
                msg.exec_()
                
            else:
                myfile.write('1\n')
                self.win.setStyleSheet(open('dark.qss').read())
                self.text_win.setStyleSheet(open('dark.qss').read())
                msg.show()
                msg.exec_()
            if self.win.taskbar.isChecked()==1:
                myfile.write('1\n')
                app.setQuitOnLastWindowClosed(False)             
            else:
                myfile.write('0\n')
                app.setQuitOnLastWindowClosed(True)
            myfile.close()
        self.win.save_btn.clicked.connect(savebtn)

        def clearbtn():
            self.win.entry.clear()
            self.win.label.setText('')
            self.text2 = ''
            self.win.copy_btn.setText('Copy')
        self.win.clear_btn.clicked.connect(clearbtn)

        def okbtn():
            
            self.text2 = self.win.entry.toPlainText()
            self.text2 = getit(self.text2)
            try:
                text = self.text2.splitlines()[0]
            except:
                text=''
            if len(text)>30:
                text = text[:80]+'...'
            self.win.label.setText(text)
            self.win.label.adjustSize()
            self.win.copy_btn.setText('Copy')
        self.win.ok_btn.clicked.connect(okbtn)

        def copybtn():
            self.text2 = self.win.entry.toPlainText()
            self.text2 = getit(self.text2)   
            clip = QClipboard()     
            clip.setText(self.text2)
            self.win.copy_btn.setText('Copied!')
        self.win.copy_btn.clicked.connect(copybtn)

        def pastebtn():
            self.win.entry.paste()
        self.win.paste_btn.clicked.connect(pastebtn)

        def set_menu_comm():
            self.win.actionPaste_2.triggered.connect(pastebtn)
            self.win.actionExit_2.triggered.connect(lambda : self.win.close())
            self.win.actionCopy_2.triggered.connect(lambda : self.win.entry.copy())
            self.win.actionCut.triggered.connect(lambda : self.win.entry.cut())
            self.win.actionRedo.triggered.connect(lambda : self.win.entry.redo())
            self.win.actionUndo.triggered.connect(lambda : self.win.entry.undo())
            def about():
                    loader = QUiLoader()
                    self.abo = loader.load('about.ui')
                    self.abo.show()
            def read_me():
                    loader = QUiLoader()
                    self.rea = loader.load('read me.ui')
                    self.rea.show()
            self.win.actionAbout.triggered.connect(about)
            self.win.actionRead_me.triggered.connect(read_me)

        self.win.clear_btn_3.clicked.connect(self.win.entry_3.clear)
        self.win.paste_btn_3.clicked.connect(self.win.entry_3.paste)
        def big3():      
            def oktext():
                text = self.text_win.textEdit.toPlainText()
                self.win.entry_3.setText(text)
                self.text_win.close()
            self.text_win.ok.clicked.connect(oktext)      
            text = self.win.entry_3.toPlainText()
            self.text_win.textEdit.setText(text)
            self.text_win.show() 
        self.win.big_3.clicked.connect(big3)    
        def say():
            if self.win.lang.currentText() == 'language':
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText('Please select your language')
                msg.setWindowTitle('language')
                msg.setWindowIcon(QIcon('icon.png'))
                msg.setStandardButtons(QMessageBox.Ok)
                msg.show()
                msg.exec_()
            else:
                if self.win.entry_3.toPlainText()!= '':
                    try :
                        speak(self.win.entry_3.toPlainText(),self.win.lang.currentText())
                    except :
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Critical)
                        msg.setText('An Error has been eccourded\nplease check your internet connection')
                        msg.setWindowTitle('Error')
                        msg.setWindowIcon(QIcon('icon.png'))
                        msg.setStandardButtons(QMessageBox.Ok)
                        msg.show()
                        msg.exec_()                        
                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText('Plase write a text , no text to speak')
                    msg.setWindowTitle('Text')
                    msg.setWindowIcon(QIcon('icon.png'))
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.show()
                    msg.exec_()
                    

        self.win.say_btn.clicked.connect(say)
        self.win.actionSay.triggered.connect(say)

        set_menu_comm()
        def select():
            fileName, _ = QFileDialog.getOpenFileName(self,"please choose your text file ...", "","Text files (*.txt);;All Files (*)")
            if fileName : 
                file = open(fileName,'r')
                lines = file.readlines()
                f = ''
                for i in lines : 
                    f += i
                self.win.entry_5.setText(f)
        self.win.select_3.clicked.connect(select)

        def select3():
            fileName, _ = QFileDialog.getOpenFileName(self,"please choose your text file ...", "","Text files (*.txt);;All Files (*)")
            if fileName : 
                file = open(fileName,'r')
                lines = file.readlines()
                f = ''
                for i in lines : 
                    f += i
                self.win.entry.setText(f)
        self.win.select.clicked.connect(select3)

        def select2():
            fileName, _ = QFileDialog.getOpenFileName(self,"please choose your text file ...", "","Text files (*.txt);;All Files (*)")
            if fileName : 
                file = open(fileName,'r')
                lines = file.readlines()
                f = ''
                for i in lines : 
                    f += i
                self.win.entry_3.setText(f)
        self.win.file_choose.clicked.connect(select2)



        def bigger():
            def oktext():
                text = self.text_win.textEdit.toPlainText()
                self.win.entry.setText(text)
                self.text_win.close()
            self.text_win.ok.clicked.connect(oktext)
            text = self.win.entry.toPlainText()
            self.text_win.textEdit.setText(text)
            self.text_win.show()
        self.win.big.clicked.connect(bigger)

        self.win.clear_bbtn.clicked.connect(self.win.entry_5.clear)
        def bigger2():
            def oktext():
                text = self.text_win.textEdit.toPlainText()
                self.win.entry_5.setText(text)
                self.text_win.close()
            self.text_win.ok.clicked.connect(oktext)
            text = self.win.entry_5.toPlainText()
            self.text_win.textEdit.setText(text)
            self.text_win.show()
        self.win.big_5.clicked.connect(bigger2)
        self.win.paste_btn_5.clicked.connect(self.win.entry_5.paste)
        def copy_bb():
            r = self.win.trans_label.text()
            clip = QClipboard()     
            clip.setText(r)
            self.win.copy_bbtn.setText('Copied!')
        self.win.copy_bbtn.clicked.connect(copy_bb)
        def reverse():
            r = self.win.f_lang.currentIndex()
            self.win.f_lang.setCurrentIndex(self.win.d_lang.currentIndex())
            self.win.d_lang.setCurrentIndex(r)
        self.win.reverse.clicked.connect(reverse)
        def tr():
            r = self.win.f_lang.currentText()
            d = self.win.d_lang.currentText()
            if r=='Language' or d=='Language':
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText('Please select language')
                msg.setWindowTitle('Language')
                msg.setWindowIcon(QIcon('icon.png'))
                msg.setStandardButtons(QMessageBox.Ok)
                msg.show()
                msg.exec_()
            else:
                r2 = self.win.entry_5.toPlainText()
                if r2!='':
                    try :
                        self.translate(r.lower(),d.lower(),r2)
                    except :
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Critical)
                        msg.setText("could't connect \nplease check your intenet connection")
                        msg.setWindowTitle('Network')
                        msg.setWindowIcon(QIcon('icon.png'))
                        msg.setStandardButtons(QMessageBox.Ok)
                        msg.show()
                        msg.exec_()                        
                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText('Plase write a text')
                    msg.setWindowTitle('Text')
                    msg.setWindowIcon(QIcon('icon.png'))
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.show()
                    msg.exec_()
        self.win.translate.clicked.connect(tr)

        def select4():
            fileName, _ = QFileDialog.getOpenFileName(self,"please choose your text file ...", "","Text files (*.txt);;All Files (*)")
            if fileName : 
                file = open(fileName,'r')
                lines = file.readlines()
                f = ''
                for i in lines : 
                    f += i
                self.win.entry_7.setText(f)
        self.win.clear_btn_5.clicked.connect(self.win.entry_7.clear)
        self.win.paste_btn_7.clicked.connect(self.win.entry_7.paste)
        self.win.file_choose_3.clicked.connect(select4)
        def bigger3():
            def oktext():
                text = self.text_win.textEdit.toPlainText()
                self.win.entry_7.setText(text)
                self.text_win.close()
            self.text_win.ok.clicked.connect(oktext)
            text = self.win.entry_7.toPlainText()
            self.text_win.textEdit.setText(text)
            self.text_win.show()
        self.win.big_7.clicked.connect(bigger3)
        self.win.say_btn_3.clicked.connect(lambda :text_to_voice(self.win.entry_7.toPlainText()))
        
    def check_file(self):
        try : 
            myfile = open('setting.txt','r')
            self.lines = myfile.read().splitlines()
        except:
            myfile = open('setting.txt','w')
            myfile.write('0\n1\n')
            myfile.close()
            self.lines = '0\n1\n'.splitlines()
        myfile.close()
    def init_tray(self):
        self.tray_icon = QSystemTrayIcon(self.win)
        self.tray_icon.setIcon(QIcon('icon.png'))
        show_action = QAction("Show", self.win)
        quit_action = QAction("Exit", self.win)
        hide_action = QAction("Hide", self.win)
        def show_task():
            self.win.entry.paste()
            self.win.show()
        show_action.triggered.connect(show_task)
        hide_action.triggered.connect(self.win.hide)
        quit_action.triggered.connect(qApp.quit)
        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI()
    
    
