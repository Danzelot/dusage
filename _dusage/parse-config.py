import configparser

def replace_variables(path, project=None, user=None, filesystem=None):
    if project:
        path = path.replace('{project}', project)
    if user:
        path = path.replace('{user}', user)
    if filesystem:
        path = path.replace('{filesystem}', filesystem)
    return path

config = configparser.ConfigParser()
config.read('config.ini')

# Accessing global configuration
filesystem = config.get('Global', 'filesystem')

# Accessing folder configuration values
folders = config.items('QuotaFolders')

project_name = "my_project"
user_name = "john_doe"

for folder, should_backup in folders:
    folder_path = replace_variables(folder, project=project_name, user=user_name, filesystem=filesystem)
    should_backup = config.getboolean('QuotaFolders', folder)
    print(f"Folder: {folder_path}, Backup: {should_backup}, Filesystem: {filesystem}")
