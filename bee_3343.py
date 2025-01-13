# Attack On Gasparini
debugMode = True

def debug(text):
    if debugMode:
        print(text)

def main():
    qntTitans, tamMuralha = list(map(int, input().split()))
    titans = input()
    tamP, tamM, tamG = list(map(int, input().split()))

    titanDamages = {"P": tamP, "M": tamM, "G": tamG}
    titanInds = {"P": 0, "M": 1, "G": 2}

    muralhas = [tamMuralha]
    indLasts = [0, 0, 0]

    for n in range(len(titans)):
        titan = titans[n]
        thisDamage = titanDamages[titan]
        percorreuQuantas = 0

        percorreuQuantas = indLasts[titanInds[titan]]

        vivo = True
        
        # Sai atacando as muralhas:
        while vivo:
            thisMuralha = muralhas[percorreuQuantas]
            if thisMuralha >= thisDamage:
                # A muralha é maior ou igual ao dano do titan. Quebrar ela.
                debug(f"[X] Titan N {n} - {titan} <causou> {thisDamage} na muralha {percorreuQuantas}.")
                muralhas[percorreuQuantas] -= thisDamage
                vivo = False
            else:
                # Muralha pequena. Pular muralha.
                debug(f"[S] Titan N {n} - {titan} <pulou> a {percorreuQuantas} muralha.")
                
                # Se essa tiver sido a última muralha, adiciona outra.
                if percorreuQuantas >= len(muralhas) - 1:
                    debug(f"[>] Muralha adicionada. ")
                    muralhas.append(tamMuralha)

                percorreuQuantas += 1

            # Guardar qual o índice da maior:
            indLasts[titanInds[titan]] = percorreuQuantas
            
            

        debug(f"Estado: {muralhas}")

    print(len(muralhas))

main()