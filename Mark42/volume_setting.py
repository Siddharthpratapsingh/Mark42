import alsaaudio
import sys
 
a = alsaaudio.Mixer()
vol = a.getvolume()

def getVolume():
    global vol
    return vol[0]
    
def increase(n):
    global vol
    if (vol[0] + n)>100:
        vol[0] = 100 - n
    m.setvolume(vol[0] + n)
    vol = m.getvolume()
    print "Volume increased to" + str(vol[0]) + "percent"
    
def decrease(n):
    global vol
    if (vol[0] - n)>100
        vol[0] = 100 + n
    m.setvolume(vol[0] - n)
    vol = m.getvolume()
    print "Volume decreased to" + str(vol[0]) + "percent"
    
def setVolume(n):
    global vol
    m.setvolume(n)
    vol = m.getvolume()
    print "Volume set to " + str(vol[0]) + "percent"
    
 
       
