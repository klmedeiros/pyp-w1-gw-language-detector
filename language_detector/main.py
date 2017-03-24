# -*- coding: utf-8 -*-

"""This is the entry point of the program."""

def detect_language(text, languages):
    """Returns the detected language of given text."""
    # implement your solution here
    answer = text.split()
    
    english_count = 0
    spanish_count = 0
    german_count = 0

    # adg psuedocode
    for language in languages:
        if language['name'] == 'Spanish':
            for word in language['common_words']:
                spanish_count += answer.count(word)
                
       
        if language['name'] == 'German':
            for word in language['common_words']:
                german_count += answer.count(word)
                
        
        if language['name'] == 'English':
            for word in language['common_words']:
                english_count += answer.count(word)
                
    if english_count > spanish_count and english_count > german_count:
        return "English"
    elif spanish_count > english_count and spanish_count > german_count:
        return "Spanish"
    elif german_count > english_count and spanish_count < german_count:
        return "German"