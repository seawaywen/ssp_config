import json
import os


def get_content_from_json_file(json_file):
    with open(json_file) as jf:
        content = json.load(jf)
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
        return new_content

def generate_new_json_file(parent_path, file_name, **content):
    file_path = os.path.join(parent_path, file_name)
    with open(file_path, 'w') as new_file:
        json.dump(content, new_file)
    print('saving new config file:{}'.format(file_path))


def iter_dir(path):
    analyze_flag = False
    for parent, dirnames, filenames in os.walk(path):
        for dirname in dirnames:
            print 'parent dir:' + parent

        for filename in filenames:

            #print 'parent is:' + parent
            print 'filename is ' + filename
            file_full_path = os.path.join(parent, filename)
            #print 'full name of file is ' + file_full_path

            if filename.endswith('.json'):
                new_content = get_content_from_json_file(file_full_path)
                #print new_content
                generate_new_json_file(os.path.dirname(parent), filename, **new_content)

                analyze_flag = True
    return analyze_flag


if __name__ == '__main__':
    base_dir = os.path.abspath(os.path.dirname(__file__))
    config_dir = os.path.join(base_dir, 'configs')
    print config_dir
    if not os.path.exists(config_dir):
        raise ValueError('you must have a configs folder to contain all the '
                         'config json files')
    if not iter_dir(config_dir):
        print('you don NOT have any json config file')
