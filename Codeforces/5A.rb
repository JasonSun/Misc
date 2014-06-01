hash = Hash.new
bytes = 0
while line = gets
	line.chomp!
	hash.store(line, 0) if line.start_with?('+')
	if line.start_with?('-')
		line[0] = '+'
		hash.delete(line)
	end
	if line.include?(':')
		msg = line.split(':')
		if msg.size == 1
			len = 0
		else
			len = msg[1].length
		end
		bytes += len * hash.size
	end
end
puts bytes
