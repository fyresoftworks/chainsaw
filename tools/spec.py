import platform
import psutil
import os
import sys
import subprocess

def get_cpu_info():
    try:
        return platform.processor() or "unknown cpu"
    except:
        return "unknown cpu"

def get_ram_info():
    try:
        mem = psutil.virtual_memory()
        return f"{round(mem.total / (1024 ** 3), 2)} GB"
    except:
        return "unknown ram"

def get_disk_info():
    try:
        disk = psutil.disk_usage(os.path.expanduser("~"))
        return f"{round(disk.total / (1024 ** 3), 2)} GB total, {round(disk.free / (1024 ** 3), 2)} GB free"
    except:
        return "unknown disk"

def get_os_info():
    try:
        return f"{platform.system()} {platform.release()}"
    except:
        return "unknown os"

def get_gpu_info():
    try:
        if sys.platform == "win32":
            # use wmic to query GPU name
            output = subprocess.check_output(
                'wmic path win32_VideoController get name', shell=True, text=True
            ).strip().split('\n')
            gpus = [line.strip() for line in output if line.strip() and 'Name' not in line]
            return ', '.join(gpus) if gpus else "unknown gpu"
        elif sys.platform == "linux":
            # lspci to find VGA compatible controllers
            output = subprocess.check_output('lspci | grep VGA', shell=True, text=True).strip()
            return output if output else "unknown gpu"
        else:
            return "gpu info not supported"
    except Exception:
        return "unknown gpu"

def main():
    print("user system specs:")
    print(f"cpu: {get_cpu_info()}")
    print(f"ram: {get_ram_info()}")
    print(f"disk: {get_disk_info()}")
    print(f"os: {get_os_info()}")
    print(f"gpu: {get_gpu_info()}")

if __name__ == "__main__":
    main()
