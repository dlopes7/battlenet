import battlenet


#def __init__(self, api_key='', public_key=None, private_key=None, game='wow', locale=None):

if __name__ == '__main__':
    c = battlenet.Connection(api_key='fb8c6j4d4avhh9xe6f5wvw7kqh9push8',
                             locale='en')

    region = battlenet.UNITED_STATES

    guild = c.get_guild(region, 'Azralon', 'BURN', fields=['members'])
    for member in guild.members:
        print(member['character'])



