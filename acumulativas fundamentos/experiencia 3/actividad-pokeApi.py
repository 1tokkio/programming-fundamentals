import tkinter as tk 
import requests
from io import BytesIO
from PIL import Image, ImageTk
import random
from customtkinter import * #for custom tkinter 

def search_pokemon(name_pokemon=None):
    if not name_pokemon:
     name_pokemon = entry_pokemon.get().lower()

    url = f"https://pokeapi.co/api/v2/pokemon/{name_pokemon}"
    response = requests.get(url)

    if response.status_code == 200:
        ans = response.json()
        name = ans["name"]
        number = ans["id"]
        type = [type["type"]["name"] for type in ans["types"]]

        result = (f"name: {name} \nnumber: {number} \ntypes: {', '.join(type)}")

        img_url = ans["sprites"]["front_default"]
        rsp_img= requests.get(img_url)
        img = Image.open(BytesIO(rsp_img.content))
        img = img.resize((200, 200), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(img)
        label_img.config(image=photo)
        label_img.image = photo

        stats = ans["stats"]
        stats_view = "\n".join([f"{stat['stat']['name']} : {stat['base_stat']}" for stat in stats])
        result = f"\n\nbase stats:  \n{stats_view}"

        species_url = f"https://pokeapi.co/api/v2/pokemon-species/{number}/"
        rsp_species = requests.get(species_url)
        if rsp_species.status_code == 200:
            ans_species = rsp_species.json()
            description = next(entry['flavor_text'] for entry in ans_species["flavor_text_entries"] if entry['language']['name'] == 'en').replace('\n', ' ').replace('\f', ' ')
            result += f"\n\ndescriptión:\n{description}"
        else:
            result = "\ndescription is not available."

    else:
        result = "the pokemon was not found."  
        label_img.config(image=None) 

    label_result.config(text=result)

def clean():
    entry_pokemon.delete(0, tk.END)  
    label_result.config(text="")  
    label_img.config(image=None)  

def view_random_pokemon():
    random_number = random.randint(1, 898)
    search_pokemon(random_number)  

window = tk.Tk()
window.title("")

label_pokemon = tk.Label(window, text="enter the name of the pokemon: ")
label_pokemon.pack()
entry_pokemon = tk.Entry(window)
entry_pokemon.pack()
search_button = tk.Button(window, text="search", command=search_pokemon)
search_button.pack()
clear_button = tk.Button(window, text="clear", command=clean)
clear_button.pack()
random_button = tk.Button(window, text="random pokemon", command=view_random_pokemon)
random_button.pack()
label_result = tk.Label(window, text="", wraplength=400)
label_result.pack()
label_img = tk.Label(window)
label_img.pack()

window.mainloop()