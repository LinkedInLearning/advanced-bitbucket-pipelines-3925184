import sys
import psutil
import cpuinfo
import platform
import pkg_resources
from datetime import datetime


def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


def system_information():
    info = []  # List to hold information tuples

    # System Information
    uname = platform.uname()
    info.append(("System", uname.system))
    info.append(("Node Name", uname.node))
    info.append(("Release", uname.release))
    info.append(("Version", uname.version))
    info.append(("Machine", uname.machine))
    info.append(("Processor", uname.processor))
    info.append(("Processor Brand", cpuinfo.get_cpu_info()["brand_raw"]))

    # CPU Information
    info.append(("Physical cores", psutil.cpu_count(logical=False)))

    # Memory Information
    svmem = psutil.virtual_memory()
    info.append(("Total Memory", get_size(svmem.total)))

    # Disk Information
    partitions = psutil.disk_partitions()
    for partition in partitions:
        if partition.mountpoint in ["/", "/boot"]:
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
                info.append(
                    (
                        f"Disk: {partition.device} Total Size",
                        get_size(partition_usage.total),
                    )
                )
            except PermissionError:
                # Skip the partition if permission error
                continue

    return info


def python_information():
    """Fetches details about the Python environment."""
    info = []
    # Python Executable
    info.append(("Python Executable", sys.executable))

    # Site-Packages Location
    info.append(("Site-Packages Location", sys.prefix))

    # Installed Packages
    installed_packages = [(d.project_name, d.version) for d in pkg_resources.working_set]
    info.append(("Installed Packages", installed_packages))

    return info

if __name__ == "__main__":
    print("System Information Report")
    print("Generated on:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("=" * 40)

    system_info = system_information()
    python_info = python_information()

    for label, value in system_info:
        print(f"{label:<25}: {value}")

    print("=" * 40)
    print("Python Environment Report")
    print("=" * 40)

    for label, value in python_info:
        if label == "Installed Packages":
            print(f"{label:<25}:")
            for pkg_name, pkg_version in value:
                print(f"  - {pkg_name} ({pkg_version})")
        else:
            print(f"{label:<25}: {value}")

    print("=" * 40)

