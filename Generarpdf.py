from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate,Table,TableStyle,Paragraph,Spacer,Image
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm

import time
import datetime
import sqlite3 as dbapi
from gi.repository import Gtk
class PDF():
    def __init__(self):
        #Conexion con la base de datos
        self.bd = dbapi.connect("basedatos.dat")
        self.cursor = self.bd.cursor()
        self.foto = Image("./talleres-rodal.jpg")
        self.elementos = []

    def pdf(self):
        historialpdf ="Clientes"+ str(datetime.date.today()) +"_.pdf"
        c = canvas.Canvas(historialpdf, pagesize=A4)
        c.drawString(20,800,"Impresion lista clientes")


        #c.drawImage(foto,200,800)
        #c.drawImage(self.foto, 1*cm, 26*cm, 19*cm, 3*cm)

        tabla = self.tabla()
        tabla.wrapOn(c, 20, 30)
        tabla.drawOn(c, 20, 600)
        c.save()

        self.popup("PDF Generado")
        #self.elements.append(tabla)
        #doc.build(elements)

    def tabla(self):

        clientes = list(self.cursor.execute("select * from taller"))
        titulos = [["MATRICULA", "VEHICULO","KILOMETROS", "FECHA ENTRADA", "CLIENTE", "CIF/NIF","TELEFONO", "DIRECCION"]]

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
    def cerrar(self, widget):
        widget.destroy()
    #Metodo para que salga una ventana emergente segun el metodo en el que lo llame
    def popup(self, texto):
        window = Gtk.Window(title="Warning")
        label = Gtk.Label(texto)
        label.set_padding(15,15)
        window.add(label)
        window.connect("delete-event", self.cerrar)
        window.set_position(Gtk.PositionType.RIGHT)
        window.show_all()
#PDF().pdf()