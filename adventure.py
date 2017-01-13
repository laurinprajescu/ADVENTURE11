from data import locations
from data import descriptions
from data import room_object

directions = {
    'west': (-1, 0),
    'east': (1, 0),
    'north': (0, -1),
    'south': (0, 1),
}

position = (0, 0)
inventory = []

while True:
    location = locations[position]

    print 'you are at the %s' % location

    valid_directions = {}
    for k, v in directions.iteritems():
        possible_position = (position[0] + v[0], position[1] + v[1])
        possible_location = locations.get(possible_position)
        if possible_location:
            print 'to the %s is a %s' % (k, possible_location)
            valid_directions[k] = possible_position

    direction = raw_input('which direction do you want to go?\n')
    new_position = valid_directions.get(direction)

    if new_position:
        position = new_position
        inventory.append(room_object[position])
        print descriptions[position]
    else:
        print "sorry, that isn't a valid direction"

    for i in inventory:
        print "You aquaired : a " + i

    print "This is the map :\nH P\nL M"





