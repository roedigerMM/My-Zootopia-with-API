from animals_html_handling import write_new_html_file
from data_fetcher import fetch_data


def serialize_animal(animal):
    """ Serializes a single animal item into the needed structure for the html template and
    returns it as a string."""
    output = ""
    output += "<li class='cards__item'>"
    if "name" in animal:
        output += f"<div class='card__title'>{animal['name']}</div>\n"
    if "scientific_name" in animal["taxonomy"]:
        output += f"<div class='card__subtitle'>{animal['taxonomy']['scientific_name']}</div>\n"
    output += "<div class='card__text'>\n<ul>"
    if "diet" in animal["characteristics"]:
        output += f"<li><strong>Diet:</strong> {animal['characteristics']['diet']}</li>\n"
    if "locations" in animal and len(animal["locations"]) > 0:
        output += f"<li><strong>Location:</strong> {animal['locations'][0]}</li>\n"
    if "type" in animal["characteristics"]:
        output += f"<li><strong>Type:</strong> {animal['characteristics']['type']}</li>\n"
    if "lifespan" in animal["characteristics"]:
        output += f"<li><strong>Lifespan:</strong> {animal['characteristics']['lifespan']}</li>\n"
    output += "</ul>\n</div>\n</li>\n"
    return output


def get_animals_data(animal_data):
    """ Creates and returns the complete String with animal information to be inserted
    into the html template """
    output = ""
    for animal in animal_data:
        output += serialize_animal(animal)
    return output


def main():
    while True:
        user_animal = input("Enter a name of an animal: ")
        if user_animal != "" and type(user_animal) == str:
            break
    animals_data = fetch_data(user_animal)
    if len(animals_data) == 0:
        write_new_html_file(f'<h2>The animal "{user_animal}" does not exist.</h2>')
    else:
        write_new_html_file(get_animals_data(animals_data))

if __name__ == "__main__":
    main()