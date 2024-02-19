# -*- coding: utf-8 -*-

# Pycharm에서 결과 확인
import subprocess

subprocess.run(['python', 'test.py'])

f = open('output3.txt', 'w', encoding='utf-8')
out = subprocess.check_output(['python', 'test.py'], encoding='utf-8')
f.write(out)
f.close()
