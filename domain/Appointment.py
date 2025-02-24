from dataclasses import dataclass
from datetime import date
from utils.generate_id import generate_id

from domain import Service
from domain import Pet
from domain import Person

  
@dataclass
class Appointment():
  pet: Pet
  veterinarian: Person
  service_name: str
  scheduled_date: date 
  completed: bool

  def complete_appointment(self, cost: float) -> None:
    if not self.completed:
      service = Service(
          id = generate_id(),
          name = self.service_name,
          cost = cost,
          date = self.scheduled_date,
          veterinarian_id = self.veterinarian.get_id()
        )
      self.pet.add_service(service)
      self.completed = True
      print(f"Service '{self.service_name}' completed for pet '{self.pet.name}'")
    else:
      print(f"Service '{self.service_name}' already completed for pet '{self.pet.name}'")

  def __repr__(self):
    return f'Appointment(date={self.date}, time={self.time}, service={self.type_of_service}, venerinarian={self.veterinarian}, pet={self.pet})'
  