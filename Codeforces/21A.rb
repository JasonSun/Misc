str = gets.strip!
re_pattern = /^\w{1,16}@(\w{1,16}(\.\w{1,16})*)(\/\w{1,16})?$/
if str.match(re_pattern) && $1.size <= 32
	puts 'YES'
else
	puts 'NO'
end
