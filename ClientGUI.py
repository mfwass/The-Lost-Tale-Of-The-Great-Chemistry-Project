from direct.gui.DirectGui import *
from direct.gui.OnscreenText import OnscreenText
import ClientLocalizerEnglish
from panda3d.core import *

class ClientGUI():
    CL = ClientLocalizerEnglish
    finished = 0
    def __init__(self):
        pass

    def setupAssets(self):
        self.questionPanel = DirectFrame(parent = None, relief = None, image = "resources/board.png")
        self.questionPanel.setScale(10)
        self.directions = OnscreenText(parent = self.questionPanel, text = ClientLocalizerEnglish.DirectionsText)
        self.directions.setScale(0.01)
        self.directions.setZ(-0.075)
        self.mainMenu = DirectFrame(parent = None, relief = None, image = "resources/board.png")
        self.mainMenu.setScale(10)
        self.gameVersion = OnscreenText(parent = self.mainMenu, text = "Version: " + ClientLocalizerEnglish.GameVersion, scale = 0.007)
        self.gameVersion.setZ(+0.09)
        self.gameVersion.setX(-0.11)
        self.nextQuestion = OnscreenText(parent = self.questionPanel, text = ClientLocalizerEnglish.DirectionsText, scale = 0.01)
        self.nextQuestion.setColor(0,1,1,100)
        self.nextQuestion.setZ(-0.05)
        self.questionPanel.hide()
        self.directions.hide()
        self.mainMenu.hide()
        self.gameVersion.hide()
        self.nextQuestion.hide()

    def showMainMenu(self):
        if not self.mainMenu:
            # assets weren't set up, lets do that.
            self.notify.warning("Called showMainMenu without setting up assets!")
            self.setupAssets()
        self.mainMenu.show()
        self.gameVersion.show()
        mainMenu = self.mainMenu
        self.updateDirections(-0.05, ClientLocalizerEnglish.MainMenuDirections, mainMenu)
        self.initialTextInput()

    def updateDirections(self, z, text, parent):
        if self.directions:
            self.directions.hide()
            self.directions.removeNode()
        self.directions = OnscreenText(parent = parent, text = text)
        self.directions.setScale(0.01)
        self.directions.setZ(z)

    def updateQuestionText(self, category, question):
        try:
            if self.question:
                self.question.hide()
                self.question.removeNode()
        except:
            pass
        showtext = category + "\n" + question
        self.question = OnscreenText(parent = self.questionPanel, text = question)
        self.question.setScale(0.01)
        self.question.setZ(0.071)

    def showNewQuestion(self, category, question):
        # clear the text function
        def clearText():
            base.GUI.questionsText.enterText('')
        # hide Main Menu function

        def setText(text):
            base.handleNextQuestion(currentQuestion = base.questionText, currentAnswer = text)
        #add text input field
        if not self.finished == 1:
            self.questionsText = DirectEntry(text = "" ,scale=.05,command=setText,
            initialText="Username", numLines = 5,focus=1,focusInCommand=clearText)
            self.questionsText.setZ(0.3)
            self.questionsText.setX(-0.6)
            self.questionsText.setScale(0.12)
        else:
            return



    def initialTextInput(self):
        # clear the text function
        def clearText():
            base.GUI.initial.enterText('')
        # hide Main Menu function
        def hideMainMenu(text):
            base.setUsername(text)
            base.GUI.gameVersion.hide()
            base.GUI.mainMenu.hide()
            self.initial.hide()
            base.GUI.questionPanel.show()
            base.GUI.nextQuestion.show()
            base.GUI.directions.show()
            base.generateNextQuestion()

        #add text input field
        self.initial = DirectEntry(text = "" ,scale=.12,command=hideMainMenu,
        initialText="Username", numLines = 5,focus=1,focusInCommand=clearText)
        self.initial.setZ(0.3)
        self.initial.setX(-0.6)

    def handleFinished(self):
        self.finished = 1
        if not self.mainMenu:
            # assets weren't set up, lets do that.
            self.notify.warning("Called handleFinished without setting up assets!")
            self.setupAssets()
        self.mainMenu.show()
        mainMenu = self.mainMenu
        self.questionsText.hide()
        self.question.hide()
        self.question.removeNode()
        self.updateDirections(-0.05, ClientLocalizerEnglish.ThankYouText, mainMenu)

