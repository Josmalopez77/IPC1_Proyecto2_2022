from Album import Album
from Stamps_DAO import Stamps_DAO
from Stamps_DB import stamps_DB
import random

class Album_DAO:
    def __init__(self):
        self.albumes = []
        
    def Crear(self, id, name, created):
        for album in self.albumes:
            if album.id == id:
                print("id ya creado")
                return False
        ST = Stamps_DAO ()
        ST.Iniciar("", "", "", "")
        nuevo = Album(id, name, created,ST)
        self.albumes.append(nuevo)
        print("Albúm Creado Satisfactoriamente!!!")
        return True
        
    def Abrir_sobre(self, id):
        for album in self.albumes:
            if album.id == id:
                for _ in range(6):
                    random1 = random.randint(0, 31)
                    random2 = random.randint(0, 18)
                    Equipo = stamps_DB[random1]
                    Team = Equipo['id']
                    Player = Equipo['elements'][random2]
                    id_P = Player['id']
                    name_P = Player['name']
                    isPlayer = Player['isPlayer']
                    ST = Stamps_DAO()
                    ST = album.stamps
                    ST.Agregar_Estampa(Team, id_P, name_P, isPlayer)
                return True   
            print("Albúm no encontrado")
                
                
    @staticmethod
    def conv(album):
        return{
            "id":album.id,
            "name":album.name,
            "created_at":album.created
        }

    def Mostrar_Album(self):
        temporal = []
         
        for album in self.albumes:
            temporal.append(self.conv(album))
            print("ID: "+album.id+" Nombre: "+album.name+ " Fecha: "+album.created)
        return(temporal)
            
            
    def Mostrar_Estampas(self, id):
        for album in self.albumes:
            if album.id == id:
                ST = Stamps_DAO()
                ST = album.stamps
                ST.Mostrar()
                
    def Mostrar_Grupos(self, id, grupo):
        for album in self.albumes:
            if album.id == id:
                ST = Stamps_DAO()
                ST = album.stamps
                ST.Mostrar_grupos(grupo)
                
    def Mostrar_Pais(self, id, pais):
        for album in self.albumes:
            if album.id == id:
                ST = Stamps_DAO()
                ST = album.stamps
                ST.Mostrar_Pais(pais)
                
    