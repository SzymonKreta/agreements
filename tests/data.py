USERS = (
    ('Andrzej', 'Kowalski', 'foo', '00-111'),
    ('Bogdan', 'Nowak', 'bar', '01-111')
)

NOT_VALID_USERS = (
    ('Andrzej', 'Kowalski', 'foo', "1234"),
    ('Bogdan', 'Nowak', "S" * 61, '01-111'),
    ('Andrzej', "A" * 151, 'foo', '00-111'),
    ("B" * 61, 'Kowalski', 'foo', '00-111')
)
