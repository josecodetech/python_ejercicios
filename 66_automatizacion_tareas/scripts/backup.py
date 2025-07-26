import shutil
import os
import datetime
import logging

try:
    origen = "D:\\Workspace\\WorkspaceTutorialEjerciciosPython\\66_automatizacion_tareas\\logs"
    destino_base = "D:\\Workspace\\WorkspaceTutorialEjerciciosPython\\66_automatizacion_tareas\\backup_logs"
    fecha = datetime.datetime.now().strftime("%Y-%m-%d")
    destino = os.path.join(destino_base, fecha)
    shutil.copytree(origen, destino, dirs_exist_ok=True)
    logging.info(f"Backup realizado en: {destino}")
    # print(f"Backup realizado en: {destino}")
except Exception as e:
    logging.error(f"Error al realizar el backup: {e}")
    # print(f"Error al realizar el backup: {e}")