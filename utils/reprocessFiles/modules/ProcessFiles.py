import os
import shutil
import tempfile
import json
import requests


class ProcessFiles:
    def __init__(self, src, url):
        self.srcFolder = src
        self.url = url
    
    def processFiles(self):
        # Create a temporary folder
        # with tempfile.TemporaryDirectory() as tmpdirname:
        if True:
            tmpdir = tempfile.TemporaryDirectory()
            print('created temporary directory', tmpdir.name)

            # Copy files into temporary folder
            files = os.listdir(self.srcFolder)
            for fname in files:
                # copying the files to the 
                # destination directory
                shutil.copy2(os.path.join(self.srcFolder,fname), tmpdir.name)

            # Process each file in temporary folder
            files = os.listdir(tmpdir.name)
            for tmpfname in files:
                print("tmpdir.name: ", tmpdir.name)
                print("tmpfname: ", tmpfname)
                fulltmpfname = os.path.join(tmpdir.name, tmpfname)
                print("fulltmpfname: ", fulltmpfname)
                # Load JSON file
                with open(fulltmpfname) as jsonFile:
                    jsonObject = json.load(jsonFile)
                    jsonFile.close()
                print("json: {}".format(jsonObject))
                
                try:
                    # Send file to URL with the body set to the json contents
                    r = requests.post(self.url, json=jsonObject)

                    # If upload is successful
                    print("[{}] {} {}".format(r.status_code, self.url, fulltmpfname))
                    if r.status_code >= 200 and r.status_code <= 299:
                        # remove file
                        os.remove(fulltmpfname)
                        print("Removed: {}".format( fulltmpfname ))
                except Exception as err:
                    print("Exception:{}".format(err))

                    

