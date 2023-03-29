class DocumentInfos:

    title = u'''Rédaction d'un rapport écrit avec Sphinx '''
    first_name = 'Cédric'
    last_name = 'Donner'
    address = u'Chemin des Combes 26, 1630 Bulle'
    author = f'{first_name} {last_name}'
    the_date = f'Le 29 mars 2023'
    year = u'2023'
    month = u'Mars'
    seminary_title = u'Développement Web'
    tutor = u"Cédric Donner"
    release = ""
    repository_url = "https://github.com/informatiquecsud/sphinx-tm-template-2023"

    @classmethod
    def date(cls):
        return cls.month + " " + cls.year

infos = DocumentInfos()