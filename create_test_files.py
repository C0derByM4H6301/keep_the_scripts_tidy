import os
import random
import string

def create_random_file(ext, dir):
    """
    Belirtilen uzantıda bir rastgele dosya oluşturur.
    """
    filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10)) + '.' + ext
    with open(os.path.join(dir, filename), 'w') as f:
        f.write("Bu dosya {} uzantılıdır.".format(ext))

def create_test_files(exts, dir):
    """
    Belirtilen dizinde belirtilen uzantılarda rastgele dosyalar oluşturur.
    """
    if not os.path.exists(dir):
        os.makedirs(dir)
    for ext in exts:
        ext_dir = os.path.join(dir, ext.upper())
        if not os.path.exists(ext_dir):
            os.makedirs(ext_dir)
        try:
            create_random_file(ext, ext_dir)
        except Exception as e:
            print("Hata oluştu: ", e)

if __name__ == '__main__':
    exts = ['py', 'java', 'cpp', 'c', 'html', 'css', 'js', 'php']
    target_dir = 'test_files'
    create_test_files(exts, target_dir)
    with open(os.path.join(target_dir, 'main.py'), 'w') as f:
        f.write("Bu ana dosyadır.")
    print("Test dosyaları oluşturuldu.")
