# 数组元素的映射操作 map
# 数组弹出前N个元素 drop n
n, m = gets.split.map { |item| item.to_i }
a = gets.split.map { |item| item.to_i }
bus = 0
while true
	break if a.empty?
	tmp = m
	
	while (a.empty? == false) && (tmp >= a.first)
		tmp -= a.first
		a = a.drop 1
	end
	bus += 1
end
puts bus
