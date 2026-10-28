morning = {"tea", "toast", "fruit"}
evening = {"rice", "tea", "vegetables"}
print(f"Eaten at both meals: {morning & evening}")
print(f"All different foods: {morning | evening}")
print(f"Only at breakfast: {morning - evening}")
