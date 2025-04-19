# Burglary Series (14): Adjectives Total
# You call your spouse in anger and a "little" argument takes place. Count the total amount of insults used. Given a dictionary of insults, return the total amount of insults used.

def total_amount_adjectives(word_dict):
    return len(word_dict.values())

print(total_amount_adjectives({ "a": "idiot", "b": "idiot", "c": "idiot" }))