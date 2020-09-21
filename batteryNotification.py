import pynotifier
import psutil

def batteryDetails():
    batteryInfo = psutil.sensors_battery()
    batteryPercentage = batteryInfo.percent
    return batteryPercentage
    
def batteryNotifier():
    pynotifier.Notification(
        title="Battery Percentage by Iris",
        description = f"Remaining Battery : {batteryDetails()}% ",
        duration=10
    ).send()
