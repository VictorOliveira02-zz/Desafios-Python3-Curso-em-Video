def title(txt):
    tam = len(txt)+4
    print('-'*tam)
    print(f'  {txt}')
    print('-'*tam)


while True:
    title("SYSTEM HELPER PYHELP")
    Helper = input("CAN I HELP YOU? TYPE A FUNCTION (FOR FINISH(END)): ")
    if 'end' in Helper:
        break
    help(Helper)
title("THANKS! SEE YOU SOON!")
