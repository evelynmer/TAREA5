def get_user_review():

    while True:
        point = input("Por favor, introduzca una puntuación del 1 al 5: ")
    
        if point.isdigit():
            point = int(point)

            if 1 <= point <= 5:
                comment = input("Ingrese su Comentario: ")
                print("\n")

                post = f'point:{point}, comment: {comment}'

                with open("data.txt", "a") as file:
                    file.write(f'{ post }\n')

                return
            else:
                print("Error:")
        else:
            print("Error:")
        
def show_results_to_date():
    print("Resultados :")

    with open("data.txt", "r") as file:
        print(file.read())

def  option_menu():

    while True:
            print("Seleccione el proceso que desea llevar a cabo\n1: Introduzca sus puntos de evaluación y comentarios\n2: Compruebe los resultados hasta el momento\n3: Finalizar.\n")
            opction = input("Option: ")

            if opction.isdigit():
                opction = int(opction)
            else: 
                print("Error: No Numerico")
                continue

            if opction == 1:
                get_user_review()
            elif opction == 2:
                show_results_to_date()
            elif opction == 3:
                print("Fin")
                break
            else:
                print("Por favor, introduzca un valor del 1 al 3\n")

option_menu()