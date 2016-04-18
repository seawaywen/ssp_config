import json
import os


def get_content_from_json_file(json_file):
    with open(json_file) as jf:
        content = json.load(jf)
        print content
        local_port = content['local_port']
        server_password_section = content['server_password'][0]
        server_with_port, password, method = server_password_section
        server, port = server_with_port.split(':')

        new_content = {
            "local_port": local_port,
            "server": server,
            "server_port": port,
            "password": password,
            "method": method
        }
        #print server, port, password, method,
        return new_content

def generate_new_json_file(parent_path, file_name, **content):
    file_path = os.path.join(parent_path, file_name)
    print file_path
    with open(file_path, 'w') as new_file:
        json.dump(content, new_file)


def iter_dir(path):
    for parent, dirnames, filenames in os.walk(path):
        for dirname in dirnames:
            print 'parent dir:' + parent
            #print 'dirname is ' + dirname

        for filename in filenames:
            #print 'parent is:' + parent
            print 'filename is ' + filename
            file_full_path = os.path.join(parent, filename)
            print 'full name of file is ' + file_full_path

            new_content = get_content_from_json_file(file_full_path)
            print new_content
            generate_new_json_file(os.path.dirname(parent), filename, **new_content)

if __name__ == '__main__':
    iter_dir('/home/kelvin/DevTools/ss/configs')
