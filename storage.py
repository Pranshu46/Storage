import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_files(self,file_from,file_to):

        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.AuI-ShIcvZ1B_SiIKe36jg84k_llL8c3E0DHb5eRUS1CwYzsOOhYYkKrUj_Epw5Fi-QIaxl3eiEJoFp-j4FLzpANy9JNxQGdmoujNE9UoB85zDvQ7j69wbrBhihDeT_UHjhzulc'
    transferData = TransferData(access_token)

    file_from = input("enter your file path:-")
    file_to = input("enter the full path to enter the dropbox:-")
    transferData.upload_files(file_from, file_to)
    print("file has been moved ")

if __name__ == '__main__':
    main()