s = gets.strip.split
a = s[0].split(//)
k = s[1].to_i
aa = []
while k > 0 && a.size > 0
	m = k < a.size ? a[0..k].max : a[0..a.size-1].max
	mp = a.index(m)
	k -= mp if mp != 0
	aa << a[mp]
	a.delete_at(mp)
end
aa << a
puts aa.join
