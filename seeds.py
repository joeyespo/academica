"""\
Seed data.
"""

users = [
    {
        'username': 'lee_ngo',
        'first': 'Lee',
        'last': 'Ngo',
        'email': 'lee.ngo@gmail.com',
        'phone': '412-555-5555',
        'hours': 'I NEVER SLEEP',
        'available': True,
        'education': 'TODO',    # HTML
        'positions': 'TODO',    # HTML
    },
]

universities = [
    {
        'username': 'LeeU',
        'title': 'Lee University',
        'users': ['lee_ngo'],
    },
]


def find(function, items):
    for item in items:
        if function(item):
            return item
