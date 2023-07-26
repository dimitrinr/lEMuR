import rumps
import subprocess

class AwesomeStatusBarApp(rumps.App):
    def __init__(self):
        super(AwesomeStatusBarApp, self).__init__("Awesome App")
        self.menu = ["ABOUT", "POTATO", "EXIT"]

    @rumps.clicked("ABOUT")
    def about(self, _):
        rumps.alert('Hello, world!')

    @rumps.clicked("POTATO")
    def potato(self, _):
        subprocess.run(["echo", "hihi"], shell=True)

    @rumps.clicked("EXIT")
    def exit(self, _):
        rumps.quit_application()

app = AwesomeStatusBarApp()
app.run()
This script creates an application that resides in the macOS status bar with the name "Awesome App" and has three menu items "ABOUT", "POTATO", and "EXIT". When "ABOUT"



