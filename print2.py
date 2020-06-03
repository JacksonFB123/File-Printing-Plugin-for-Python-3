import os, time
def run(text, filez='print2out.main'):
  main = open(filez, 'w'); main.write(text); main.close(); main = open(filez, 'r'); output = main.read(); print(output); time.sleep(.1)
def run_noOut(text, filez):
  main = open(filez, 'w'); main.write(text); main.close(); time.sleep(.1)
os.system('clear')