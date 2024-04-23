def recomendar_plano(consumo):
   
if consumo <= 10 :
    
    return "plano essencial fibra - 50mbps"
    
elif consumo <= 20 :
return "plano prata fibra - 100mbps"
      
else
        
return "plano de premium fibra - 300mbps"
consumo = float (input())
        
print(recomendar_plano (consumo))
      