from pacientes import *
from Organizar import *

Servicios = []
class pacientes:
    def __init__(self):
        self.nombre = nombre()
        self.cedula = random.randrange(10**9, 10**10)
        self.etapa = random.choice(DatosPaciente.estados)
        self.t1 = 0
        self.t2 = 0
        self.t3 = 0
        self.t4 = 0
        self.clasTriaje = random.randrange(1,6)
    
        if self.etapa == "Triaje":
            self.t1 = random.randrange(0,240)
            self.clasTriaje = 0
            
        elif self.etapa == "Prediagnostico":
            self.t1 = random.randrange(0,240)
            self.t2 = random.randrange(self.t1,self.t1+30)
            
        elif self.etapa == "Examenes":
            self.t1 = random.randrange(0,240)
            self.t2 = random.randrange(self.t1,self.t1+30)
            self.t3 = random.randrange(self.t2,self.t2+300) 
            
        elif self.etapa == "Tratamiento":
            self.t1 = random.randrange(0,240)
            self.t2 = random.randrange(self.t1,self.t1+30)
            self.t3 = random.randrange(self.t2,self.t2+300) 
            self.t4 = random.randrange(self.t3,self.t3+200)
    
        self.ttotal = self.t1 + self.t2 + self.t3 + self.t4
        Servicios.append([self.clasTriaje, self.t1, self.t2, self.t3, self.t4])

    def __str__(self):
        return f'Paciente: {self.nombre} | {self.cedula} | Triaje: {self.t1} min --> Nivel Urgencia({self.clasTriaje})| PreDiagnostico: {self.t2} min | Examenes: {self.t3} min | Tratamiento: {self.t4} min || Tiempo Total: {self.ttotal} min'

    def __gt__(self, OtroPaciente):
        if self.etapa == "Triaje":
            return self.t1 > OtroPaciente.t1  
        elif self.etapa == "Prediagnostico":
            return self.t2 > OtroPaciente.t2
        elif self.etapa == "Examenes":
            return self.t3 > OtroPaciente.t3
        elif self.etapa == "Tratamiento":
            return self.t4 > OtroPaciente.t4
    
    def __lt__(self, OtroPaciente):
        if self.etapa == "Triaje":
            return self.t1 < OtroPaciente.t1  
        elif self.etapa == "Prediagnostico":
            return self.t2 < OtroPaciente.t2
        elif self.etapa == "Examenes":
            return self.t3 < OtroPaciente.t3
        elif self.etapa == "Tratamiento":
            return self.t4 < OtroPaciente.t4
    
    def __eq__(self, OtroPaciente):
        if self.etapa == "Triaje":
            return self.t1 == OtroPaciente.t1  
        elif self.etapa == "Prediagnostico":
            return self.t2 == OtroPaciente.t2
        elif self.etapa == "Examenes":
            return self.t3 == OtroPaciente.t3
        elif self.etapa == "Tratamiento":
            return self.t4 == OtroPaciente.t4
        
  
triaje = []
Prediagnostico = []
Examenes = []
Tratamiento = []

def categorizar(lista):
    for paciente in lista:    
        if paciente.etapa == "Triaje":
            triaje.append(paciente)
        elif paciente.etapa == "Prediagnostico":
            Prediagnostico.append(paciente)
        elif paciente.etapa == "Examenes":
            Examenes.append(paciente)
        elif paciente.etapa == "Tratamiento":
            Tratamiento.append(paciente)
        
def nombre():
    nombre = random.choice(DatosPaciente.Nombres)
    return f'{nombre}'

def creacionPacientes(cant):
    listaPacientes = []
    for i in range(cant):
        paciente = pacientes()
        listaPacientes.append(paciente)
    
    return listaPacientes

def verLista(list):
    for i in list:
        print (f'{i}')
    print("\n")
