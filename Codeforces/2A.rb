n = gets.to_i
ary = []
hash = Hash.new 0
n.times do
	list = gets.split
	name = list[0]
	score = list[1].to_i
	hash.has_key?(name) ? hash[name] += score : hash[name] = score
	ary << [name, hash[name]]
end
maximum = hash.values.max
candidates = hash.select {|key, value| value == maximum}
ary.each do |entry|
	if candidates.key?(entry[0]) && entry[1] >= maximum
		puts entry[0]
		break
	end
end
