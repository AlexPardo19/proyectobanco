import sqlite3
class Conexion():
    def __init__(self):
        try:
            self.con=sqlite3.connect("banco.db")
            self.creartablas()
        except Exception as ex:
            print(ex)
    def creartablas(self):
        sql_crear_tabla1="""CREATE TABLE IF NOT EXISTS usuarios
        nombre TEXT,
        usuario TEXT UNIQUE,
        clave TEXT"""
        cur= self.con.cursor()
        cur.execute(sql_crear_tabla1)
        

con= Conexion()