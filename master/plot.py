import pandas as pd
import matplotlib.pyplot as plt
import argparse
def motor(json):
    d = pd.read_json(str(json))
    motorTable = pd.DataFrame(d['raspberrypi']['motor'])
    xaxis = [key.split(";")[1] for key,value in motorTable.items()]
    yaxis = [value for key,value in motorTable.items()]
    plt.grid(True)
    plt.plot(xaxis,yaxis, color='maroon',marker='o')
    plt.xlabel('Datetime')
    plt.ylabel('Motor Speed')
    plt.show()
def humidity(json):
    d = pd.read_json(str(json))
    rpiTable = pd.DataFrame(d['raspberrypi']['rpi'])
    xaxis = [key.split(";")[1] for key,value in rpiTable.items()]
    yaxis = [value.get("Humidity") for key,value in rpiTable.items()]
    plt.grid(True)
    plt.plot(xaxis,yaxis, color='maroon',marker='o')
    plt.xlabel('Datetime')
    plt.ylabel('Humidity')
    plt.show()
def motion(json):
    d = pd.read_json(str(json))
    rpiTable = pd.DataFrame(d['raspberrypi']['rpi'])
    xaxis = [key.split(";")[1] for key,value in rpiTable.items()]
    yaxis = [value.get("Motion") for key,value in rpiTable.items()]
    plt.grid(True)
    plt.plot(xaxis,yaxis, color='maroon',marker='o')
    plt.xlabel('Datetime')
    plt.ylabel('Motion')
    plt.show()
def temperature(json):
    d = pd.read_json(str(json))
    rpiTable = pd.DataFrame(d['raspberrypi']['rpi'])
    xaxis = [key.split(";")[1] for key,value in rpiTable.items()]
    yaxis = [value.get("Temperature") for key,value in rpiTable.items()]
    plt.grid(True)
    plt.plot(xaxis,yaxis, color='maroon',marker='o')
    plt.xlabel('Datetime')
    plt.ylabel('Temperature')
    plt.show()
def ultrasonic(json):
    d = pd.read_json(str(json))
    rpiTable = pd.DataFrame(d['raspberrypi']['rpi'])
    xaxis = [key.split(";")[1] for key,value in rpiTable.items()]
    yaxis = [value.get("Ultrasonic") for key,value in rpiTable.items()]
    plt.grid(True)
    plt.plot(xaxis,yaxis, color='maroon',marker='o')
    plt.xlabel('Datetime')
    plt.ylabel('Ultrasonic')
    plt.show()
def plotall(json):
    d = pd.read_json(str(json))
    motorTable = pd.DataFrame(d['raspberrypi']['motor'])
    rpiTable = pd.DataFrame(d['raspberrypi']['rpi'])
    plt.subplot(1,5,1)
    plt.plot([key.split(";")[1] for key,value in motorTable.items()],[value for key,value in motorTable.items()], color='maroon',marker='o')
    plt.grid(True)
    plt.ylabel('Motor Speed')

    plt.subplot(1,5,2)
    plt.plot([key.split(";")[1] for key,value in rpiTable.items()],[value.get("Humidity") for key,value in rpiTable.items()], color='maroon',marker='o')
    plt.grid(True)
    plt.ylabel('Humidity')
    
    plt.subplot(1,5,3)
    plt.plot([key.split(";")[1] for key,value in rpiTable.items()],[value.get("Motion") for key,value in rpiTable.items()], color='maroon',marker='o')
    plt.grid(True)
    plt.ylabel('Motion')

    plt.subplot(1,5,4)
    plt.plot([key.split(";")[1] for key,value in rpiTable.items()],[value.get("Temperature") for key,value in rpiTable.items()], color='maroon',marker='o')
    plt.grid(True)
    plt.ylabel('Temperature')

    plt.subplot(1,5,5)
    plt.plot([key.split(";")[1] for key,value in rpiTable.items()],[value.get("Ultrasonic") for key,value in rpiTable.items()], color='maroon',marker='o')
    plt.grid(True)
    plt.ylabel('Ultrasonic')

    plt.show()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-pmt", "--plotmotor", nargs=1, help="Plot motor speed against time")
    parser.add_argument("-ph", "--plothumid",nargs=1,help="Plot humidity against time")
    parser.add_argument("-pm", "--plotmotion",nargs=1,help="Plot motion against time")
    parser.add_argument("-pt", "--plottemp",nargs=1,help="Plot temperature against time")
    parser.add_argument("-pu","--plotultra",nargs=1,help="Plot ultrasonic against time")
    parser.add_argument('-pall','--plotallgraphs',nargs=1,help="Combine all plotted graphs")
    args = parser.parse_args()
    if (args.plotmotor):
        args = args.plotmotor
        motor(args[0])
    if (args.plothumid):
        args = args.plothumid
        humidity(args[0])    
    if (args.plotmotion):
        args = args.plotmotion
        motion(args[0])    
    if (args.plottemp):
        args = args.plottemp
        temperature(args[0])
    if (args.plotultra):
        args = args.plotultra
        ultrasonic(args[0])
    if (args.plotallgraphs):
        args = args.plotallgraphs
        plotall(args[0])
