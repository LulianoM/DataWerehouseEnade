import requests
import shutil
import os
import zipfile
from io import BytesIO

os.makedirs("./DadosENADE", exist_ok=True)

lista_arquivos = [
    "https://download.inep.gov.br/microdados/Enade_Microdados/microdados_enade_2019.zip",
    "https://download.inep.gov.br/microdados/Enade_Microdados/microdados_enade_2018.zip",
    "https://download.inep.gov.br/microdados/Enade_Microdados/microdados_Enade_2017_portal_2018.10.09.zip",
]

for url in lista_arquivos:
    print(f"Baixando {url}")
    filebytes = BytesIO(requests.get(url).content)
    myzip = zipfile.ZipFile(filebytes)
    myzip.extractall("./DadosENADE")

# A partir é um código para mesclar os dados de 2018 com os de 2017 e 2019, e deixá-los na mesma pasta


def forceMergeFlatDir(srcDir, dstDir):
    if not os.path.exists(dstDir):
        os.makedirs(dstDir)
    for item in os.listdir(srcDir):
        srcFile = os.path.join(srcDir, item)
        dstFile = os.path.join(dstDir, item)
        forceCopyFile(srcFile, dstFile)


def forceCopyFile(sfile, dfile):
    if os.path.isfile(sfile):
        shutil.copy2(sfile, dfile)


def isAFlatDir(sDir):
    for item in os.listdir(sDir):
        sItem = os.path.join(sDir, item)
        if os.path.isdir(sItem):
            return False
    return True


def copyTree(src, dst):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isfile(s):
            if not os.path.exists(dst):
                os.makedirs(dst)
            forceCopyFile(s, d)
        if os.path.isdir(s):
            isRecursive = not isAFlatDir(s)
            if isRecursive:
                copyTree(s, d)
            else:
                forceMergeFlatDir(s, d)


diretorioOriginal = "./DadosENADE/"
dieretorioAntigo = "./DadosENADE/2018/"

copyTree(dieretorioAntigo, diretorioOriginal)

shutil.rmtree(dieretorioAntigo, ignore_errors=False, onerror=None)
