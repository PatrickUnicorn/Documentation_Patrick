class DocumentInfos:

    title = u'ProjetRoguelikeGame'
    first_name = 'Patrick'
    last_name = 'Oliveira Alves'
    author = f'{first_name} {last_name}'
    year = u'2024'
    month = u'Janvier'
    seminary_title = u'Projet OCI'
    tutor = u"Cédric Donner"
    release = "(Version finale)"
    repository_url = "https://github.com/<username>/<reponame>"

    @classmethod
    def date(cls):
        return cls.month + " " + cls.year

infos = DocumentInfos()