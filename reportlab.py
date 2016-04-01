from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
import time
import datetime
import sqlite3 as dbapi

class Historial:
    def __init__(self):
        #Conexion con la base de datos
        self.bd = dbapi.connect("basedatos.dat")
        self.cursor = self.bd.cursor()
        self.elementos = []

    def pdf(self):
        historialpdf = "Historial clientes_" + str(datetime.date.today()) +"_.pdf"
        c = canvas.Canvas(historialpdf, pagesize=A4)
        self.logo = "../img/default-icon.jpg"
        formatted_time = time.ctime()

        img = Image(self.logo, 5*cm, 5*cm)
        self.elementos.append(img)

        tabla = self.tabla()
        tabla.wrapOn(c, 300, 400)
        tabla.drawOn(c, 50, 50)
        c.save()


        #self.elements.append(tabla)
        #doc.build(elements)

    def tabla(self):

        clientes = list(self.cursor.execute("select * from taller"))
        titulos = [["MATRICULA", "VEHICULO","KILOMETROS", "FECHA ENTRADA", "CLIENTE", "CIF/NIF", "DIRECCION"]]

        clientes = titulos + clientes
        tabla = Table(clientes)

        tabla.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 2, colors.white),
                                   ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                   ('LEFTPADDING', (0, 0), (-1, -1), 3),
                                   ('RIGHTPADDING', (0, 0), (-1, -1), 3),
                                   ('FONTSIZE', (0, 1), (-1, -1), 10),
                                   ('BACKGROUND', (0,1),(-1,-1), colors.lightblue),
                                   ('BACKGROUND', (0, 0), (-1, 0), colors.blue)]))

        return tabla
        #print(self.cursor.fetchall())



Historial().pdf()