from direct.showbase.ShowBase import ShowBase
from direct.directnotify import DirectNotifyGlobal
from ClientGUI import ClientGUI
import ClientLocalizerEnglish
import random
import sys
import os

class ClientBase(ShowBase):
    notify = DirectNotifyGlobal.directNotify.newCategory("ClientBase")
    def __init__(self):
        ShowBase.__init__(self, windowType=None)
        print("ClientBase: Window successfully created! Creating GUI...")
        self.CL = ClientLocalizerEnglish
        self.category = 0
        self.GUI = ClientGUI()
        self.GUI.__init__()
        self.GUI.showMainMenu()

    def handleNextQuestion(self, currentQuestion = None, currentAnswer = None):
        # Alrighty, client is ready for the next question... lets log their current questions data.

        if base.GUI.finished == 1:
            self.notify.warning("Client tried to obtain a question after already finishing its current set!")

        # have an answer? good... lets log it.
        self.logAnswer(currentQuestion, currentAnswer)
        # Checking to see if the client responded with an answer.
        if currentQuestion is not None and currentAnswer is None:
            # really? no answer? thanks for nothing... om nom nom, oh wait a second.... Nothing to om nom nom on!
            self.notify.warning("Client did not provide an answer for question %s." % currentQuestion)
        self.generateNextQuestion()

    def generateNextQuestion(self):
        # Choose a random category by choosing a random number which defines a category
        if self.category == 11:
            # client finished
            self.GUI.handleFinished()
        else:
            self.category = self.category + 1
        question = random.randint(1,14)
        # lets grab the question data...
        # find category
        self.categoryText = self.CL.POSSIBLECATEGORIES[self.category]
        if self.categoryText == "CHFOUND":
            # category text is CHFOUND, lets get a question from that category...
            self.questionText = self.CL.CHFOUND[question]
        elif self.categoryText == "ACIDSANDBASE":
            # category text is ACIDSANDBASE, lets get a question from that category...
            self.questionText = self.CL.ACIDSANDBASE[question]
        elif self.categoryText == "MATTERANDATOMS":
            # category text is MATTERANDATOMS, lets get a question from that category...
            self.questionText = self.CL.MATTERANDATOMS[question]
        elif self.categoryText == "CONCENTRATIONSANDSOLUTIONS":
            # category text is CONCENTRATIONSANDSOLUTIONS, lets get a question from that category...
            self.questionText = self.CL.CONCENTRATIONSANDSOLUTIONS[question]
        elif self.categoryText == "NUCLEARCHEMISTRY":
            # category text is NUCLEARCHEMISTRY, lets get a question from that category...
            self.questionText = self.CL.NUCLEARCHEMISTRY[question]
        elif self.categoryText == "GASSES":
            # category text is GASSES, lets get a question from that category...
            self.questionText = self.CL.GASSES[question]
        elif self.categoryText == "PERIODICTABLE":
            # category text is PERIODICTABLE, lets get a question from that category...
            self.questionText = self.CL.PERIODICTABLE[question]
        elif self.categoryText == "STOICHIOMETRY":
            # category text is STOICHIOMETRY, lets get a question from that category...
            self.questionText = self.CL.STOICHIOMETRY[question]
        elif self.categoryText == "COMPOUNDSANDMOLECULES":
            # category text is COMPOUNDSANDMOLECULES, lets get a question from that category...
            self.questionText = self.CL.COMPOUNDSANDMOLECULES[question]
        elif self.categoryText == "TYPESOFREACTIONS":
            # category text is TYPESOFREACTIONS, lets get a question from that category...
            self.questionText = self.CL.TYPESOFREACTIONS[question]
        elif self.categoryText == "BALANCINGEQUATIONS":
            # category text is BALANCINGEQUATIONS, lets get a question from that category...
            self.questionText = self.CL.BALANCINGEQUATIONS[question]
        else:
            # client finished test
            self.notify.info("Client finished test!")

        self.GUI.updateQuestionText(self.categoryText, self.questionText)
        self.GUI.showNewQuestion(self.categoryText, self.questionText)

    def logAnswer(self, question = None, answer = None):
        # checking to see if database exists
        if not os.path.exists('database/'):
            # rip, no db. let's make one.
            self.notify.warning("No database found! Made new directory to save client data.")
            os.mkdir('database/') 
        # Client answers DB filename
        filename = "%s_answers.txt" % self.getUsername()
        # Checking to see if the database file is already there.
        if not os.path.isfile('database/' + filename):
            self.notify.info("Database file %s already exists! Creating marker for the additional call.") # not really doing this atm, future update. Leaving the code there though.
            # Open the file
            f = open("database/"+filename, 'a')
            # Write DBID(Database ID) Marker
            f.write("##############################\n Database file for Client %s...\n##############################\n" % self.getUsername())
        # Open the file
        f = open("database/"+filename, 'w')
        # Write the question
        f.write("Question: %s \n" % question)
        # Write the answer provided
        f.write("Given Answer: %s \n\n" % answer)
        # Close the file
        f.close()

    def getUsername(self):
        # Returns value predeclared in self.setUsername
        return self.username

    def setUsername(self, username = None):
        # Set global variable for username
        self.username = username
        # Checking to see if user provided a username
        if username is None:
            # oof, no username provided... oh well, the idiot who failed to provide a username
            # *might* loose some info by being overwritten during parsing
            self.noify.warning("Client set their username as None. Loss of data possible...")
