class DocumentInfos:

    title = u'''Rédaction d'un rapport écrit avec Sphinx '''
    first_name = 'Donner'
    last_name = 'Cédric'
    author = f'{first_name} {last_name}'
    year = u'2023'
    month = u'Mars'
    seminary_title = u'Développement Web'
    tutor = u"Cédric Donner"
    release = "(Version intermédiaire)"
    repository_url = "https://github.com/informatiquecsud/sphinx-tm-template-2023"

    @classmethod
    def date(cls):
        return cls.month + " " + cls.year

infos = DocumentInfos()