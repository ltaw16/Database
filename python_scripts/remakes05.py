#!/usr/bin/python

import xml.sax


class MovieHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.rid = ""
        self.rtitle = ""
        self.ry = ""
        self.frac = ""
        self.sid = ""
        self.stitle = ""
        self.sy = ""

    # Call when an element starts
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "remake":
            print("*****Remake*****")
            # title = attributes["title"]
            # print("Title:", title)

    # Call when an elements ends
    def endElement(self, tag):
        if self.CurrentData == "rid":
            print("Remake id:", self.rid)
        elif self.CurrentData == "rtitle":
            print("Remake Title:", self.rtitle)
        elif self.CurrentData == "ry":
            print("Remake year:", self.ry)

        elif self.CurrentData == "frac":
            print("Fraction:", self.frac)

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

    parser.parse("../xml_files/remakes05.xml")