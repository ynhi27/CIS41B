from collections import defaultdict
binlist = []
# read
class ai:
    def __init__(self, filename):
        self.filename = filename
    def readbin(name):
        with open(name, "rb") as f:
            while True:
                # using f.read(6) to check with online converter
                data = f.read(6)
                if not data:
                    break
                for by in data:
                    # print(f"{by:08b}")
                    binlist.append(by)
        return binlist


    def Encrypt(byte, amount):
        mask = 2**amount - 1
        lowbyte = byte & mask
        highshift = byte >> amount
        lowshift = lowbyte << (8-amount)
        wholebyte = lowshift + highshift
        return wholebyte


    def decrypt(byte, amount):
        highshift = byte >> 8-amount
        highshifts = highshift << 8-amount
        wholebyte = byte - highshifts
        wholebytes = wholebyte << amount
        shifted = wholebytes + highshift
        return shifted


    def most_frequent(List):
        return max(set(List), key=List.count)

    def runai(self):
        lis = ai.readbin(self.filename)
        mostc = (ai.most_frequent(lis))
        posrot = []
        for i in range(1, 8):
            # most common letters from frequency; vowels and like t, s, h based on frequency.txt
            if (chr(ai.decrypt(mostc, i)) == ' '):
                print(chr(mostc), chr(ai.decrypt(mostc, i)), i)
                posrot.append(i)
            elif (chr(ai.decrypt(mostc, i)) == 'a'):
                print(chr(mostc), chr(ai.decrypt(mostc, i)), i)
                posrot.append(i)
            elif (chr(ai.decrypt(mostc, i)) == 'e'):
                print(chr(mostc), chr(ai.decrypt(mostc, i)), i)
                posrot.append(i)
            elif (chr(ai.decrypt(mostc, i)) == 'i'):
                print(chr(mostc), chr(ai.decrypt(mostc, i)), i)
                posrot.append(i)
            elif (chr(ai.decrypt(mostc, i)) == 'o'):
                print(chr(mostc), chr(ai.decrypt(mostc, i)), i)
                posrot.append(i)
            elif (chr(ai.decrypt(mostc, i)) == 'u'):
                print(chr(mostc), chr(ai.decrypt(mostc, i)), i)
                posrot.append(i)
            elif (chr(ai.decrypt(mostc, i)) == 't'):
                print(chr(mostc), chr(ai.decrypt(mostc, i)), i)
                posrot.append(i)
            elif (chr(ai.decrypt(mostc, i)) == 's'):
                print(chr(mostc), chr(ai.decrypt(mostc, i)), i)
                posrot.append(i)
            elif (chr(ai.decrypt(mostc, i)) == 'h'):
                print(chr(mostc), chr(ai.decrypt(mostc, i)), i)
                posrot.append(i)


        print(posrot)
        # this is where we print
        msg = defaultdict(list)
        num = 0
        for j in posrot:
            for i in lis:
                msg[num].append(chr(ai.decrypt(i, j)))
            num = num + 1


        for i in range(len(msg)):
            print("Possible message (id:{x}):".format(x=i))
            print(*msg[i], sep='')
            print()

a = ai('Encrypted.bin')
a.runai()