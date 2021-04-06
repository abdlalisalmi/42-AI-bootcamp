languages = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
    }
for key in languages.keys():
    print(f"{key} was created by {languages.get(key)}")
