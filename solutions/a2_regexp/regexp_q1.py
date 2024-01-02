import re

GOOD = (
    'B1 1AA',    'M13 9PL',
    'EX1 3PB',    'AB22 8GT',
    'W1A 1AA',    'SW1A 0AA',
)

BAD = (
    '1B 1AA',    'B1 11A',
    'B1 111',    'MA 9PL',
    'EX1 33P',   'EX1 3PBB',
    'AB228 GT',  'AB228 8GT',
    'WAA 1AA',   'W10A 1AA',
    'W1A1 1AA',   'SW10A 0AA',
    'SW1 A0AA',
)


def validate_postcode(postcode):
    return re.match(r'[A-Z]{1,2}(\d{1,2}|\d[A-Z])\s+\d[A-Z]{2}$', postcode.strip(), re.IGNORECASE) is not None


def capture_town(postcode):
    match = re.match(r'([A-Z]{1,2})(\d{1,2}|\d[A-Z])\s+\d[A-Z]{2}$', postcode.strip(), re.IGNORECASE)
    if match:
        return match.group(1)
    return None


def validate():
    for good in GOOD:
        if not validate_postcode(good):
            print('Valid postcode {} not accepted'.format(good))
    for bad in BAD:
        if validate_postcode(bad):
            print('Invalid postcode {} accepted'.format(bad))


def capture():
    for good in GOOD:
        town = capture_town(good)
        if town is not None:
            print('Captured town {} from {}'.format(town, good))
        else:
            print('Capture {} failed'.format(good))
    for bad in BAD:
        town = capture_town(bad)
        if town is not None:
            print('Capture {} failed'.format(bad))

def main():
    validate()
    capture()

if __name__ == '__main__':
    main()