# # 使用Hash表保存)对应的最长的sequence长度

# # 使用Hash会超时提交不过，报超时错误，可见Hash的时间效率不如直接用数组快。

line = gets
line.strip!
hash_longest = Hash.new  # )对应的最长的sequence长度
opn = []
i = 0
line.each_char do |ch|
	if ch == '('
		opn << i
	else
		if opn.empty?
			hash_longest[i] = -1
		else
			relative = opn.pop
			hash_longest[i] = i - relative + 1 # 不是最优，需要向前搜索
			if relative > 1 && line[relative - 1] == ")" && hash_longest[relative - 1] != -1
				hash_longest[i] += hash_longest[relative - 1]
			end
		end
	end
	i += 1
end
max = 0
cnt = 1
hash_longest.each_value do |value|
	if value > max
		max = value
		cnt = 1
	elsif value == max
		cnt += 1
	end
end
puts "#{max} #{cnt}"
