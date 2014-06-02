n, m = gets.strip.split.map { |e| e.to_i }
color = ''
bool = true
n.times do
	str = gets.strip.squeeze
	if str.size != 1
		bool = false
	else
		if str != color
			color = str
		else
			bool = false
		end
	end
end
puts bool ? 'YES' : 'NO'
