import cmdinterface as ci
from colorama import init as coloramainit
from colorama import Fore, Back, Style
coloramainit()
try:
    open("start.lh", "r")
except FileNotFoundError:
    ci.echo("0>start.lh")
    open("start.lh", "w").write("1")
finally:
    sett = ci.load("config.toml", 1)
    with open("start.lh", "r") as f:
        started = int(f.read())
    if started == 1:
        newJson = []
        ci.aprint(sett["app"]["name"])
        pcOpi = input("What your device? [PC|PI] > ").lower()
        if pcOpi == "pc": newJson.append(0)
        elif pcOpi == "pi": newJson.append(1)
        else: newJson.append(None)
        newJson.append(input("Your telegram bot token > "))
        newJson.append(input("Your telegram user id > "))
        ci.jsDump(sett["files"]["dataFile"], newJson)
        ci.fWrite("start.lh", "0")
    else:
        newJson = ci.load(sett["files"]["dataFile"], 2)

if newJson[0] == 0:
    ci.textAnimation(sett["app"]["name"], 0.1)
    while True:
        ci.update()
        inputs = []
        outputs = []
        ci.aprint(sett["app"]["name"])
        for i in range(sett["limites"]["inputPorts"]):
            try:
                infilerd = ci.fRead(f"{sett['files']['dataDir']}\\i{i+1}.lh")
            except FileNotFoundError:
                indenfalas = open(f"{sett['files']['dataDir']}\\i{i+1}.lh", "w")
                indenfalas.close()
                infilerd = ci.fRead(f"{sett['files']['dataDir']}\\i{i + 1}.lh")
            if not infilerd == "":
                inputs.append(infilerd)
            else: inputs.append("NONE")

        amounts = []
        for i in range(sett["limites"]["inputPorts"]):
            amounts.append(inputs[i])

        inputsgui = []
        for i in range(sett["limites"]["inputPorts"]):
            inputsgui.append(f"Input {i+1}")

        textToPrint = [inputsgui,amounts]
        print(ci.stabulate(textToPrint))

        for i in range(sett["limites"]["outputPorts"]):
            try:
                infilerd = ci.fRead(f"{sett['files']['dataDir']}\\o{i+1}.lh")
            except FileNotFoundError:
                indenfalas = open(f"{sett['files']['dataDir']}\\o{i+1}.lh", "w")
                indenfalas.close()
                infilerd = ci.fRead(f"{sett['files']['dataDir']}\\o{i + 1}.lh")
            if not infilerd == "":
                outputs.append(infilerd)
            else: outputs.append("NONE")

        amountsO = []
        for i in range(sett["limites"]["outputPorts"]):
            amountsO.append(outputs[i])

        outputsgui = []
        for i in range(sett["limites"]["outputPorts"]):
            outputsgui.append(f"Output {i+1}")

        textToPrintO = [outputsgui,amountsO]
        print(ci.stabulate(textToPrintO))
        ci.asleep(sett["settings"]["delayOfInput"])