## :information_source: Como rodar

É necessario ter o Python3 para rodar:

https://www.python.org/downloads/

Também é necessário o matplotlib para a interface e
o CFFI para o bind das linguagens.

Para instalar eles:

python3 -m pip install matplotlib<br />
python3 -m pip install cffi<br />

Depois disso é necessario rodar o arquivo calculations_build.py,
que vai executar o CFFI e gerar a pasta Realise, que tem o link
com o código C:

python3 calculations_build.py<br />

Depois disso é só executar o main.py que vai executar o algoritmo
e gerar a interface:

python3 main.py<br />

Se tiver algum problema para rodar o código, pode me chamar por e-mail:

rafaelcopes16@gmail.com