def response(hey_bob):
    if hey_bob.endswith('?')  and not hey_bob.isupper():
        return 'Sure.'
    elif hey_bob.isupper() and '?' not in hey_bob:
        return 'Whoa, chill out!'
    elif hey_bob.isupper() and '?' in hey_bob:
        return "Calm down, I know what I'm doing!"  
    elif hey_bob.strip() == '':
    #and hey_bob[-1] == " ":
        return "Fine. Be that way!"
    else:
        return 'Whatever.'
