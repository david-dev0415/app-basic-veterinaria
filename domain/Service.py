from dataclasses import dataclass
from datetime import date

@dataclass
class Service:
  id: str
  name: str
  cost: float
  date: date
  veterinarian_id: str

  def __post_init__(self):
    if not isinstance(self.name, str) or not self.name.strip():
      raise ValueError(f'Enter a valid name for the service.')
    if not isinstance(self.cost, float) or self.cost < 0:
      raise ValueError(f'Enter a valid cost for the service.')
    if not isinstance(self.date, date):
      raise ValueError(f'Enter a valid date for the service.')   
