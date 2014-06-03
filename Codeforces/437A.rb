A = gets.strip.split('.')[1].size
B = gets.strip.split('.')[1].size
C = gets.strip.split('.')[1].size
D = gets.strip.split('.')[1].size
ary = []
ary << 'A' if (A >= B * 2 && A >= C * 2 && A >= D * 2) \
           || (A * 2 <= B && A * 2 <= C && A * 2 <= D)
ary << 'B' if (B >= A * 2 && B >= C * 2 && B >= D * 2) \
           || (B * 2 <= A && B * 2 <= C && B * 2 <= D)
ary << 'C' if (C >= A * 2 && C >= B * 2 && C >= D * 2) \
           || (C * 2 <= A && C * 2 <= B && C * 2 <= D)
ary << 'D' if (D >= A * 2 && D >= B * 2 && D >= C * 2) \
           || (D * 2 <= A && D * 2 <= B && D * 2 <= C)
puts ary.size == 1 ? ary[0] : 'C'
