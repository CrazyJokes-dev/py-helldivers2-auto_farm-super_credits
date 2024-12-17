import re
from screeninfo import get_monitors

class monitorSizes:
    
    def _init_(self, monitorConfigs):
        self.monitorConfigs = monitorConfigs
    
    def setMonitorConfig(self, allMonitorsArr = []):
        for m in get_monitors():
            name = re.sub('[^0-9a-zA-Z]+','', m.name)
            width = str(m.width)
            height = str(m.height)
            curMonitor = [str(name), str(width), str(height), '|']
            allMonitorsArr.extend(curMonitor)
            self.monitorConfigs = allMonitorsArr
            
    def getMonitorConfig(self):
        return self.monitorConfigs
    
    def getChosenMonitorStats(self, monitorNum):
        """
        Returns:
            Array: [WIDTH, HEIGHT]
        """
        for i in range(0, int(len(self.monitorConfigs)/4)):
            if monitorNum != i:
                continue
            return [self.monitorConfigs[1], self.monitorConfigs[2]]