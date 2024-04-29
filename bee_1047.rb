def main
    # Em Ruby, usamos a função chomp.split.map para obter vários dados numa única linha.
    # chomp = remove a nova linha \n no final.
    # split = divide normal
    # map(&:to_i) aplica a função to_i a cada elemento

    horaInicial, minutoInicial, horaFinal, minutoFinal = gets.chomp.split.map(&:to_i)
    if horaInicial < horaFinal 
        duracaoHoras = horaFinal - horaInicial
    else
        duracaoHoras = (24 - horaInicial) + horaFinal
    end

    if minutoInicial < minutoFinal
        duracaoMinutos = minutoFinal - minutoInicial
    else
        duracaoMinutos = 60 - minutoInicial + minutoFinal
        duracaoHoras = duracaoHoras - 1
    end
    
    if duracaoMinutos == 60
        duracaoHoras = duracaoHoras + 1
        duracaoMinutos = 0
    end

    if duracaoHoras == 24 and duracaoMinutos > 0
        duracaoHoras = 0
    end
    	
    # O JOGO DUROU 0 HORA(S) E 59 MINUTO(S)
    puts "O JOGO DUROU #{duracaoHoras} HORA(S) E #{duracaoMinutos} MINUTO(S)"
end

main