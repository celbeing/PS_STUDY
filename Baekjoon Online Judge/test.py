bb = list(map(int, input().split()))
st = [(0, 0, 0, 0)]
res = 0
n = len(bb)

while st:
    idx, sum_a, sum_b, count = st.pop()
    if idx == n:
        res = max(res, count)
        continue
    num = bb[idx]
    st.append((idx + 1, sum_a, sum_b, count))
    if sum_b + num <= 30:
        st.append((idx + 1, sum_a, sum_b + num, count + 1))
    if sum_a + num <= 30:
        st.append((idx + 1, sum_a + num, sum_b, count + 1))
print(res)