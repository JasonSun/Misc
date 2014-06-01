# 使用数组保存)对应的最长的sequence长度
line = gets
line.strip!
longest = []  # )对应的最长的sequence长度
opn = []
i = 0
line.each_char do |ch|
	if ch == '('
		opn << i
	else
		if opn.empty?
			longest[i] = -1
		else
			relative = opn.pop
			longest[i] = i - relative + 1 # 不是最优，需要向前搜索
			if relative > 0 && line[relative - 1] == ")" && longest[relative - 1] != -1
				longest[i] += longest[relative - 1]
			end
		end
	end
	i += 1
end
max = 0
cnt = 1
# 不能使用.max方法，因为数组中有nil，不能将nil与整数相比较
longest.each do |item|
	if item && (item > max)
		max = item
		cnt = 1
	elsif item == max
		cnt += 1
	end
end
puts "#{max} #{cnt}"
