from modules import derivees, integrales, matrices, primitives, tools

modules: dict[str, str] = {"1": "Derivées", "2": "Primitives", "3": "Intégrales", "4": "Matrices"}


def menu() -> None:
    choice: int = 0
    while choice < 1 or choice > 4:
        print("Quel module voulez-vous utiliser ?")
        for key, element in modules.items():
            print(key + ". " + element)
        try:
            choice = int(input("Entrez le chiffre correspondant au module désiré : "))
        except ValueError:
            choice = 0
        tools.carriage_return()
    func_router(choice)


def func_router(choice: int) -> None:
    if choice == 1:
        derivees.main()
    elif choice == 2:
        integrales.main()
    elif choice == 3:
        matrices.main()
    elif choice == 4:
        primitives.main()


menu()
