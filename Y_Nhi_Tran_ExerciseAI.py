# Y Nhi Tran
# Exercise AI

from collections import defaultdict


class AI:
    def __init__(self):
        self.messageInFile = []

    def read_bin_file(self, name):
        with open(name, "rb") as file:
            while True:
                data = file.read()
                if not data:
                    break
                for mess in data:
                    self.messageInFile.append(mess)
        return self.messageInFile

    @staticmethod
    def encrypt(byte, amount):
        mask = 2 ** amount - 1
        lowbyte = byte & mask
        highshift = byte >> amount
        lowshift = lowbyte << (8 - amount)
        wholebyte = lowshift + highshift
        return wholebyte

    @staticmethod
    def decrypt(byte, amount):
        highshift = byte >> (8 - amount)
        lowshift = highshift << (8 - amount)
        wholebyte = byte - lowshift
        whole = wholebyte << amount
        shifted = whole + highshift
        return shifted

    @staticmethod
    def most_frequent(in_mess):
        return max(set(in_mess), key=in_mess.count)

    def driver(self, filename):
        self.messageInFile = self.read_bin_file(filename)
        most = (self.most_frequent(self.messageInFile))
        text_message = []
        for i in range(1, 8):
            characters = [' ', 'e', 't', 'o', 'a', 's', 'i', 'r', 'n', 'h']
            decrypted_char = chr(self.decrypt(most, i))
            if decrypted_char in characters:
                print(chr(most), decrypted_char, i)
                text_message.append(i)

        sentences = defaultdict(list)
        n = 0
        for j in text_message:
            for i in self.messageInFile:
                sentences[n].append(chr(self.decrypt(i, j)))
                n += 1

        for i in range(len(sentences)):
            print(*sentences[i], end="")


ai = AI()
ai.driver('Encrypted.bin')

"""
OUTPUT
   4
Stay Hungry, Stay Foolish.  I am honored to be with you today at your commencement from one of the finest universities in the world. I never graduated from college. Truth be told, this is the closest I've ever gotten to a college graduation. Today I want to tell you three stories from my life. That's it. No big deal. Just three stories... When I was young, there was an amazing publication called The Whole Earth Catalog, which was one of the bibles of my generation. It was created by a fellow named Stewart Brand not far from here in Menlo Park, and he brought it to life with his poetic touch. This was in the late 1960s, before personal computers and desktop publishing, so it was all made with typewriters, scissors, and polaroid cameras. It was sort of like Google in paperback form, 35 years before Google came along it was idealistic, and overflowing with neat tools and great notions.  Stewart and his team put out several issues of The Whole Earth Catalog, and then when it had run its course, they put out a final issue. It was the mid 1970s, and I was your age. On the back cover of their final issue was a photograph of an early morning country road, the kind you might find yourself hitchhiking on if you were so adventurous. Beneath it were the words "Stay Hungry. Stay Foolish." It was their farewell message as they signed off. Stay Hungry. Stay Foolish. And I have always wished that for myself. And now, as you graduate to begin anew, I wish that for you. Steve Jobs  
"""