## This file contains the data necessary for the report card mechanism to function.




## The base info dictionary (I don't even think this is necessary anymore but it doesn't hurt to have it here).
define info = {
    "current_height": "", 
    "blood_type": "", 
    "birthday": "",
    "likes": "",
    "dislikes": "",
    "ultimate": "",
    "text": "",
    "ft1": "",
    "ft2": "",
    "ft3": ""
    }


## These dictionaries contain the report card information for each character.

define player_info = {
    "current_height": "162 cm", 
    "blood_type": "A", 
    "birthday": "January 13",
    "likes": "Weighted blankets",
    "dislikes": "Themself",
    "ultimate": "...",
    "text": "The player character. Currently with no set name or ultimate, but we did our best to make them look cool.",
    "ft1": "asdadas",
    "ft2": "asdfsdfg",
    "ft3": "dsfh"
    }

define luke_info = {
    "current_height": "175 cm", 
    "blood_type": "AB", 
    "birthday": "May 12",
    "likes": "Being alone",
    "dislikes": "Showering",
    "ultimate": "???",
    "text": "...",
    "ft1": "asdfasdf",
    "ft2": "adg",
    "ft3": "ahgwaer"
    }

define david_info = {
    "current_height": "172 cm", 
    "blood_type": "B", 
    "birthday": "March 17",
    "likes": "Free stuff",
    "dislikes": "Unironed clothes",
    "ultimate": "Wind Shitter",
    "text": "A strange fellow. He seems to think he is a character from a video game. He also denies being hardstuck gold.",
    "ft1": "",
    "ft2": "",
    "ft3": ""
    }

define sean_info = {
    "current_height": "160 cm", 
    "blood_type": "AB", 
    "birthday": "November 13",
    "likes": "Burping",
    "dislikes": "Grease, The dark",
    "ultimate": "Monokuma",
    "text": "...",
    "ft1": "",
    "ft2": "",
    "ft3": ""
    }

define julian_info = {
    "current_height": "179 cm", 
    "blood_type": "O", 
    "birthday": "April 20",
    "likes": "East Asian fashion",
    "dislikes": "Untidyness",
    "ultimate": "Vtuber \"Appreciator\"",
    "text": "...",
    "ft1": "",
    "ft2": "",
    "ft3": ""
    }

define riley_info = {
    "current_height": "190 cm", 
    "blood_type": "A", 
    "birthday": "August 21",
    "likes": "Illicit drugs, rocks",
    "dislikes": "The law",
    "ultimate": "Druggie",
    "text": "...",
    "ft1": "",
    "ft2": "",
    "ft3": ""
    }

define mitch_info = {
    "current_height": "175 cm", 
    "blood_type": "A", 
    "birthday": "June 14",
    "likes": "JoJo's references",
    "dislikes": "Retail",
    "ultimate": "Shitposter",
    "text": "...",
    "ft1": "",
    "ft2": "",
    "ft3": ""
    }

define will_info = {
    "current_height": "180 cm", 
    "blood_type": "O", 
    "birthday": "October 24",
    "likes": "Dictionaries",
    "dislikes": "Sacrilege",
    "ultimate": "God Complex",
    "text": "No comment.",
    "ft1": "",
    "ft2": "",
    "ft3": ""
    }

define johan_info = {
    "current_height": "180 cm", 
    "blood_type": "A", 
    "birthday": "November 26",
    "likes": "Obscure 2010 anime",
    "dislikes": "The colour red",
    "ultimate": "Dad",
    "text": "...",
    "ft1": "",
    "ft2": "",
    "ft3": ""
    }

define mel_info = {
    "current_height": "150 cm", 
    "blood_type": "A", 
    "birthday": "April 4",
    "likes": "Sea urchins",
    "dislikes": "Chihuahuas",
    "ultimate": "Animal Caretaker",
    "text": "A small girl who has the emotional range of an Olympic swimming pool. Her shoes add an extra five centimetres to her height, it seems.",
    "ft1": "",
    "ft2": "",
    "ft3": ""
    }

define felicity_info = {
    "current_height": "167 cm", 
    "blood_type": "AB", 
    "birthday": "May 29",
    "likes": "Otome games",
    "dislikes": "Spending money",
    "ultimate": "Simp",
    "text": "A girl who's nice enough, most of the time. She tends to \"freeze\" occassionally while speaking, but nobody else seems to notice...",
    "ft1": "",
    "ft2": "",
    "ft3": ""
    }




## This dictionary assigns a number to each character, which is used when cycling through the report card.
define characters = {
    1:player_info,
    2:luke_info,
    3:david_info,
    4:sean_info,
    5:julian_info,
    6:riley_info,
    7:mitch_info,
    8:will_info,
    9:johan_info,
    10:mel_info,
    11:felicity_info
}

## This list stores the base names of each character (which is used when calling the file name, and for string reference).
define character_names = ["player", "luke", "david", "sean", "julian", "riley", "mitch", "will", "johan", "mel", "felicity"]


## This dictionary stores the friendship level information for each character. Default is zero.
define character_friendship = {
    "player": 0,
    "luke":0,
    "david": 0,
    "sean": 0,
    "julian":0,
    "riley": 0,
    "mitch": 0,
    "will":0,
    "johan": 0,
    "mel": 0,
    "felicity": 2
}

