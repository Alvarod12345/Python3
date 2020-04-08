#Hwk I/O
userLimit = 5
NotesData = []
registeredNotes = 0
tempNoteData = []
NameData = []
namedict = {}
outputFile = open("Notas.txt","w")
while(registeredNotes < userLimit):    
    nameNote = input("Ingrese nombre de su archivo: ")
    tempNoteData.append(nameNote)
    NameData.append(nameNote)
    print("Dato Temporal: ",tempNoteData)
    
    for name in NameData:
        if name in NameData: 
            print("A. Leer archivo ")
            print("B. Eliminar el archivo y comenzar de nuevo ")
            print("C. Agregar el archivo")
            input("Ingresar opcion: ")
    # if(nameNote != NotesData):
        else:  
            NotesData.append(tempNoteData)
            registeredNotes += 1
            #print("Nombre de Notas: ",NotesData)
            content = input("Ingrese el texto: ")
            tempNoteData.append(content)
            #NotesData.append(tempNoteData)
            print(nameNote,content)

        
outputFile.close()

# if(nameNote != NotesData):
#         NotesData.append(tempNoteData)
#         registeredNotes += 1
#         print("Nombre de Notas: ",NotesData)
#         content = input("Ingrese el texto: ")
#         tempNoteData.append(content)
#         NotesData.append(tempNoteData)
#         print(nameNote,content)
#     else:  
#         print("A. Leer archivo ")
#         print("B. Eliminar el archivo y comenzar de nuevo ")
#         print("C. Agregar el archivo")
#         input("Ingresar opcion: ")



# Note = {}
# for part in NotesData:
#     temPart = part[0]
#     if temPart in NotesData:
#         print("A. Leer archivo ")
#         print("B. Eliminar el archivo y comenzar de nuevo ")
#         print("C. Agregar el archivo")
#     else:
#         NotesData.append(temPart)



import os.path

fileName = str(input("Ingresar nombre de su archivo: ") + ".txt")


def options():
    print("A) Leer archivo.\n")
    print("B) Eliminar el archivo y comenzar de nuevo.\n")
    print("C) Agregar el archivo.\n")
    print("D) Reemplazar una sola linea.\n")
    choice = input("Elija una opcion: ")
    return choice


def change_line():
    fl = open(fileName, "r").readlines()
    line_num = int(input("Que linea editar? "))-1
    fl[line_num] = str(input("Escribe tu nuevo texto de linea: ") + "\n")
    out_f = open(fileName, "w")
    out_f.writelines(fl)
    print("Linea", line_num+1, "cambio exitoso.")
    out_f.close()


if os.path.isfile(fileName):
    print("Archivo Existente\n")
    get_choice = options()
    if get_choice == "A":
        file = open(fileName, "r")
        for line in file:
            print(line, end="")
        file.close()
    elif get_choice == "B":
        file = open(fileName, "w")
        while True:
            temp_inp = (input("Escribe el nombre de su archivo:\n"))
            file.write(str(temp_inp) + "\n")
            keep_on = str(input("Desea continuar escribiendo en su archivo? Yes/No\n"))
            if keep_on == "Yes":
                continue
            elif keep_on == "No":
                break
            else:
                keep_on = str(input("Desea continuar escribiendo en su archivo? Yes/No\n"))
        file.close()
    elif get_choice == "C":
        file = open(fileName, "a")
        while True:
            temp_inp = (input("Write for your file:\n"))
            file.write(str(temp_inp) + "\n")
            keep_on = str(input("Desea continuar escribiendo en su archivo? Yes/No\n"))
            if keep_on == "Yes":
                continue
            elif keep_on == "No":
                break
            else:
                keep_on = str(input("Desea continuar escribiendo en su archivo? Yes/No\n"))
        file.close()
    elif get_choice == "D":
        lines = len(open(fileName).readlines())
        print("This file has", lines, "lines.\n")
        change_line()
    else:
        print("No existe esa opcion.")
else:
    print("El archivo acaba de ser creado\n")
    file = open(fileName, "w")
    while True:
        temp_inp = (input("Escribe contenido en su nuevo archivo:\n"))
        file.write(str(temp_inp) + "\n")
        keep_on = str(input("Desea continuar escribiendo en su archivo? Yes/No\n"))
        if keep_on == "Yes":
            continue
        elif keep_on == "No":
            break
        else:
            keep_on = str(input("Desea continuar escribiendo en su archivo? Yes/No\n"))
    file.close()