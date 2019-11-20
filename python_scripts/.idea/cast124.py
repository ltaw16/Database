#!/usr/bin/python

import xml.sax


class MovieHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.dirfilms = ""
        self.dirId = ""
        self.standardizedName = ""
        self.castNote = ""
        self.filmc = ""
        self.m = ""
        self.filmIdentifier = ""
        self.filmTitle = ""
        self.actorName = ""
        self.roleType = ""
        self.roleDescription = ""
        self.n = ""
        self.awards = ""
        self.award = ""

    # Call when an element starts
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "casts":
            print("*****Cast*****")
            # title = attributes["title"]
            # print("Title:", title)

    # Call when an elements ends
    def endElement(self, tag):
        if self.CurrentData == "dirfilms":
            print("Director's films:", self.pname)

        elif self.CurrentData == "dirId":
            print("Director id:", self.dirId)

        elif self.CurrentData == "standardizedName":
            print("Standardized Name:", self.standardizedName)

        elif self.CurrentData == "castNote":
            print("Cast Note:", self.castNote)

        elif self.CurrentData == "filmc":
            print("Filmc:", self.filmc)

        elif self.CurrentData == "m":
            print("m:", self.m)

        elif self.CurrentData == "filmIdentifier":
            print("Film Identifier:", self.filmIdentifier)

        elif self.CurrentData == "filmTitle":
            print("Film Title:", self.filmTitle)

        elif self.CurrentData == "actorName":
            print("Actor Name:", self.actorName)

        elif self.CurrentData == "roleType":
            print("Role Type:", self.roleType)

        elif self.CurrentData == "roleDescription":
            print("Role Description:", self.roleDescription)

        elif self.CurrentData == "n":
            print("n:", self.n)

        elif self.CurrentData == "awards":
            print("Awards:", self.awards)

        elif self.CurrentData == "award":
            print("Award:", self.award)

        self.CurrentData = ""

    # Call when a character is read
    def characters(self, content):
        if self.CurrentData == "dirfilms":
            self.dirfilms = content
        elif self.CurrentData == "dirId":
            self.dirId = content
        elif self.CurrentData == "standardizedName":
            self.standardizedName = content
        elif self.CurrentData == "castNote":
            self.castNote = content
        elif self.CurrentData == "filmc":
            self.filmc = content
        elif self.CurrentData == "m":
            self.m = content
        elif self.CurrentData == "filmIdentifier":
            self.filmIdentifier = content
        elif self.CurrentData == "filmTitle":
            self.filmTitle = content
        elif self.CurrentData == "actorName":
            self.actorName = content
        elif self.CurrentData == "roleType":
            self.roleType = content
        elif self.CurrentData == "roleDescription":
            self.roleDescription = content
        elif self.CurrentData == "n":
            self.n = content
        elif self.CurrentData == "awards":
            self.awards = content
        elif self.CurrentData == "award":
            self.award = content

if (__name__ == "__main__"):
    # create an XMLReader
    parser = xml.sax.make_parser()
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # override the default ContextHandler
    Handler = MovieHandler()
    parser.setContentHandler(Handler)

    parser.parse("./xml_files/remakes05.xml")