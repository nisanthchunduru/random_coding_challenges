# number_of_items = 5
# carton_max_weight = 5
# item_weights = [5, 2, 3, 1, 4]

# number_of_items = 7
# carton_max_weight = 12
# item_weights = [12, 2, 3, 11, 6, 8 ,1]

number_of_items = int(input())
carton_max_weight = int(input())
item_weights = []

for x in range(0, number_of_items):
  item_weight = int(input())
  item_weights.append(item_weight)

class Items:
  def __init__(self, item_weights):
    self.items = item_weights
  
  def none_remaining(self):
    return (len(self.items) == 0)

  # @todo Optimize
  def pop_heaviest_item(self):
    heaviest_item = self.heaviest_item()
    self.items.remove(heaviest_item)
    return heaviest_item
  
  def heaviest_item(self):
    return max(self.items)
  
  # @todo Optimize
  def pop_heaviest_item_whose_weight_is_less_than_or_equal_to(self, max_weight):
    heaviest_item_whose_weight_is_less_than_or_equal_to_max_weight = self.heaviest_item_whose_weight_is_less_than_or_equal_to(max_weight)
    self.items.remove(heaviest_item_whose_weight_is_less_than_or_equal_to_max_weight)
    return heaviest_item_whose_weight_is_less_than_or_equal_to_max_weight
    
  def heaviest_item_whose_weight_is_less_than_or_equal_to(self, max_weight):
    items_heavier_than_weight = filter(lambda item: item <= max_weight , self.items)
    return max(self.items)

minimum_number_of_cartons_required = 0
items = Items(item_weights)

while True:
  if items.none_remaining():
    break

  heaviest_item = items.pop_heaviest_item()
  if items.none_remaining():
    minimum_number_of_cartons_required = minimum_number_of_cartons_required + 1
    break

  carton_remaining_weight = carton_max_weight - heaviest_item
  if (carton_remaining_weight == 0):
    minimum_number_of_cartons_required = minimum_number_of_cartons_required + 1
    continue

  items.pop_heaviest_item_whose_weight_is_less_than_or_equal_to(carton_remaining_weight)
  minimum_number_of_cartons_required = minimum_number_of_cartons_required + 1

print(minimum_number_of_cartons_required)
