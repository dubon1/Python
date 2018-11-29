#!/usr/bin/python3

class ReadFirstLine:

    def read_first_line(path):
        file = None
        first_line = None
        try:
            file = open(path)
            first_line = file.readline()
        except IOError as e:
            print('Error reading from "' + path + '". Message = "' + e.message + '"')
        finally:
            if file is not None:
                try:
                    file.close()
                except:
                    pass
        return first_line

#x=ReadFirstLine()
#x.read_first_line('/tmp/xxx')
ReadFirstLine.read_first_line('/tmp/xyx')
