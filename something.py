# A script to create a standard 52-card deck

def create_ColourCards():
    colours = ['Red', 'Blue', 'Yellow', 'Green']
    types = ['0','1','2', '3', '4', '5', '6', '7', '8', '9', 'Skip', 'Reverse','skip all', 'Draw Two','drop all',]
    amounts = ['1st' ,'2nd' ,'3rd']
    deck = [f"{amount} {colour} {type} " for amount in amounts for colour in colours for type in types]
    return deck
def create_WildCards():
    wild_cards = ['draw until', 'wild +6', 'wild +10', 'wild reverse +4']#
    amounts = [8,4,4,8]
    deck = [f"{wild_card} " for wild_card in wild_cards]
    return deck
if __name__ == "__main__":
    deck = create_WildCards()
    for card in deck:
        print(card)
