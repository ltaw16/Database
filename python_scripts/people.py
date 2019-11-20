#!/usr/bin/python

import xml.sax


class MovieHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.pname = ""
        self.pcodes = ""
        self.pcode = ""
        self.did = ""
        self.yearstart = ""
        self.yeardirstart = ""
        self.yearend = ""
        self.familynm = ""
        self.givennm = ""
        self.dob = ""
        self.dod = ""
        self.background = ""

    # Call when an element starts
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "person":
            print("*****Person*****")
            # title = attributes["title"]
            # print("Title:", title)
 
    # Call when an elements ends
    def endElement(self, tag):
        if self.CurrentData == "pname":
            print("Person name:", self.pname)

        elif self.CurrentData == "pcodes":
            print("Person codes:", self.pcodes)

        elif self.CurrentData == "pcode":
            print("Person code (single):", self.pcode)

        elif self.CurrentData == "did":
            print("Director id:", self.frac)

        elif self.CurrentData == "sid":
            print("Source id:", self.sid)

        elif self.CurrentData == "stitle":
            print("Source title:", self.stitle)

        elif self.CurrentData == "sy":
            print("Source year:", self.sy)

        self.CurrentData = ""

    # Call when a character is read
    def characters(self, content):
        if self.CurrentData == "rid":
            self.rid = content
        elif self.CurrentData == "rtitle":
            self.rtitle = content
        elif self.CurrentData == "ry":
            self.ry = content
        elif self.CurrentData == "frac":
            self.frac = content
        elif self.CurrentData == "sid":
            self.sid = content
        elif self.CurrentData == "stitle":
            self.stitle = content
        elif self.CurrentData == "sy":
            self.sy = content


if (__name__ == "__main__"):
    # create an XMLReader
    parser = xml.sax.make_parser()
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # override the default ContextHandler
    Handler = MovieHandler()
    parser.setContentHandler(Handler)

    parser.parse("./xml_files/remakes05.xml")