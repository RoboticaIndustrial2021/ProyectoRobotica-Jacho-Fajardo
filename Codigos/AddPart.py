# Type help("robolink") or help("robodk") for more information
# Press F5 to run the script
# Note: you do not need to keep a copy of this file, your python script is saved with the station
from robolink import *    # API to communicate with RoboDK
from robodk import *      # basic matrix operations
import random
RDK = Robolink()

#Variables con nombre de objeto y referencia a usar
PART_NAME       = 'box100mm'
CONVEYOR_REF    = 'MovingRef'

#Valores de las dimensiones de la caja
SIZE_BOX = RDK.getParam('SizeBox')
SIZE_BOX_XYZ = [float(x.replace(' ','')) for x in SIZE_BOX.split(',')]
[SIZE_BOX_X, SIZE_BOX_Y, SIZE_BOX_Z] = SIZE_BOX_XYZ

# Creacion de nueva caja en la banda
part = RDK.Item(PART_NAME, ITEM_TYPE_OBJECT)
conveyor_ref = RDK.Item(CONVEYOR_REF, ITEM_TYPE_FRAME) #Referencia movil de la banda transportadora
part_pos = part.PoseAbs() # Posicion absoluta de la caja de referencia
part.Copy() 
newpart = conveyor_ref.Paste() 
newpart.setPoseAbs(part_pos*transl(0,0,SIZE_BOX_Z/2)) #Posicionando la nueva caja teniendo en cuenta su referencia central.
newpart.setName('Part') # Se crea una caja para el palleteA
newpart.Scale([SIZE_BOX_X/100, SIZE_BOX_Y/100, SIZE_BOX_Z/100]) #Escala con respecto al objeto de referencia (100mm cube)
newpart.Recolor([0.678, 0.529, 0.2, 1]) #set RGBA color
newpart.setVisible(True, False) #make item visible but hide the reference frame



