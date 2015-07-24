#Add anything in here you want to
#run before the game window opens.
from panda3d.core import loadPrcFileData
import ClientLocalizerEnglish
windowtitle = "The Lost Tale of the Great Chemistry Project"
loadPrcFileData("", "window-title %s" % windowtitle)
loadPrcFileData("", "default-directnotify-level info")
print ":ClientPreloader: Window title set to string value '%s'" % windowtitle
print ":ClientPreloader: Game Version: %s" % ClientLocalizerEnglish.GameVersion