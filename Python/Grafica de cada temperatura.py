import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy import signal
import matplotlib.dates as mdates
from datetime import datetime
formato_tiempo=mdates.DateFormatter("%H:%M")
plt.figure("Análisis de temperaturas en latas de diversos colores")
plt.gca().xaxis.set_major_formatter(formato_tiempo)
#Lata Blanca 2
dataBlanca2=np.genfromtxt("lata_blanca_2.txt",names=True,delimiter=",",dtype=None,encoding=None)
date_listBlanca2=list()
for i in range(0,len(dataBlanca2)):
    fecha_horaBlanca2=dataBlanca2["fecha"][i]+" "+dataBlanca2["hora"][i]
    date_listBlanca2.append(datetime.strptime(fecha_horaBlanca2, "%d/%m/%Y %H:%M:%S"))
plt.plot(date_listBlanca2,dataBlanca2["temperatura_lata"],"b:", label="Lata blanca 2", linewidth=1)
plt.plot(date_listBlanca2,signal.medfilt(dataBlanca2["temperatura_ambiente"],31), "g-.", label="Ambiente 2", linewidth=1)
#Lata Aluminio 3
data=np.genfromtxt("nuevo_lata_aluminio_3.csv",names=True,delimiter=",",dtype=None,encoding=None)
date_list=list()
for i in range(0,len(data)):
    fecha_hora=data["fecha"][i]+" "+data["hora"][i]
    date_list.append(datetime.strptime(fecha_hora, "%d/%m/%Y %H:%M:%S"))
plt.plot(date_list,data["temperatura"], "r--", label="Lata aluminio 3", linewidth=1)
#Lata Negra 4
data=np.genfromtxt("lata_negra_4.txt",names=True,delimiter=",",dtype=None,encoding=None)
date_list=list()
for i in range(0,len(data)):
    fecha_hora=data["fecha"][i]+" "+data["hora"][i]
    date_list.append(datetime.strptime(fecha_hora, "%d.%m.%Y %H:%M:%S"))
plt.plot(date_list,data["temperatura_lata"], "c-", label="Lata negra 4", linewidth=1)
# Lata Blanca 5
data=np.genfromtxt("lata_blanca_5.txt",names=True,delimiter=",",dtype=None,encoding=None)
date_list=list()
for i in range(0,len(data)):
    fecha_hora=data["fecha"][i]+" "+data["hora"][i]
    date_list.append(datetime.strptime(fecha_hora, "%d-%m-%Y %H:%M:%S"))
plt.plot(date_list,data["temperatura_lata"], "m:", label="Lata blanca 5", linewidth=2)
plt.plot(date_list,signal.medfilt(data["temperatura_ambiente"],595), "y-.", label="Ambiente 5", linewidth=2)
#Lata Azul 7
data=np.genfromtxt("lata_azul_7.txt",names=True,delimiter=",",dtype=None,encoding=None)
date_list=list()
for i in range(0,len(data)):
    fecha_hora=data["fecha"][i]+" "+data["hora"][i]
    date_list.append(datetime.strptime(fecha_hora, "%d-%m-%Y %H:%M:%S"))
plt.plot(date_list,data["temperatura"], "k--", label="Lata azul 7", linewidth=2)
#Lata Blanca 8
data=np.genfromtxt("lata_blanca_8.txt",names=True,delimiter=",",dtype=None,encoding=None)
date_list=list()
for i in range(0,len(data)):
    fecha_hora=data["fecha"][i]+" "+data["hora"][i]
    date_list.append(datetime.strptime(fecha_hora, "%d.%m.%Y %H:%M:%S"))
plt.plot(date_list,signal.medfilt(data["temperatura_lata"],295), "b-", label="Lata blanca 8", linewidth=2)
plt.plot(date_list,signal.medfilt(data["temperatura_ambiente"],9), "g:", label="Ambiente 8", linewidth=3)
#Lata Aluminio 9
data=np.genfromtxt("lata_aluminio_9.txt",names=True,delimiter=",",dtype=None,encoding=None)
date_list=list()
for i in range(0,len(data)):
    fecha_hora=data["fecha"][i]+" "+data["hora"][i]
    date_list.append(datetime.strptime(fecha_hora, "%d.%m.%Y %H:%M:%S"))
plt.plot(date_list,signal.medfilt(data["temperatura_lata"],389), "r-.", label="Lata aluminio 9", linewidth=3)

plt.xlabel("Hora [HH:MM]")
plt.ylabel("Temperatura [°C]")
plt.title("Análisis de temperaturas en latas de diversos colores")
plt.grid(color="gray", linestyle="--", linewidth=0.5)
plt.legend(loc="best")
mng=plt.get_current_fig_manager()
mng.window.state("zoomed")
plt.show()

