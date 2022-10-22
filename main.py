from Album_DAO import Album_DAO
from Stamps_DB import stamps_DB
from Stamps_DB import grupos_DB
cl = Album_DAO()

cl.Crear("1a2b3c","Jose","21/10/2022")
cl.Crear("1a2b3c","Jose","21/10/2022")
cl.Crear("3c2b1a","Paola","20/90/2022")
cl.Mostrar_Album()
cl.Abrir_sobre("1a2b3c")
cl.Abrir_sobre("1a2b3c")
cl.Abrir_sobre("1a2b3c")
cl.Abrir_sobre("1a2b3c")
cl.Mostrar_Estampas("1a2b3c")
print("--------------------------------------")
cl.Mostrar_Pais("1a2b3c","arg")





