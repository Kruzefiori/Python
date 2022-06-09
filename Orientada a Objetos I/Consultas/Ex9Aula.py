class Musica:
    def __init__(self, titulo, artista, album, nroFaixa):
        self.__titulo = titulo
        self.__artista = artista
        self.__album = album
        self.__nroFaixa = nroFaixa

        artista.addMusica(self)

    def getTitulo(self):
        return self.__titulo
    
    def getArtista(self):
        return self.__artista

    def getAlbum(self):
        return self.__album

    def getNroFaixa(self):
        return self.__nroFaixa
    

class Album:
    def __init__(self, titulo, artista, ano):
        self.__titulo = titulo
        self.__artista = artista
        self.__ano = ano

        self.__faixas = []
        artista.addAlbum(self)

    def getTitulo(self):
        return self.__titulo

    def getArtista(self):
        return self.__artista

    def getAno(self):
        return self.__ano

    def getFaixas(self):
        return self.__faixas

    def addFaixa(self, titulo, artista=None):
        if artista is None:
            artista = self.__artista
        nroFaixa = len(self.__faixas)
        musica = Musica(titulo, artista, self, nroFaixa)
        self.__faixas.append(musica)

class Artista:
    def __init__(self, nome):
        self.__nome = nome

        self.__albuns = []
        self.__musicas = []

    def getNome(self):
        return self.__nome

    def getAlbuns(self):
        return self.__albuns

    def getMusicas(self):
        return self.__musicas

    def addAlbum(self, album):
        self.__albuns.append(album)

    def addMusica(self, musica):
        self.__musicas.append(musica)

    

class Playlist:
    def __init__(self, nome):
        self.__nome = nome
        self.__musicas = []

    def getNome(self):
        return self.__nome

    def getMusicas(self):
        return self.__musicas

    def addMusica(self , musica):
        self.__musicas.append(musica)
         

if __name__ == "__main__":    
    listaAlbuns = []
    art1 = Artista('Coldplay')
    album1 = Album('Mylo Xyloto', art1, 2011)
    album1.addFaixa('Paradise')
    album1.addFaixa('Hurts Like Heaven')
    album1.addFaixa('Charlie Brown') 
    listaAlbuns.append(album1)

    album2 = Album('A Head Full of Dreams', art1, 2015)
    album2.addFaixa('A Head Full of Dreams')
    album2.addFaixa('Birds')
    album2.addFaixa('Everglow')
    listaAlbuns.append(album2)

    art2 = Artista('Skank')
    album3 = Album('Siderado', art2, 1998)
    album3.addFaixa('Resposta')
    album3.addFaixa('Saideira')
    album3.addFaixa('Romance Noir')
    listaAlbuns.append(album3)

    # Criar uma playlist com as músicas do album "Mylo Xyloto"
    pl1 = Playlist('Play do Mylin')
    for each in album1.getFaixas():
        pl1.addMusica(each)
    
    print(pl1.getNome())
    for each in pl1.getMusicas():
        print(each.getTitulo())
       
    # Criar uma playlist com todas as músicas do Coldplay  
    print() 
    pl2 = Playlist('Todas dos Reis da Formatura')
    for each in art1.getMusicas():
        pl2.addMusica(each)
    print(pl2.getNome())
    for each in pl2.getMusicas():
        print(each.getTitulo())

    # Criar uma playlist contendo uma música de cada album
    print()
    pl3 = Playlist("Mcauly do funk")
    for each in listaAlbuns:
        musicas = each.getFaixas()
        pl3.addMusica(musicas[0])

    for each in pl3.getMusicas():
        print(each.getTitulo())
    
    
    