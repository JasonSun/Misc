n, m, c = gets.chomp!.split
n = n.to_i
m = m.to_i
ary = []
hash = {}
n.times {ary << gets.chomp!}
n.times do |i|
	m.times do |j|
		if ary[i][j] == c
			hash[ary[i][j]] = 1
			hash[ary[i - 1][j]] = 1 if i - 1 >= 0
			hash[ary[i + 1][j]] = 1 if i + 1 < n
			hash[ary[i][j - 1]] = 1 if j - 1 >= 0
			hash[ary[i][j + 1]] = 1 if j + 1 < m
		end
	end
end
hash.delete c
hash.delete '.'
puts hash.size
