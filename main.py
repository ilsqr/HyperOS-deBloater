import subprocess
import colorama

def is_package_installed(package_name):
    result = subprocess.run(
        ["adb", "shell", "pm", "list", "packages", package_name],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    return f"package:{package_name}" in result.stdout

bloat_apps = []

with open("apps.txt", "r") as f:
    for x in f:
        package = x.strip()
        if package:
            if is_package_installed(package):
                print(colorama.Fore.GREEN + f"{package} yüklü." + colorama.Fore.RESET)
                bloat_apps.append(x)
            else:
                print(colorama.Fore.RED + f"{package} yüklü değil." + colorama.Fore.RESET)

print(colorama.Fore.BLUE + f"{len(bloat_apps)} adet uygulama cihazdan kaldırabilir." + colorama.Fore.RESET)
quest = input("İşlemi başlatmak istiyor musunuz? [y/n]\n> ")

if quest.lower() == "y":
    for app in bloat_apps:
        package = app.strip()
        if package:
            subprocess.run(
                ["adb", "shell", "pm", "uninstall", package],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            print(colorama.Fore.YELLOW + f"{package} kaldırıldı." + colorama.Fore.RESET)
else:
    exit()