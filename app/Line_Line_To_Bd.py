#!/usr/bin/env python3

import json
from collections import OrderedDict
from datetime import datetime

import simplejson as json
import xlrd
columns = [
    'nome',
    'email',
    'telefone',
    'sms_check_alert',
    'email_check_alert',
    'call_check_alert',
    'push_check_alert',
    'whatsapp_check_alert',
    'alerta_verde',
    'alerta_amarelo',
    'alerta_vermelho',
    'hora_inicial',
    'hora_final',
    'dom',
    'seg',
    'ter',
    'qua',
    'qui',
    'sex',
    'sab',
    'regiao'
]
name_to_json_file = datetime.now().strftime('%m%d%Y_%H%M%S')


def line_line_to_bd(wb):
    """
    :param wb:
    :return:
    """

    try:
        sh = wb.sheet_by_index(0)
        data_list = []
        try:
            for rownum in range(1, sh.nrows):
                c = 0
                data = OrderedDict()
                row_values = sh.row_values(rownum)

                for name_columns in columns:
                    data[name_columns] = row_values[c]
                    c += 1

                data_list.append(data)
                show_json_file = json.dumps(data)
                print(show_json_file)

        except Exception as e:
                print("for rownum in range(x, sh.nrows): error ==>", e)
        # Serialize the list of dicts to JSON
        finally:

            j = json.dumps(data_list)
            save_json_file(j)

    except Exception as e:
        print("line_line_to_bd error ==>", e)
    finally:
        print("EOF")


def ler_planilha():
    """
    :return:
    """
    try:
        # TODO: fazer buscar arquivo na pasta
        wb = xlrd.open_workbook(
            'app/spreadsheets/contacts.xlsx',
        )

        # self.df.info()
        line_line_to_bd(wb)
    except FileNotFoundError:
        print("Arquivo nao existe!")


def save_json_file(j):
    """
    Cria arquivo .json usando data e hora no inicio do arquivo.
    MMDDYYYY_HHMMSS
    """
    try:
        with open('app/processed/' + name_to_json_file + '.json', 'w') as f:
            f.write(j)
    except Exception as e:
        print("save_json_file error ==>", e)
