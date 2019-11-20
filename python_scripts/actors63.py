#!/usr/bin/python

import xml.sax
import psycopg2 as psycopg2



class MovieHandler(xml.sax.ContentHandler):


    def __init__(self):


        self.CurrentData = ""
        self.stagename = ""
        self.dowstart = ""
        self.dowend = ""
        self.familyname = ""
        self.firstname = ""
        self.gender = ""
        self.dob = ""
        self.roletype = ""
        self.origin = ""
        self.picref = ""
        self.relationships = ""
        self.dod = ""

    # Call when an element starts
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "actor":
            print("*****Actor*****")
            # title = attributes["title"]
            # print("Title:", title)

    # Call when an elements ends
    def endElement(self, tag):
        if self.CurrentData == "stagename":
            print("Stage name:", self.stagename)
        elif self.CurrentData == "dowstart":
            print("Start date:", self.dowstart)
        elif self.CurrentData == "dowend":
            print("End date:", self.dowend)
        elif self.CurrentData == "dod":
            print("Date of death: ", self.dod)
        elif self.CurrentData == "familyname":
            print("Family name:", self.familyname)
        elif self.CurrentData == "firstname":
            print("First name:", self.firstname)
        if self.CurrentData == "dob":
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
        elif self.CurrentData == "dod":
            self.dod = content
        elif self.CurrentData == "roletype":
            self.roletype = content
        elif self.CurrentData == "picref":
            self.picref = content


if (__name__ == "__main__"):

    # create an XMLReader
    parser = xml.sax.make_parser()
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # override the default ContextHandler
    Handler = MovieHandler()
    parser.setContentHandler(Handler)

    parser.parse("../xml_files/actors63.xml")

