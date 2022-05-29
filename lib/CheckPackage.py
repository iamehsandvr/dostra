import sys
import os
import importlib.util
import subprocess


class CheckPackageClass:
    def InstallModule():
        CurrectPath = os.getcwd()
        with open(CurrectPath + os.sep + 'requirements.txt', 'r') as File:
            for ModuleName in File:
                ModuleName = ''.join(
                    char for char in ModuleName if char.isalpha())
                if importlib.util.find_spec(ModuleName) is None:
                    subprocess.check_call(
                        [sys.executable, '-m', 'pip', 'install', ModuleName])
                    reqs = subprocess.check_output(
                        [sys.executable, '-m', 'pip', 'freeze'])
                    InstalledModules = [r.decode().split('==')[0]
                                        for r in reqs.split()]
                    print(InstalledModules)
                else:
                    pass
        os.system("cls" if os.name == "nt" else "clear")
