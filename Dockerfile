## Dockerfile
# Toda linha que iniciar com '#' e um comentário
FROM python:3

# ADD adiciona arquivos ao container na pasta indicada
ADD run.py /
ADD requirements.txt /

COPY . /app

# WORKDIR indica a pasta padrão do container
WORKDIR /app

# RUN executa instruções no container
RUN pip install -r requirements.txt --upgrade

# CMD indica com o que e como será executado uma instrução
# O comando python executará o arquivo Line_Line_to_Bd.py
CMD python run.py