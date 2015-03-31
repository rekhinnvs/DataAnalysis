__author__ = 'rekhin'
import os
import time

def main():


    counter = 0
    while counter<1:
        print('Executing Master clear')
        #os.system('adb -s d23fca72 wait-for-device shell am broadcast -a android.intent.action.MASTER_CLEAR')
        os.system('adb -s d23fca72 wait-for-device reboot')
        print('Done resetting!')
        os.system('adb -s d23fca72 wait-for-device root')
        time.sleep(1)
        os.system('adb -s d23fca72 wait-for-device remount');
        #os.system('adb -s d23fca72 wait-for-device')
        print('Starting of logs')
        #os.system('adb -s d23fca72 wait-for-device logcat -b main -b radio -b system -b events -v time >> factory_reset_logact_'+str(counter)+ '&')
        #print('Sleeping for 8 minutes for the devie to bootup')
        #time.sleep(480)
        counter+=1;
    else:
        print('Done with resetting! End of counter')
if __name__ == '__main__':
    main()
