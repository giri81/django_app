'''
Created on 13-Dec-2015

@author: girish
'''
import subprocess
import shutil
from myproject   import settings
import os
import shutil

class Run:
    def compile(self, filepath, filename):
        absPath = os.path.join(settings.MEDIA_ROOT,filepath)
        proc = subprocess.Popen(["gcc",absPath, "-o", absPath[:-1]+"o" ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
        stdout, stderr = proc.communicate()
        p_status = proc.wait()
        return stdout, stderr, p_status
     
            
    def execute(self, filepath, filename):
        absPath = os.path.join(settings.MEDIA_ROOT, filepath)
        os.chdir(os.path.dirname(absPath))
        proc = subprocess.Popen(["./"+filename[:-1]+"o"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
        stdout, stderr = proc.communicate()
        p_status = proc.wait()
        return stdout, stderr, p_status

    def ifobjExists(self, filepath):
        objpath = filepath[:-1]+'o'
        absPath = os.path.join(settings.MEDIA_ROOT,objpath)
        print absPath
        return os.path.isfile(absPath)

    def flushObj(self, filepath, filename):
        absPath = os.path.join(settings.MEDIA_ROOT, filepath)
        absPath = absPath[:-1]+'o'
        os.chdir(os.path.dirname(absPath))
        if self.ifobjExists(absPath):
            os.remove(os.path.basename(absPath))