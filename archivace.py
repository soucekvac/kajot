from datetime import date
import tarfile
import os


date_today = str(date.today()) + ".tar.gz"
cesta = "/var/log/"

tar_obj = tarfile.open(date_today, "w:gz")

with os.scandir(cesta) as files:
    for file in files:
        if file.is_file():
            tar_obj.add(file)
            os.remove(file)

tar_obj.close()

print("done")