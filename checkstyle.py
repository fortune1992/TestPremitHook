#encoding=utf-8
import os
import sys
import subprocess
import platform

def check_style():
    if platform.system().lower() == 'windows':
        ret = subprocess.call(["gradlew", "checkstyle"], shell=True)
    else:
        ret = subprocess.call(["./gradlew", "checkstyle"])

    print(ret)

    if ret != 0:
        return ret

    if platform.system().lower() == 'windows':
        ret = subprocess.call(["gradlew", "detekt"], shell=True)
    else:
        ret = subprocess.call(["./gradlew", "detekt"])
    print(ret)

    return ret


if __name__ == '__main__':
    sys.exit(check_style())
