# Criando um ambiente virtual

Vamos primeiro criar uma pasta para simular esse novo projeto, você pode fazer manualmente ou pelo terminal:

"""
mkdir novo_projeto

"""
Agora, vamos entrar na pasta do projeto:

"""
cd novo_projeto/

"""

Para criar o ambiente virtual, abra o terminal dentro da pasta criada e faça:

"""
python -m venv nome_do_ambiente_virtual

"""

O `nome_do_ambiente_virtual` por convenção utiliza-se `venv`, mas poderiamos utilizar outro nome sem problema algum. A partir do comando acima será criada a pasta que conterá a versão do Python instalada em sua máquina e todas as bibliotecas que serão instaladas nesse projeto, ou seja, as bibliotecas do nosso novo_projeto ficarão apenas nesse diretório e não diretamente no sistema principal como era feito antes.

Mas, não basta somente criar o ambiente, é necessário ativá-lo:
"""
source nome_do_ambiente_virtual/bin/activate

"""
