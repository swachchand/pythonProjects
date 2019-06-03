Interactive dictionary
this gives more verbose meaning of any words you type in and also provides an alternative if you mistype a word


the program references a large JSON file which is stored in a dict. format.
The file contains a word and it's corresponding meaning.
e.g.: If user types in rain, the user is shown the definition of Rain verbosely.
The program also uses a probablility to check if a user has entered a typo and suggests a correct meaning for that specific Typo.
To check for the probability, get_close_matches from difflib is implemented.
