class DocumentInfos:

    title = u'''Rédaction d'un rapport écrit avec Sphinx'''
    first_name = 'Jules'
    last_name = 'Tartempion'
    address = u'Chemin des Allouettes 45, 1700 Fribourg'
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

tmconfig = DocumentInfos()