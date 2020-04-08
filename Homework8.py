import os.path

fileName = str(input("Ingresar nombre de su archivo: ") + ".txt")

def options(): #metodo opciones imprime y ingreso
    print("A. Leer archivo.\n")
    print("B. Eliminar el archivo y comenzar de nuevo.\n")
    print("C. Agregar el archivo.\n")
    print("D. Reemplazar una sola linea.")
    choice = input("Elija una opcion: ") #elegir opcion
    return choice

def change_line():
    fl = open(fileName, "r").readlines() #abre filename y lo lee
    line_num = int(input("Que linea editar? "))-1 #convierte parametros a enteros 
    fl[line_num] = str(input("Escribe tu nuevo texto de linea: ") + "\n") #de fl el line_num ingresado es a editar
    out_f = open(fileName, "w") #abre el archivo y lo reescribe o cambia de nombre
    out_f.writelines(fl) #reescribe el archivo
    print("Linea", line_num+1, "cambio exitoso .") #imprime que linea a sido modificada
    out_f.close() #cierra archivo

if os.path.isfile(fileName): #es true si el archivo es existente
    print("Archivo Existente\n") #imprime
    get_choice = options() #va al metodo opciones 
    if get_choice == "A": #opcion "A"
        file = open(fileName, "r") #abre el archivo para leer "r"
        for line in file: #para line in en el archivo (recorre todo el archivo line por linea)
            print(line, end="") #imprime linea , final
        file.close() #cierra archivo
    elif get_choice == "B": #opcion "B"
        file = open(fileName, "w") #abre el archivo para escribir "w"
        while True: #mientras sea True
            temp_inp = (input("Escribe el nuevo nombre de su archivo:\n")) #ingresar el nombre del archivo
            file.write(str(temp_inp) + "\n") #agregar al archivo el temporaly input
            keep_on = str(input("Desea continuar escribiendo en su archivo? si/no\n")) #seguir si/no
            if keep_on == "si": #caso si retorna al metodo
                continue
            elif keep_on == "no": #caso no rompe 
                break
            else: #caso de no cumplir lo anterior
                keep_on = str(input("Desea continuar escribiendo en su archivo? si/no\n")) # si / no
        file.close() #cierra archivo
    elif get_choice == "C": #opcion c
        file = open(fileName, "a") #abre archivo y agrega
        while True: #mientras true
            temp_inp = (input("Escribir en tu nota archivo:\n")) # escribir en el archivo
            file.write(str(temp_inp) + "\n") #agrega temporaly input al archivo
            keep_on = str(input("Desea continuar escribiendo en su archivo? si/no\n")) #si / no
            if keep_on == "si": #caso si retorna al metodo
                continue
            elif keep_on == "no": #caso no rompe 
                break
            else:
                keep_on = str(input("Desea continuar escribiendo en su archivo? si/no\n")) #si / no
        file.close() #cierra el archivo
    elif get_choice == "D":
        lines = len(open(fileName).readlines())
        print("This file has", lines, "lines.\n")
        change_line()
    else:
        print("No existe esa opcion.") #imprime
else:
    print("El archivo acaba de ser creado\n") #imprime
    file = open(fileName, "w") #abre el archuvo para escribir
    while True: #mientras true
        temp_inp = (input("Escribe contenido en su nuevo archivo:\n")) #escribir nombre en el archivo
        file.write(str(temp_inp) + "\n") #agrega o escribe el temporaly input
        keep_on = str(input("Desea continuar escribiendo en su archivo? si/no\n")) #si / no
        if keep_on == "si": #caso si retorna al metodo
            continue
        elif keep_on == "no": #caso no rompe 
            break
        else:
            keep_on = str(input("Desea continuar escribiendo en su archivo? si/no\n")) #si / no retorna
    file.close() #cierra archivo