import datetime

from app.Line_Line_To_Bd import ler_planilha

if __name__ == '__main__':
    print("init")
    try:
        print(datetime.datetime.now().strftime('%H:%M:%S'))

        ler_planilha()

        print(datetime.datetime.now().strftime('%H:%M:%S'))
    except Exception as e:
        print(e)
    finally:
        print("End")
