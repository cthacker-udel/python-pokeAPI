import collections
from collections import defaultdict
from dataclasses import dataclass
import requests
import json

pokemon_name = input("Enter the name of the pokemon ")
while type(pokemon_name) != type(''):
    pokemon_name = input('Please enter only strings')

req = requests.get('https://pokeapi.co/api/v2/pokemon/{}'.format(pokemon_name))  # .json()
json_data = req.json()
print(json_data.keys())
print('\n\n')
#comment
# moves = {}
# machine = {}
# tutor = {}
# levelup = {} ##organize into 3 lists, machine moves, tutor moves, levelup, classified by which game too
# print(json_data['moves'])
# print(json_data['abilities']) multiple
# print(json_data['held_items']) multiple
# print(json_data['game_indices'])
x = {}
print('\n\n')


class Pokemon:

    def __init__(self, json_data):
        self.forms = {}  # Check
        forms_counter = 0  # check
        self.abilities = []  # check
        self.hidden_abilities = []  # check
        self.versions = {}  # Check
        self.types = []  # Check
        self.held_items = {}  # Check
        self.item_versions = []  # Check
        self.moves = {}
        self.machine = {}
        self.tutor = {}
        self.levelup = {}
        self.pokemon = json_data['name']
        self.base_experience = json_data['base_experience']
        self.height = json_data['height']
        self.weight = json_data['weight']
        self.hp = json_data['stats'][0]['base_stat']
        self.attack = json_data['stats'][1]['base_stat']
        self.defense = json_data['stats'][2]['base_stat']
        self.special_attack = json_data['stats'][3]['base_stat']
        self.special_defense = json_data['stats'][4]['base_stat']
        self.speed = json_data['stats'][5]['base_stat']
        for eachappearance in json_data['game_indices']:
            self.versions['{}'.format(eachappearance['version']['name'])] = eachappearance['game_index']
        for eachform in json_data['forms']:
            forms_counter += 1
            self.forms[forms_counter] = eachform['name']
        for eachtype in json_data['types']:
            self.types.append(eachtype['type']['name'])
        for eachability in json_data['abilities']:
            if eachability['is_hidden'] == False:
                self.abilities.append(eachability['ability']['name'])
            elif eachability['is_hidden'] == True:
                self.hidden_abilities.append(eachability['ability']['name'])
        for eachitem in json_data['held_items']:
            for eachversion in eachitem['version_details']:
                self.item_versions.append(eachversion['version']['name'])
            self.held_items[eachitem['item']['name']] = self.item_versions
            self.item_versions = []
        self.item_versions = []
        for eachmove in json_data['moves']:
            # print(eachmove)
            print('\n')
            self.moves[eachmove['version_group_details'][0]['version_group']['name']] = {}
            self.moves[eachmove['version_group_details'][0]['version_group']['name']]['machine'] = {}
            self.moves[eachmove['version_group_details'][0]['version_group']['name']]['tutor'] = {}
            self.moves[eachmove['version_group_details'][0]['version_group']['name']]['levelup'] = {}
            for eachversion in eachmove['version_group_details']:
                if eachversion['move_learn_method']['name'] == 'machine':
                    self.machine[eachmove['move']['name']] = 'Level : {}'.format(eachversion['level_learned_at'])
                elif eachversion['move_learn_method']['name'] == 'tutor':
                    self.tutor[eachmove['move']['name']] = 'Level : {}'.format(eachversion['level_learned_at'])
                elif eachversion['move_learn_method']['name'] == 'level-up':
                    self.levelup[eachmove['move']['name']] = 'Level : {}'.format(eachversion['level_learned_at'])
            self.moves[eachmove['version_group_details'][0]['version_group']['name']]['machine'] = self.machine
            self.moves[eachmove['version_group_details'][0]['version_group']['name']]['tutor'] = self.tutor
            self.moves[eachmove['version_group_details'][0]['version_group']['name']]['levelup'] = self.levelup

    def get_basehp(self):
        return self.hp

    def get_baseattack(self):
        return self.attack

    def get_basedefense(self):
        return self.defense

    def get_basespecialattack(self):
        return self.special_attack

    def get_basespecialdefense(self):
        return self.special_defense

    def get_basespeed(self):
        return self.speed

    def get_helditems(self):
        return self.held_items

    def get_abilities(self):
        return self.abilities

    def get_hidden_abilities(self):
        return self.hidden_abilities

    def get_type(self):
        return self.types

    def get_forms(self):
        return self.forms

    def get_appearances(self):
        return self.versions


pokemon = Pokemon(json_data)
print(len(pokemon.get_appearances()))
print(type(pokemon.get_appearances()))
for eachversion in pokemon.get_appearances().keys():
    x = lambda eachversion: [eachversion]
    y = x(eachversion)
    newdict = dict.fromkeys(y, '')

"""
----------------------------------------------------------JUNK DEPOSIT--------------------------------------------------

for eachitem in json_data['held_items']: #eachitem = eachitem --> eachitem['name'] = name --> eachitem['version_details']
    print(eachitem)                                                                          #is every version it is in
    print(eachitem['item']['name'])                                                          # so we must make a dictionary
    #print(eachitem['version_details'][0]['version']['name'])      #version details           # for eachitem is a key
    print('\n\n')                                                                            # which results in a value of
    #for eachversion in eachitem['version_details']:                                          # lists which contain the
    #    print(eachversion)                                                                   # versions
    #    newlist.append(eachversion['version']['name'])
    #item[eachitem['item']['name']] = newlist
    #newlist = []

    #print('MOVES##### {}'.format(moves))
    #moves
    #So i have a dictionary variable and i want to make a dictionary within the dictionary with keys
    #red = {'moves': {move1: description, move2: description}}
    #red['moves'] = {}

    ///////////////

    for eachmove in json_data['moves']:
    #print(eachmove)
    print('\n')
    moves[eachmove['version_group_details'][0]['version_group']['name']] = {}
    moves[eachmove['version_group_details'][0]['version_group']['name']]['machine'] = {}
    moves[eachmove['version_group_details'][0]['version_group']['name']]['tutor'] = {}
    moves[eachmove['version_group_details'][0]['version_group']['name']]['levelup'] = {}
    for eachversion in eachmove['version_group_details']:
        if eachversion['move_learn_method']['name'] == 'machine':
            machine[eachmove['move']['name']] = 'Level : {}'.format(eachversion['level_learned_at'])
        elif eachversion['move_learn_method']['name'] == 'tutor':
            tutor[eachmove['move']['name']] = 'Level : {}'.format(eachversion['level_learned_at'])
        elif eachversion['move_learn_method']['name'] == 'level-up':
            levelup[eachmove['move']['name']] = 'Level : {}'.format(eachversion['level_learned_at'])
    moves[eachmove['version_group_details'][0]['version_group']['name']]['machine'] = machine
    moves[eachmove['version_group_details'][0]['version_group']['name']]['tutor'] = tutor
    moves[eachmove['version_group_details'][0]['version_group']['name']]['levelup'] = levelup

"""
