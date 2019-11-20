#!/usr/bin/python

import xml.sax


class MovieHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.fid = ""
        # self.dowstart = ""
        # self.dowend = ""
        # self.familyname = ""
        # self.firstname = ""
        # self.gender = ""
        # self.dob = ""
        # self.roletype = ""
        # self.origin = ""
        # self.picref = ""
        # self.relationships = ""

    # Call when an element starts
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "film":
            print("*****Film*****")
            # title = attributes["title"]
            # print("Title:", title)

    # Call when an elements ends
    def endElement(self, tag):
        if self.CurrentData == "fid":
            print("Film id:", self.fid)
        elif self.CurrentData == "t":
            print("Title:", self.t)
        elif self.CurrentData == "year":
            print("Year:", self.year)

        elif self.CurrentData == "familyname":
            print("Family name:", self.familyname)

        elif self.CurrentData == "firstname":
            print("First name:", self.firstname)

        elif self.CurrentData == "gender":
            print("Gender:", self.gender)

        elif self.CurrentData == "dob":
            print("Date of birth:", self.dob)

        self.CurrentData = ""

    # Call when a character is read
    def characters(self, content):
        if self.CurrentData == "stagename":
            self.stagename = content
        elif self.CurrentData == "dowstart":
            self.dowstart = content
        elif self.CurrentData == "dowend":
            self.dowend = content
        elif self.CurrentData == "familyname":
            self.familyname = content
        elif self.CurrentData == "firstname":
            self.firstname = content
        elif self.CurrentData == "gender":
            self.gender = content
        elif self.CurrentData == "dob":
            self.dob = content


if (__name__ == "__main__"):
    # create an XMLReader
    parser = xml.sax.make_parser()
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # override the default ContextHandler
    Handler = MovieHandler()
    parser.setContentHandler(Handler)

    parser.parse("../xml_files/actors63.xml")