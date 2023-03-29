import random
class DatosPaciente:

    # Estos datos seran aleatorios "Simulando" la toma de datos en un hospital
    """
    Datos que tomare: 
        - Nombre 
        - Cedula
        - Tiempo en triaje t1
        - Tiempo en Prediagnostico t2
        - Tiempo en Examenes t3
        - Tiempo en Tratamiento t4

    """

    Nombres = ["Emma", "Noah", "Olivia", "Liam", "Sophia", "Mason", "Ava", "Jacob", "Isabella", "William", 
         "Mia", "Ethan", "Charlotte", "Michael", "Amelia", "Alexander", "Emily", "James", "Abigail", 
         "Daniel", "Madison", "Elijah", "Elizabeth", "Matthew", "Evelyn", "Aiden", "Avery", "Jackson", 
         "Ella", "Logan", "Scarlett", "David", "Feid", "Anthony", "Chloe", "Isaac", "Victoria", 
         "Andrew", "Aubrey", "Luke", "Zoe", "Joshua", "Addison", "Wyatt", "Natalie", "Sebastian", 
         "Lily", "Owen", "Aaliyah", "Nathan", "Hannah", "Ryan", "Aubree", "Caleb", "Kaylee", 
         "Brayden", "Annabelle", "Gavin", "Makayla", "Isaiah", "Gianna", "Jacob", "Alexis", "Cameron", 
         "Brooklyn", "Eli", "Lillian", "Aaron", "Adalynn", "Kyle", "Maya", "Nicholas", "Leah", 
         "Evan", "Allison", "Adrian", "Savannah", "Jonathan", "Nevaeh", "Colton", "Peyton", "Adam", 
         "Mackenzie", "Jace", "Molly", "Ian", "Bailey", "Cooper", "Maria", "Tyler", "Jordan", 
         "Bentley", "Taylor", "Damien", "Hadley", "Hayden", "Kaitlyn", "Eduardo", "Naomi", "Carson", 
         "Aurora", "Erick", "Melanie", "Devin", "Lydia", "Gage", "Alyssa", "Nathaniel", "Bella"]
    
    estados = ["Triaje", "Prediagnostico", "Examenes", "Tratamiento"]
    

    