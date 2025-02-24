from domain.Person import Person
from utils.generate_id import generate_id

class ManageClient:

  def __init__(self, client_repository):
    self.client_repository = client_repository

  def add_client(self, name: str, phone: str, address: str, specialization: str) -> str:
    id = generate_id()
    client = Person(id, name, phone, address, specialization)

    try:
      self.client_repository.add(client)
      return f'Client {client.name} registrado exitosamente.'
    except Exception as e:
      return f"Error al registrar el cliente: {str(e)}"    
  
  def list_clients(self) -> str:
    clients = self.client_repository.get_all()
    if not clients:
      return 'No clients found.'
    
    return "\n".join([repr(client) for client in clients])

