from Entidades.SubOpcionLlamada import SubOpcionLlamada         #Importamos la relacion de agregacion con la clase SubOpcionLlamada
from Entidades.Validacion import Validacion         #Importamos la relacion de asociacion con la clase Validacion

class OpcionLlamada:
    def init(self, audioMensajeSubOpcion, mensajeSubOpciones, nombre, nroOrden):
        #Inicializamos los valores de los atributos
        self.audioMensajeSubOpcion = audioMensajeSubOpcion
        self.mensajeSubOpciones = mensajeSubOpciones
        self.nombre = nombre
        self.nroOrden = nroOrden

        self.subOpcionLlamada: SubOpcionLlamada = []
        self.validacionesRequeridas: Validacion = []

    def getAudioMensajeSubOpcion(self):
        #Devuelve el valor del atributo "audioMensajeSubOpcion"
        return self.audioMensajeSubOpcion

    def getDescripcionConSubOpcion(self):
        #Devuelve el valor de una descripcion a partir de los valores de "nombre" y "nroOrden"
        descripcion = self.subOpcionLlamada.getNombre()
        return descripcion
    
    def getNombre(self):
        # Devuelve el valor del atributo 'nombre'
        return self.nombre
    
    def getNroOrden(self):
        # Devuelve el valor del atributo 'nroOrden'
        return self.nroOrden
    
    

