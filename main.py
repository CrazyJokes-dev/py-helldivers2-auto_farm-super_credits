import cv2
import numpy as np
import find_monitor_sizes

object = find_monitor_sizes.monitorSizes()
object.setMonitorConfig([])

screenStatsArr = object.getChosenMonitorStats(1)
screenWidth = screenStatsArr[0]
screenHeight = screenStatsArr[1]




