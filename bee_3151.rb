H, Z, L = gets.chomp.split.map(&:to_i)

if (H < Z && Z < L) || (L < Z && Z < H)
    puts "zezinho"
elsif (Z < H && H < L) || (L < H && H < Z)
    puts "huguinho"
else
    puts "luisinho"
end
