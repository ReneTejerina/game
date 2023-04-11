evaluar = """ título: Experiences in Developing a Distributed Agent-based 
Modeling Toolkit with Python
resumen: Distributed agent-based modeling (ABM) on high-performance 
computing resources provides the promise of capturing unprecedented details 
of large-scale complex systems. However, the specialized knowledge required 
for developing such ABMs creates barriers to wider adoption and utilization. 
Here we present our experiences in developing an initial implementation of 
Repast4Py, a Python-based distributed ABM toolkit. We build on our 
experiences in developing ABM toolkits, including Repast for High 
Performance Computing (Repast HPC), to identify the key elements of a useful 
distributed ABM toolkit. We leverage the Numba, NumPy, and PyTorch packages 
and the Python C-API to create a scalable modeling system that can exploit 
the largest HPC resources and emerging computing architectures.
"""
titulo = evaluar.split("resumen: ")[0].split("título: ")[1].split("\n")[0]
titulo = titulo.split(" ")
titulo_2= evaluar.split("resumen: ")[0].split("título: ")[1].split("\n")[1]
titulo_2=titulo_2.split(" ")
titulo.extend(titulo_2)
print(titulo)

facil=0
aceptable=0
dificil=0
muy_dificil=0
oracion_0 = evaluar.split("resumen: ")[1]
oracion_1=oracion_0.split(".")
oracion_1.remove("\n")
#print(oracion_1)

for tex in oracion_1:
    palabras= tex.split(" ")
    if " " in palabras :
        palabras.remove("")
    cant_palabras= len(palabras)
    match cant_palabras:
        case cant_palabras if cant_palabras < 12:
             facil+=1
        case cant_palabras if  13 <= cant_palabras <=17:
            aceptable+=1
        case cant_palabras if 18 <=cant_palabras <=25:
            dificil+=1
        case cant_palabras if cant_palabras > 25:
            muy_dificil+=1
if(len(titulo) == 11):
    print("Titulo: ok")
else:
    print("Titulo: not OK")
print(f" oraciones faciles de leer:{facil}")
print(f" oraciones aceptables de leer:{aceptable}")
print(f" oraciones dificiles de leer: { dificil} ")
print(f" oraciones muy dificiles de leer:{muy_dificil}")