weight = gets.to_i
if weight < 4
	case weight
	when 1
		puts 'NO'
	when 2
		puts 'NO'
	when 3
		puts 'NO'
	end
else
	if weight % 2 == 0
		puts 'YES'
	else
		puts 'NO'
	end
end
