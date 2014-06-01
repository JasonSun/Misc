source = gets.chomp!
destination = gets.chomp!
h = []
v = []
while true
	if source[0] < destination[0]
		h << 'R'
		source[0] = (source[0].ord + 1).chr
	elsif source[0] > destination[0]
		h << 'L'
		source[0] = (source[0].ord - 1).chr
	else
		h << ''
	end

	if source[1] < destination[1]
		v << 'U'
		source[1] = (source[1].to_i + 1).to_s
	elsif source[1] > destination[1]
		v << 'D'
		source[1] = (source[1].to_i - 1).to_s
	else
		v << ''
	end

	break if source == destination

end
if h.size == 1 && v.size == 1 && h[0] == '' && v[0] == '' 
	puts 0
else
	puts h.size
	h.each_index {|index| puts h[index] + v[index]}
end
