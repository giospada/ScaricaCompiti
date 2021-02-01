from rich.console import Console
import datetime as dt

class TUI:

    def __init__(self):
        self.console=Console()
        self.today=dt.datetime.now().date()

    def initUpdate(self):
        self.spinner=self.console.status("Download Compiti")
        self.spinner.start()
    
    def finishUpdate(self):
        self.spinner.stop()

    def printCompiti(self,obj):
        lastd=""
        for i in obj:
            if not (lastd==i["datCompiti"]):
                lastd=i["datCompiti"]
                istoday=(dt.date.fromisoformat(lastd)-self.today).days==1
                color="red" if istoday else "blue"
                self.console.print("["+color+" bold]"+i["datCompiti"]+"[/"+color+" bold]",justify="center")

            self.console.print("[blue bold]---"+i["desMateria"]+"[/blue bold]")
            self.console.print(i["desCompiti"])
            self.console.print("\n")

