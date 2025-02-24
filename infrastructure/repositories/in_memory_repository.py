class InMemoryRepository:
  def __init__(self):
    self._data = {}
  
  def add(self, entity):
    if entity.id in self._data:
      raise ValueError(f'Entity with id {entity.id} already exists.')
    self._data[entity.id] = entity

  def get(self, entity_id):
    if entity_id not in self._data:
      raise ValueError(f'Entity with id {entity_id} not found.')
    return self._data[entity_id]
  
  def get_all(self):
    return list(self._data.values())