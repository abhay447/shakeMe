#sudo apt-get install xautomation
from subprocess import Popen, PIPE

def keypress(sequence):
	#sequence = 'keydown '+key+' keyup '+key
	p = Popen(['xte',sequence])
	p.communicate()

