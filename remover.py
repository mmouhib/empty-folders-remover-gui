import os


def MainFn(dir_tree):
    for folder in dir_tree:
        # 'System Volume Information' is a folder created by windows and cant be deleted
        if folder == 'System Volume Information':
            continue
        if os.path.isdir(folder):
            if len(os.listdir(folder)) == 0:
                os.rmdir(folder)


def remove(path_url):
    os.chdir(path_url)
    dir_tree = os.listdir(os.getcwd())
    MainFn(dir_tree)

