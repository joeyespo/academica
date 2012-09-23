 # -*- coding: utf-8 -*-
"""\
Seed data.
"""

users = [
    {
        'username': 'philip.grant',
        'first': 'Philip',
        'last': 'Grant',
        'credentials': 'PhD',
        'interests': '',
        'email': 'p.grant@uoe.edu',
        'phone': '412-555-5555',
        'hours': None,
        'available': True,
        'education': [
            {
                'university': 'University of California, Irvine',
                'field': 'Ph.D., Sociocultural Anthropology',
                'years': '2006 – 2012',
            },
            {
                'university': "Institut d'Etudes politiques de Paris",
                'field': 'DEA, Sociétés et politiques comparées-monde musulman',
                'years': '2003 – 2005',
            },
            {
                'university': 'University of Oxford',
                'field': 'BA, Modern History',
                'years': '1995 – 1998',
            },
        ],
        'positions': [
            {
                'title': 'Research Fellow in Social Studies of Finance',
                'location': 'University of Edinburgh',
                'years': 'September 2012 – Present (1 month) Edinburgh, United Kingdom',
            },
            {
                'title': 'Teaching Assistant, School of Social Sciences',
                'location': 'UC Irvine',
                'years': 'January 2007 – December 2011 (5 years) Irvine, CA',
            },
            {
                'title': 'Lecturer',
                'location': 'Linguistic Anthropology\nUC Irvine',
                'years': 'July 2011 – September 2011 (3 months) Irvine, CA',
            },
            {
                'title': '',
                'location': '',
                'years': '',
            },
        ],
        'awards': [
            'Fulbright Fellowship 2009-2010',
            'Wenner-Gren Dissertation Development Award 2010-2011',
            'National Science Foundation Dissertation Development Award 2011-2012 ',
            'School of Social Sciences Top Dissertation Award (granted 2012)',
        ],
        'skills': [
            'Ethnographic fieldwork',
            'SPSS',
            'R',
            'Novio',
            'Atlas.ti',
            'Stata',
            'Oral life history',
            'Social Network Analysis',
        ],
        'theory': [
            'Pierre Bourdieu',
            'Michel Foucault',
            'Gilles Deleuze',
            'Stephen Hawking',
        ],
        'languages': [
            'English (native fluent)',
            'Persian (proficient)',
            'French (proficient)',
            'Italian (proficient)',
            'Spanish (proficient)',
            'Arabic (advanced)',
            'German (advanced)',
        ],
    },
    {
        'username': 'lee.ngo',
        'first': 'Lee',
        'last': 'Ngo',
        'credentials': 'Founder',
        'interests': '',
        'email': 'lee.ngo@gmail.com',
        'phone': '412-555-5555',
        'hours': 'I NEVER SLEEP',
        'available': True,
        'education': [],
        'positions': [],
        'awards': [],
        'skills': [],
        'theory': [],
        'languages': [],
    },
]

universities = [
    {
        'username': 'LeeU',
        'title': 'Lee University',
        'users': ['lee'],
    },
]


def find(function, items):
    for item in items:
        if function(item):
            return item
