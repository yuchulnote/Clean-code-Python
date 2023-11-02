class AsciiArt:
    def __init__(self, characters):
        self._characters = characters

    @classmethod
    def fromFile(cls, filename):
        with open(filename) as fileObj:
            characters = fileObj.read()
            return cls(characters)

    def display(self):
        print(self._characters)


# 다른 AsciiArt 메소드들은 여기에...
face1 = AsciiArt(" ______\n" + "| . .  |\n" + "|      |\n" + " ------")
face1.display()

# face2 = AsciiArt.fromFile("face.txt")
