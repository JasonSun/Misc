n = gets.to_i
hash = Hash.new
n.times do
	str = gets.chomp!
	if hash.key?(str)
		hash[str] += 1
		puts str + hash[str].to_s
	else
		hash[str] = 0
		puts 'OK'
	end
end
