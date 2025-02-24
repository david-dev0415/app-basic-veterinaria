from abc import ABC, abstractmethod
from dataclasses import dataclass

class IPerson(ABC):

  @abstractmethod
  def get_id(self) -> int:
    return self.id

  @abstractmethod
  def get_name(self) -> str:
    pass

  @abstractmethod
  def get_phone(self) -> str:
    pass

  @abstractmethod
  def get_address(self) -> str:
    pass

  @abstractmethod
  def __repr__(self) -> str:
    pass

@dataclass
class Person(IPerson):
  id: str
  name: str
  phone: str
  address: str
  specialization: str

  def __post_init__(self):
    if not isinstance(self.name, str) or not self.name.strip():
      raise ValueError(f'Enter a valid name for the person.')
    if not isinstance(self.phone, str) or not self.phone.strip():
      raise ValueError(f'Enter a valid phone for the person.')
    if not isinstance(self.address, str) or not self.address.strip():
      raise ValueError(f'Enter a valid address for the person.')
    if not isinstance(self.specialization, str) or not self.specialization.strip():
      raise ValueError(f'Enter a valid specialization for the person.')

  def get_id(self) -> int:
    return self.id
  
  def get_name(self) -> str:
    return self.name
  
  def get_phone(self) -> str:
    return self.phone
  
  def get_address(self) -> str:
    return self.address

  def __repr__(self):
    return f'\nPersona(id={self.id}, name={self.name}, phone={self.phone}, address={self.address})'