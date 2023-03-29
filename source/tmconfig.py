class DocumentInfos:

    title = u'''Rédaction d'un rapport écrit avec Sphinx '''
    first_name = 'Nom de famille'
    last_name = 'Prénom'
    author = f'{first_name} {last_name}'
    year = u'2023'
    month = u'Janvier'
    seminary_title = u'Développement Web'
    tutor = u"Cédric Donner"
    release = "(Version intermédiaire)"
    repository_url = "https://github.com/username/repo"

    @classmethod
    def date(cls):
        return cls.month + " " + cls.year

infos = DocumentInfos()