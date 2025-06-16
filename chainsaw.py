import os
import sys
import subprocess
import urllib.request

def get_home():
    return os.path.join(os.path.expanduser('~'), '.chainsaw')

def get_tool_path(name):
    base = get_home()
    py = os.path.join(base, 'tools', name + '.py')
    exe = os.path.join(base, 'tools', name + '.exe')
    return py if os.path.exists(py) else exe

def ensure_tool(name):
    base = get_home()
    tool_dir = os.path.join(base, 'tools')
    if not os.path.exists(tool_dir):
        os.makedirs(tool_dir)

    py_url = f'https://raw.githubusercontent.com/fyresoftworks/chainsaw/main/tools/{name}.py'
    exe_url = f'https://raw.githubusercontent.com/fyresoftworks/chainsaw/main/tools/{name}.exe'

    py_path = os.path.join(tool_dir, name + '.py')
    exe_path = os.path.join(tool_dir, name + '.exe')

    try:
        urllib.request.urlretrieve(py_url, py_path)
        return py_path
    except:
        pass

    try:
        urllib.request.urlretrieve(exe_url, exe_path)
        return exe_path
    except:
        pass

    return None

def run_tool(name, args):
    path = get_tool_path(name)
    if not os.path.exists(path):
        print('[chainsaw] fetching tool...')
        path = ensure_tool(name)

    if not path or not os.path.exists(path):
        print('[chainsaw] tool not found')
        return

    if path.endswith('.py'):
        subprocess.run(['python', path] + args)
    else:
        subprocess.run([path] + args)

def main():
    if len(sys.argv) < 2:
        print('[chainsaw] missing command')
    elif sys.argv[1] == 'run':
        if len(sys.argv) < 3:
            print('[chainsaw] missing tool name')
        else:
            run_tool(sys.argv[2], sys.argv[3:])
    else:
        print('[chainsaw] unknown command')

    print('[chainsaw] program ended')
    input('[chainsaw] press enter to exit...')

if __name__ == '__main__':
    main()
