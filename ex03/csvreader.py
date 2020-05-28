class CsvReader():
    def parsing(self):
        try:
            f = open(self.filename, "r")
        except:
            print("Error, Bad File")
            exit(1)
        lines = f.readlines()
        if len(lines) is 0:
            print("Error, empty file")
            exit(1)
        if self.skip_top >= len(lines) or\
            self.skip_bottom >= len(lines)\
                or self.skip_bottom + self.skip_top >= len(lines):
            print("Error, too many lines to skip")
            exit(1)
        nb_info = 0
        if self.header is True:
            lines[0] = lines[0].rstrip()
            setattr(self, "str_header", lines[0])
            lines.remove(lines[0])
        else:
            setattr(self, "str_header", None)
            lines.remove(lines[0])
        del lines[0:self.skip_top]
        if self.skip_bottom is not 0:
            del lines[self.skip_bottom:len(lines)]
        tmp = []
        for l in lines:
            l = l.rstrip()
            l = l.split(self.sep)
            tmp.append(l)
        setattr(self, "lst_data", tmp)

    def getdata(self):
        ret = []
        string = ""
        for line in self.lst_data:
            string = line[0] + " " + line[1] + " " + line[2]
            ret.append(string)
        return ret

    def getheader(self):
        return self.str_header

    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom

    def __enter__(self):
        if self.filename is None:
            print("Error, no filename")
            exit(1)
        if len(self.sep) is not 1:
            print("Error, too many sep, just one please")
            exit(1)
        if self.skip_top < 0:
            print("Error, not negative skip_top")
            exit(1)
        if self.skip_bottom < 0:
            print("Error, not negative skip_bottom")
            exit(1)
        self.parsing()
        return self

    def __exit__(filename, header, skip_top, skip_bottom):
        pass


if __name__ == "__main__":
    with CsvReader("data.csv", ',', False) as file:
        data = file.getdata()
        header = file.getheader()
        print("Header: ", header)
        for elem in data:
            print(elem)
