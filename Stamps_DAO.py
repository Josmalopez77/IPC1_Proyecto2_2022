from Stamps import Stamps
from Stamps_DB import grupos_DB
class Stamps_DAO():
    def __init__(self):
        self.stamps = []
        
    def Iniciar(self, id_Team, id, name, isPlayer):
        nuevo = Stamps(id_Team, id, name, isPlayer)
        self.stamps.append(nuevo)
    
    def Agregar_Estampa(self, id_Team, id, name, isPlayer):
        nuevo = Stamps(id_Team, id, name, isPlayer)
        self.stamps.append(nuevo)
        print("Estampa Agregada")
        
    def Mostrar(self):
        for stamp in self.stamps:
            print(stamp.id_Team, stamp.id, stamp.name, stamp.isPlayer)
            
    def Mostrar_grupos(self, grupo):
        for group in grupos_DB:
            if group['group'] == grupo:
                a = group['teams']
                
        for stamp in self.stamps:
            if stamp.id_Team == a[0]:
                print(stamp.id_Team, stamp.id, stamp.name, stamp.isPlayer)
            elif stamp.id_Team == a[1]:
                print(stamp.id_Team, stamp.id, stamp.name, stamp.isPlayer)
            elif stamp.id_Team == a[2]:
                print(stamp.id_Team, stamp.id, stamp.name, stamp.isPlayer)
            elif stamp.id_Team == a[3]:
                print(stamp.id_Team, stamp.id, stamp.name, stamp.isPlayer)
                
    def Mostrar_Pais(self, pais):
        for stamp in self.stamps:
            if stamp.id_Team == pais:
                print(stamp.id_Team, stamp.id, stamp.name, stamp.isPlayer)
                    
                
            
        
        
        