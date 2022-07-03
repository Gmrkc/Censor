from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

class DriveDemo:

    # 1RWd7Jhl5t1qRoWZv7S0wm25Dzbv9h5XO -> directory id of edited files
    # 1HqUkoNS2zyNIM-hREUZYuFtvBJK7nmIA -> directory id of raw files

    def __init__(self):
        self.gauth = GoogleAuth()
        self.gauth.LocalWebserverAuth()
        self.drive = GoogleDrive(self.gauth)
        
    def upload_file(self, file_name, directory_id):
        """ adi verilen dosyayi id'si verilen klasöre upload eder """
        gfile = self.drive.CreateFile({'parents': [{'id': directory_id}]})
        gfile.SetContentFile(file_name)
        gfile.Upload()

    def get_file_list(self, directory_id) -> list:
        """ id'si verilen klasördeki dosyalarin listesini döndürür """
        file_list = self.drive.ListFile({'q': "'{}' in parents and trashed=false".format(directory_id)}).GetList()
        return file_list
    
    def get_only_title(self, file_list):
        new_list = []

        for i in file_list:
            #print(i['originalFilename'])
            #print(type(i['originalFilename']))
            new_list.append(i['originalFilename'])

        return new_list
        
    def print_file_list(self, file_list):
        """ dosya listesini yazdirir """
        for file in file_list:
            print('title: %s, id: %s' % (file['title'], file['id']))

    def get_difference_lists(self, list1, list2) -> list:
        """ list2 de olmayan list1 elemanlarini döndürür """
        list_difference = [item for item in list1 if item not in list2]
        return list_difference

    def download_files(self, directory_id, diff_list):
        """
        #id'si verilen klasördeki dosyalarin tümünü indirir
        file_list = self.get_file_list(directory_id)
        for i, file in enumerate(sorted(file_list, key = lambda x: x['title']), start=1):
            print('Downloading {} file from GDrive ({}/{})'.format(file['title'], i, len(file_list)))
            file.GetContentFile(file['title'])

        """
        difference_list = diff_list
        file_list = self.get_file_list(directory_id)

        
        for item in file_list:
            if item['originalFilename'] in difference_list:
                #print('Downloading {} file from GDrive ({}/{})'.format(item['title'], len(file_list)))
                item.GetContentFile(item['originalFilename'])

        """
        for i, file in enumerate(sorted(file_list, key = lambda x: x['title']), start=1):
            print('Downloading {} file from GDrive ({}/{})'.format(file['title'], i, len(file_list)))
            file.GetContentFile(file['title'])

        """