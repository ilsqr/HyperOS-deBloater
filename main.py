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

# Root desteği kontrolü
root_quest = input("Cihazınızda root desteği var mı? [y/n]\n> ")
use_root = root_quest.lower() == "y"

if use_root:
    # Root izni test et
    print(colorama.Fore.CYAN + "Root izni isteniyor..." + colorama.Fore.RESET)
    root_check = subprocess.run(
        ["adb", "shell", "su", "-c", "id"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    if root_check.returncode != 0 or "uid=0" not in root_check.stdout:
        print(colorama.Fore.RED + "UYARI: Root izni alınamadı! Cihazınızın root istemcisi izni reddetti." + colorama.Fore.RESET)
        print(colorama.Fore.YELLOW + "Rootsuz modda devam ediliyor..." + colorama.Fore.RESET)
        use_root = False
    else:
        print(colorama.Fore.GREEN + "Root izni başarıyla alındı!" + colorama.Fore.RESET)

quest = input("İşlemi başlatmak istiyor musunuz? [y/n]\n> ")

if quest.lower() == "y":
    if use_root:
        print(colorama.Fore.CYAN + "Root izniyle işlem yapılıyor..." + colorama.Fore.RESET)
        for app in bloat_apps:
            package = app.strip()
            if package:
                # Önce --user 0 ile dene
                result = subprocess.run(
                    ["adb", "shell", "su", "-c", f"pm uninstall --user 0 {package}"],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                )
                if result.returncode == 0 and "Success" in result.stdout:
                    print(colorama.Fore.YELLOW + f"{package} kaldırıldı." + colorama.Fore.RESET)
                else:
                    # Başarısız olursa -k --user 0 ile dene (veriyi koruyarak)
                    result2 = subprocess.run(
                        ["adb", "shell", "su", "-c", f"pm uninstall -k --user 0 {package}"],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        text=True
                    )
                    if result2.returncode == 0 and "Success" in result2.stdout:
                        print(colorama.Fore.YELLOW + f"{package} kaldırıldı (veri korundu)." + colorama.Fore.RESET)
                    else:
                        # Son çare: disable et
                        result3 = subprocess.run(
                            ["adb", "shell", "su", "-c", f"pm disable-user --user 0 {package}"],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            text=True
                        )
                        if "disabled" in result3.stdout.lower() or result3.returncode == 0:
                            print(colorama.Fore.MAGENTA + f"{package} devre dışı bırakıldı (sistem korumalı)." + colorama.Fore.RESET)
                        else:
                            print(colorama.Fore.RED + f"{package} kaldırılamadı!" + colorama.Fore.RESET)
    else:
        print(colorama.Fore.CYAN + "Normal modda işlem yapılıyor..." + colorama.Fore.RESET)
        for app in bloat_apps:
            package = app.strip()
            if package:
                result = subprocess.run(
                    ["adb", "shell", "pm", "uninstall", "--user", "0", package],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                )
                if result.returncode == 0 and "Success" in result.stdout:
                    print(colorama.Fore.YELLOW + f"{package} kaldırıldı." + colorama.Fore.RESET)
                else:
                    print(colorama.Fore.RED + f"{package} kaldırılamadı!" + colorama.Fore.RESET)
else:
    exit()