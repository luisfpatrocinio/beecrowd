def main
    qntBolinhas = gets.to_i
    qntGalhos = gets.to_i

    bolasPrecisa = (qntGalhos / 2).to_i;
    bolasFaltam = bolasPrecisa - qntBolinhas;

    if bolasFaltam > 0
        puts "Faltam #{bolasFaltam} bolinha(s)";
    else
        puts "Amelia tem todas bolinhas!";
    end
end

main