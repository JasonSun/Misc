n = gets.to_i
n.times do
	str = gets.chomp
	
	if re  = str.match(/^R(\d+)C(\d+)$/)
		c = re[2].to_i
		s = ""
		while c != 0
			mod = c % 26
			if mod == 0
				mod = 26
				c -= mod
			end
			s << (mod + 64).chr
			c /= 26
		end
		print s.reverse, re[1], "\n"
	elsif re  = str.match(/^([A-Z]+)(\d+)$/)
		c = 0
		re[1].each_byte do |char|
			c = char - 64 + c * 26
		end
		print "R", re[2], "C", c, "\n"
	end
end
