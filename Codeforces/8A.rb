str1 = gets.chomp!
str2 = gets.chomp!
str3 = gets.chomp!
forward = backward = false
if str1.match(/#{str2}\w*#{str3}/)
	forward = true
end
str11 = str1.reverse
if str11.match(/#{str2}\w*#{str3}/)
	backward = true
end
if forward && backward
	puts 'both'
elsif forward
	puts 'forward'
elsif backward
	puts 'backward'
else
	puts 'fantasy'
end
