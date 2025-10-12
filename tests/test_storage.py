import os
import json
from util.storage import save_game, load_game #för att kunna testa dessa def.

def test_save_and_load_game(tmp_path):
    test_data = {"health": 100, "location": "forest"} #bara random saker att testa
    save_file = tmp_path / "test_save.json"

    #Sparar data
    save_game(test_data, filename=save_file)

    #Laddar upp data igen
    loaded_data = load_game(filename=save_file)

    #Se ifall resultatet är detsamma
    assert loaded_data == test_data