from direct.gui.DirectGui import *
from direct.gui.OnscreenText import OnscreenText
from panda3d.core import *
import ClientLocalizerEnglish

class ClientGUI():
    CL = ClientLocalizerEnglish
    finished = 0
    question = 0
    def __init__(self):
        # This sets up the 'assets' for the GUI of the program
        # It will declare all main GUI variables and prepare them for usage
        self.questionPanel = DirectFrame(parent = None,
                                         relief = None,
                                         image = "resources/board.png")
        self.questionPanel.setScale(10)
        self.directions = OnscreenText(parent = self.questionPanel,
                                       text = ClientLocalizerEnglish.DirectionsText)
        self.directions.setScale(0.01)
        self.directions.setZ(-0.075)
        self.mainMenu = DirectFrame(parent = None,
                                    relief = None,
                                    image = "resources/board.png")
        self.mainMenu.setScale(10)
        self.gameVersion = OnscreenText(parent = self.mainMenu,
                                        text = "Version: " + ClientLocalizerEnglish.GameVersion,
                                        scale = 0.007)
        self.gameVersion.setZ(+0.09)
        self.gameVersion.setX(-0.11)
        self.nextQuestion = OnscreenText(parent = self.questionPanel,
                                         text = ClientLocalizerEnglish.DirectionsText,
                                         scale = 0.01)
        self.nextQuestion.setColor(0,1,1,100)
        self.nextQuestion.setZ(-0.05)
        self.questionPanel.hide()
        self.directions.hide()
        self.mainMenu.hide()
        self.gameVersion.hide()
        self.nextQuestion.hide()

    def showMainMenu(self):
        # Shows main menu
        if not self.mainMenu:
            # assets weren't set up, lets do that.
            self.notify.warning("Called showMainMenu without setting up assets!")
            self.setupAssets()
        self.mainMenu.show()
        self.gameVersion.show()
        self.updateDirections(-0.05, ClientLocalizerEnglish.MainMenuDirections, self.mainMenu)
        self.initialTextInput()

    def updateDirections(self, z, text, parent):
        # Call this to update the directions.
        if self.directions:
            self.directions.hide()
            self.directions.removeNode()
        self.directions = OnscreenText(parent = parent,
                                       text = text)
        self.directions.setScale(0.01)
        self.directions.setZ(z)

    def updateQuestionText(self, category, question):
        if self.question:
            self.question.hide()
            self.question.removeNode()
        showtext = category + "\n" + question
        self.question = OnscreenText(parent = self.questionPanel,
                                     text = question)
        self.question.setScale(0.01)
        self.question.setZ(0.071)

    def showNewQuestion(self, category, question):
        def clearText():
            # Clear the text function
            base.GUI.questionsText.enterText('')
        def setText(text):
            # Hide Main Menu function
            base.handleNextQuestion(currentQuestion = base.questionText,
                                    currentAnswer = text)
        # Add text input field
        if not self.finished == 1:
            self.questionsText = DirectEntry(text = "" ,
                                             scale=.05,
                                             command=setText,
                                             initialText="Username",
                                             numLines = 5,
                                             focus=1,
                                             focusInCommand=clearText)
            self.questionsText.setZ(0.3)
            self.questionsText.setX(-0.6)
            self.questionsText.setScale(0.12)
        else:
            return

    def initialTextInput(self):
        def clearText():
            # Clear the text function
            base.GUI.initial.enterText('')
        
        def hideMainMenu(text):
            # Hide Main Menu function
            base.setUsername(text)
            base.GUI.gameVersion.hide()
            base.GUI.mainMenu.hide()
            self.initial.hide()
            base.GUI.questionPanel.show()
            base.GUI.nextQuestion.show()
            base.GUI.directions.show()
            base.generateNextQuestion()

        # Add text input field
        self.initial = DirectEntry(text = "" ,
                                   scale=.12,
                                   command=hideMainMenu,
                                   initialText="Username",
                                   numLines = 5,
                                   focus=1,
                                   focusInCommand=clearText)
        self.initial.setZ(0.3)
        self.initial.setX(-0.6)

    def handleFinished(self):
        self.finished = 1
        if not self.mainMenu:
            # Assets weren't set up, lets do that
            self.notify.warning("Called handleFinished without setting up assets!")
            self.setupAssets()
        self.mainMenu.show()
        self.questionsText.hide()
        self.question.hide()
        self.question.removeNode()
        self.updateDirections(-0.05, ClientLocalizerEnglish.ThankYouText, self.mainMenu)

