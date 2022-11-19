postcards = {
    "Maria": "London",
    "Lorenzo": "Milan",
    "Oleg": "Canberra",
    "Hans": "Calgary",
    "Mark": "Milan",
    "Alex": "Krakow",
    "Julia": "Murmansk"
}
postcards["Petra"] = "Paris"
postcards["Ivan"] = "Moscow"
postcards["Oleg"] = "Sydney"
print(postcards)
postcards = (list(postcards.values()))
postcards = set(postcards)
print(postcards)
print(len(postcards), "unique cities")






# Алиса говорит, что в ее коллекции более 10 уникальных городов. Сколько их на самом деле?
# Выведите названия этих городов.