from datetime import datetime

agora = datetime.now()

# Diferentes formatos:
print(agora.strftime("%d/%m/%Y"))         
print(agora.strftime("%d/%m/%Y %H:%M"))     
print(agora.strftime("%d/%m/%Y %H:%M:%S"))  
print(agora.strftime("%d de %B de %Y"))   
print(agora.strftime("%A, %d/%m/%Y"))       