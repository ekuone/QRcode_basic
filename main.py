import qrcode


class QRcode:

    def __init__(self, target, file_name):
        self.target = target
        self.file_name = file_name


    def QR_code_creator(self):
        image = qrcode.make(self.target)
        return image


    def QR_code_saver(self):
        product = self.QR_code_creator()
        product.save(self.file_name)

target_name = "" #link, for example: target_name = "https://www.youtube.com/"
name = "" #save as you want, for example: name = "myQRcode.png"
run = QRcode(target_name, name)
run.QR_code_saver()
# just run this prgram and everything will be fine.