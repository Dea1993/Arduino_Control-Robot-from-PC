#!/usr/bin/env python

import pygtk
import gtk
import serial
import gtk.glade

USB = '/dev/ttyUSB0'
arduino = 0

#provo a connettermi con arduino tramite la porta seriale
try:
	print 'Connessione in corso...'
	#instauro la comunicazione con la porta seriale
	seriale = serial.Serial(USB, 9600)
	arduino = 1
	print 'Connessione stabilita con successo'

except:
	print 'ERRORE: Collega arduino alla presa USB'
	arduino = 1


if arduino == 1:
	def on_control(cmd):
		print(cmd)
		#invio il comando ad arduino tramite la porta seriale
		seriale.write(cmd)
	
	#chiude il programma e spegne il robot
	def on_quit(cmd):
		print "Chiusura in Corso..."
		cmd = '0'
		seriale.write(cmd)
		gtk.main_quit()

	dizionario = {
		'on_cmdAvanti_clicked': (lambda cmd: on_control("w")),
		'on_cmdIndietro_clicked': (lambda cmd: on_control("s")),
		'on_cmdDestra_clicked': (lambda cmd: on_control("d")),
		'on_cmdSinistra_clicked': (lambda cmd: on_control("a")),
		'on_cmdVel1_clicked': (lambda cmd: on_control("1")),
		'on_cmdVel2_clicked': (lambda cmd: on_control("2")),
		'on_cmdVel3_clicked': (lambda cmd: on_control("3")),
		'on_cmdVel4_clicked': (lambda cmd: on_control("4")),
		'on_cmdStop_clicked': (lambda cmd: on_control("0")),
		'on_cmdRsx_clicked': (lambda cmd: on_control("q")),
		'on_cmdRdx_clicked': (lambda cmd: on_control("e")),
		'on_winMain_destroy': on_quit,
		'on_cmdCancel_clicked': on_quit,
	}

	gladeFile = gtk.glade.XML(fname='GTK.glade')
	gladeFile.signal_autoconnect(dizionario)
	
	gw = gladeFile.get_widget
	winMain = gw('winMain')
	winMain.show()
	gtk.main()
	
if arduino == 0:
	def on_quit(cmd):
		print "Chiusura in Corso..."
		gtk.main_quit()
		
	dizionario = {
			'on_winMain_destroy': on_quit,
			'on_cmdCancel_clicked': on_quit
	}
		
	gladeFile = gtk.glade.XML(fname='GTK_err.glade')
	gladeFile.signal_autoconnect(dizionario)
	
	gw = gladeFile.get_widget
	winMain = gw('winMain')
	winMain.show()
	gtk.main()
