from sqlite3.dbapi2 import Cursor
from tkinter import ttk
from tkinter import *
import sqlite3


class alumno:
    
    db_name='database.s3db'
    
    def ejecutarSql(self,sql,parametros=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor= conn.cursor()
            resultado=cursor.execute(sql,parametros)
            conn.commit()
        return resultado
    
    def readAlumnos(self):
        rsAlumnos=self.trvAlumnos.get_children()
        #limpiar la tabla
        for a in rsAlumnos:
            self.trvAlumnos.delete(a)
            
        sqlAlumnos = 'SELECT * FROM ALUMNOS'
        resultado= self.ejecutarSql(sqlAlumnos)
        for fila in resultado:
            self.trvAlumnos.insert('',0,text=fila[0],values=fila[1])
            
    def createAlumno(self):
        sqlInsertAlumno="insert into alumnos values (?,?)"
        parametros=(self.nombre.get(),self.email.get())
        self.ejecutarSql(sqlInsertAlumno,parametros)
        self.readAlumnos()
            
            
    def __init__(self,window):
        self.wind=window
        self.wind.title('Alumnosss')
        
        #CREACION DE FRAME
        #PADY=SEPARACION CON LA PARTE SUPERIOR
        # .GRID =METODO PARA POSICIONARLO EN LA VENTANA
        frame =LabelFrame(self.wind,text='Regsitro de nuevo alumno')
        frame.grid(row=0,column=0,columnspan=3,pady=20)
        
        #CAMPOS DEL FORMULARIO
        #AGREGAR CAMPO NOMBRE (ROW=FILA)
        #CREACION DE LABEL PARA NOMBRE
        lbNombre= Label(frame,text='Nombre :')
        lbNombre.grid(row=1,column=0)
        #TEXFIELD PARA NOMBRE
        #ENTRY = CAJA DE TEXTO
        self.nombre=Entry(frame)
        self.nombre.grid(row=1,column=1)  
        
        #LABEL PARA NOMBRE DEL EMAIL
        lbEmail=Label(frame,text='Email :')
        lbEmail.grid(row=2,column=0)
        #TEXT FIELD PARA EMAIL
        self.email=Entry(frame)
        self.email.grid(row=2,column=1)
    
        #LABEL PARA CELULAR 
        lbCelular=Label(frame,text='Celular :')
        lbCelular.grid(row=3,column=0)
        #TEXTFIELD PARA CELULAR
        self.celular=Entry(frame)
        self.celular.grid(row=3,column=1)
        
        #BOTON 
        btnNUevoalumno=Button(frame,text='Registrar alumno',command=self.createAlumno)
        btnNUevoalumno.grid(row=3,columnspan=2,sticky=W+E)
        
        self.trvAlumnos=ttk.Treeview(height=10,columns=2)
        self.trvAlumnos.grid(row=5,column=0,columnspan=2)
        self.trvAlumnos.heading('#0',text='Nombre', anchor=CENTER)
        self.trvAlumnos.heading('#1',text='Email',anchor=CENTER)
        #trvAlumnos.heading('#2',text='Celular',anchor=CENTER)
        
        self.readAlumnos()
                 
    
    
    
window=Tk()
app=alumno(window)
window.mainloop()
