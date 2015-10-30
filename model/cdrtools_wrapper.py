__author__ = 'denest'
import os
import subprocess
import sys

class Cdrtools():

    def __init__(self, path_to_bin):
        self.bin_path = os.path.abspath(path_to_bin)



    def get_devices(self):
        device_number_mask = b'Using dev='
        try:
            available_drives_output = subprocess.check_output(' '.join([os.path.join(self.bin_path,'cdrecord'),
                                                                '-checkdrive']),
                                                        shell=True,
                                                        stderr=subprocess.STDOUT)
            available_drives = [i.replace(device_number_mask,b'') for i in available_drives_output.splitlines()
                                           if i.startswith(device_number_mask)]
            return available_drives
        except subprocess.CalledProcessError as e:
            return e.output



def check_cdrtools_installed():
    pass

def make_iso():
    pass

def check_iso():
    pass

def burn_iso():
    pass

def check_dvd():
    pass


if __name__ == '__main__':
    c = Cdrtools('../external/cdrtools/bin')
    a = c.get_devices()
    print (a)