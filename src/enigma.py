import numpy as np
import random as random
from constants import alphabet, rotor_combination, reflector_combination

def create_rotors(nr_rotors):
	rotors = []
	for i in range(nr_rotors):
		rotor = {}
		for i in range(len(rotor_combination)):
			rotor[alphabet[i]] = rotor_combination[i]

		rotors.append(rotor)

	return rotors

def create_reflector():
	reflector = {}
	for i in range(len(reflector_combination)):
		reflector[alphabet[i]] = reflector_combination[i]

	return reflector

def create_random_enigma_setup(nr_rotors):
	plugboard = generate_random_plugboard_combination()
	rotors = create_rotors(nr_rotors)
	reflector = create_reflector()

	return plugboard, rotors, reflector

def shift_values(rotor):
	combination = list(rotor.values())
	new_combination = np.roll(combination, 1)
	for key, index in zip(rotor.keys(),range(len(rotor))):
		rotor[key] = new_combination[index]

	return rotor

def update_rotors(rotors, rotors_rotation):
	rotors_rotation[0] = rotors_rotation[0] + 1
	rotors[0] = shift_values(rotors[0])
	for i in range(len(rotors_rotation)):		
		if rotors_rotation[i] % len(alphabet) == 0 and rotors_rotation[i] != 0:
			rotors_rotation[i] = 0		
			if i + 1 < len(rotors):
				rotors_rotation[i+1] = rotors_rotation[i+1] + 1
				rotors[i+1] = shift_values(rotors[i+1])
			
	return rotors

def run_rotors(letter, letter_path, rotors, reflector):
	new_letter = letter
	for j in range(len(rotors)):
		rotor = rotors[j]
		new_letter = rotor[new_letter]
		letter_path = letter_path + " -> " + new_letter

	new_letter = reflector[new_letter]
	letter_path = letter_path + " -> " + new_letter

	for _rotor in reversed(rotors):
		new_letter = list(_rotor.keys())[list(_rotor.values()).index(new_letter)][0]
		letter_path = letter_path + " -> " + new_letter

	return new_letter, letter_path

def run_plugboard(letter, letter_path, plugboard, is_reverse = False):
	if not is_reverse:
		new_letter = plugboard[letter]
		letter_path = letter + " -> " + new_letter
	else: 
		new_letter = list(plugboard.keys())[list(plugboard.values()).index(letter)][0]
		letter_path = letter_path + " -> " + new_letter

	return new_letter, letter_path

def encode_letter(letter, plugboard, rotors, reflector):
	path = ""
	coded_letter, path = run_plugboard(letter, path, plugboard)
	coded_letter, path = run_rotors(coded_letter, path, rotors, reflector)
	coded_letter, path = run_plugboard(coded_letter, path, plugboard, True)

	return coded_letter

def generate_random_plugboard_combination(nr_pairs = 13):

	plugboard = {}

	free_indexes = np.linspace(0,25,num=26, dtype='int')
	final_combination = np.empty(len(alphabet),dtype='str')

	for i in range(len(final_combination)):
		final_combination[i] = alphabet[i]


	while free_indexes.size != 0 and nr_pairs >= 0:
		nr_pairs = nr_pairs - 1
		index1 = random.choice(free_indexes)
		free_indexes = np.delete(free_indexes, np.where(free_indexes == index1))

		index2 = random.choice(free_indexes)
		free_indexes = np.delete(free_indexes, np.where(free_indexes == index2))

		final_combination[index1] = alphabet[index2]
		final_combination[index2] = alphabet[index1]

	for letter, index in zip(alphabet, range(len(alphabet))):
		plugboard[letter] = final_combination[index]
		
	return plugboard

def encrypt(str: str) -> str:
	'''
	    Criptografa uma string usando o algoritmo Enigma.

		param str: string a ser criptografada
        type str: str
        return: string criptografada
        type: str
	'''
	encrypted_str = ""	
	nr_rotors = 3
	rotors_rotation = []
	for i in range(nr_rotors):
		rotors_rotation.append(0)

	plugboard, rotors, reflector = create_random_enigma_setup(nr_rotors)

	for letter in str:
		letter = letter.upper()
		if letter not in alphabet:
			encrypted_str += letter
			continue
		encrypted_str += encode_letter(letter, plugboard, rotors, reflector)
		rotors = update_rotors(rotors, rotors_rotation)
	
	return encrypted_str

