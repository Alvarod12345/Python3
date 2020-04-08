#homework dictionaries and sets

#diccionario favsong
favsongDictionarie = {
"Name":"Gravity",
"Artist":"John Mayer",
"Duration in minutes":"4.05",
"Age artist":"42",
"Album":"2006",
"Launch month":"September",
"Genre":"Blues,Rock and Pop"
}

for values in favsongDictionarie:   #para los valores en el diccionario
    values = favsongDictionarie.values()    #trae solo los valores(values)
valuesSet = set(values)     #setea solo los valores y lo pone en una lista de diccionario
print("Favorite Song:",favsongDictionarie)  #imprime diccionnario favsongDictionarie
print("Values:",valuesSet)  #imprime valores seteado en diccionario

def search():   #funcion buscar
    searching = input("Search:")    #entrada de texto
    if searching in valuesSet:#     #si la entrada de texto esta en valores seteados en diccionario
        print(True)     #imprime TRUE
    else:   #sino
        print(False)    #imprime FAlSE

search() #run xd
