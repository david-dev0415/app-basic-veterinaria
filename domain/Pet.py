from typing import List, Optional
from dataclasses import dataclass
from domain.Service import Service
from domain.Person import Person

@dataclass
class Pet:
  name: str
  age: int
  race: str
  species: str
  owner_id: Optional['Person'] = None # Can be various owners
  services_history: List[Service] = None

  def __post_init__(self):
    if self.servvices_history in None:
      self.services_history = []
    if not isinstance(self.name, str) or not self.name.strip():
      raise ValueError(f'Enter a valid name for the pet.')
    if not isinstance(self.age, int) or self.age < 0:
      raise ValueError(f'Enter a valid age for the pet.')
    if not isinstance(self.race, str) or not self.race.strip():
      raise ValueError(f'Enter a race for the pet (e.g. Golden Retriever).')
    if not isinstance(self.species, str) or not self.species.strip():
      raise ValueError(f'Enter a species for the pet (e.g. Dog).')
    
  def add_service(self, service: Service):
    self.services_history.append(service)
    if not isinstance(service, Service):
      raise ValueError(f'Enter a valir service for the pet.')

  def get_services_history(self) -> List[Service]:
    return self.services_history

  def set_owner(self, owner: Person) -> None:
    if not isinstance(owner, Person):
      raise ValueError(f'Enter a valid owner for the pet.')
    self.owner_id = owner

  def __repr__(self):
    return f'Pet(name={self.name}, age={self.age}, species={self.species})'