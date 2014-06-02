str = gets.strip!
str.squeeze!('/')
if str.end_with?('/') && (str.size != 1)
	puts str.chop!
else
	puts str
end
