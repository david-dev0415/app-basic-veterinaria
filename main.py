from colorama import Fore, Style, init
from infrastructure.repositories.in_memory_repository import InMemoryRepository
from application.use_cases.manage_client import ManageClient

# Init colorama
init(autoreset=True)

def display_menu():
  print(Fore.CYAN + 'Gestión de Veterinaria')
  print('1. Gestionar clientes')
  print('2. Gestionar mascotas')
  print('3. Gestionar citas')
  print('4. Gestionar Ver historial de servicios')
  print('5. Salir')

def main():

  client_repo = InMemoryRepository()

  manage_client = ManageClient(client_repo)

  while True:
    display_menu()
    choice = input(Fore.YELLOW + 'Seleccione una opción: ')

    if choice == "1":
      print(Fore.GREEN + "=== GESTIÓN DE CLIENTES ===")
      print("1. Agregar cliente")
      print("2. Listar clientes")
      sub_choice = input("Seleccione una opción: ")
      if sub_choice == "1":
        name = input("Nombre del cliente: ")
        phone = input("Teléfono del cliente: ")
        address = input("Dirección del cliente: ")
        specialization = input("Especialización del cliente: ")
        print(manage_client.add_client(name, phone, address, specialization))  
      elif sub_choice == "2":
        print(manage_client.list_clients())
      else:
        print("Opción no válida")
    
    elif choice == "5":
      print(Fore.RED + "Saliendo del sistema...")
      break
    else:
      print(Fore.RED + "Opción inválida. Intente de nuevo.")
    

if __name__ == '__main__':
  main()

