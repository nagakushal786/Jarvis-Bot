import multiprocessing
import subprocess

def start_jarvis():
  print("Jarvis starting...")
  from main import start
  start()

def listen_hotword():
  print("Jarvis listening...")
  from engine.features import hot_word
  hot_word()

if __name__=="__main__":
  subprocess.call(['cmd.exe', '/c', r'device.bat'])

  p1=multiprocessing.Process(target=start_jarvis)
  p2=multiprocessing.Process(target=listen_hotword)
  p1.start()
  p2.start()
  p1.join()

  if p2.is_alive():
    p2.terminate()
    p2.join()

  print("Jarvis stopped...")