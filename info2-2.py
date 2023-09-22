vlan_id = int(input("Ingresa el ID de la VLAN: "))
if 1 <= vlan_id <= 1005:
    print("La VLAN", vlan_id, "es de rango básico.")
elif 1006 <= vlan_id <= 4095:
    print("La VLAN", vlan_id, "es de rango superior.")
else:
    print("El número de VLAN ingresado es desconocido.")
    
    
        
        
