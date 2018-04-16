# -*- coding: utf-8 -*-
class Callback(object):

    def __init__(self, callback):
        self.callback = callback

    def PinVerified(self, pin):
        self.callback("Input this PIN code '" + pin + "' on your LINE for smartphone in 2 minutes")

    def QrUrl(self, url, showQr=True, pointer=None, logNum=None):
        if showQr:
            notice='or scan this QR '
        else:
            notice=''
        if logNum == 0:
            noticeMsg = "Tyfe's super admin login URL"
        elif logNum == 1:
            noticeMsg = "Tyfe's login URL"
        elif logNum >= 2:
            noticeMsg = "Tyfe helper's login URL"
        if pointer == 0:
            status = "[1/2]"
        elif pointer == 1:
            status = "[2/2]"
        self.callback(noticeMsg+" "+status+": "+url+"\n")
        if showQr:
            try:
                import pyqrcode
                url = pyqrcode.create(url)
                self.callback(url.terminal('green', 'white', 1))
            except:
                pass

    def default(self, str):
        self.callback(str)
