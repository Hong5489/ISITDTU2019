# Old Story

This is an old story about wheat and chessboard, and it's easy, right?

File:[Old_story.zip](Old_story.zip)

Inside the zip got a `cipher.txt`:
```
[524288, 4194304, 16384, 1024, 4194304, 32, 262144, 2097152, 4194304, 16777216, 70368744177664, 2251799813685248, 8192, 8388608, 8192, 4503599627370496, 16777216, 36028797018963968, 16384, 2199023255552, 67108864, 1048576, 2097152, 18014398509481984, 33554432, 68719476736, 4, 17179869184, 536870912, 549755813888, 262144, 4294967296, 16384, 128, 288230376151711744, 137438953472, 16777216, 36028797018963968, 1024, 4503599627370496, 16384, 68719476736, 262144, 4611686018427387904]
```
Which is a list of numbers

We notice all the numbers is power of 2

So we wrote a script to get the power index of each number:

```python
import math
text = [524288, 4194304, ...]
for t in text:
	print math.log(t,2)
```
Output:
```
...
37.0
24.0
55.0
10.0
52.0
14.0
36.0
18.0
62.0
```

Googling `wheat and chessboard` we found a clue which is **64**

What if the index is in **base64**?

So we code a script based on [base64 table](https://en.wikipedia.org/wiki/Base64#Base64_table):

```python
import string
import math
text = [524288, 4194304, ...]
base = string.ascii_uppercase+string.ascii_lowercase+string.digits+"+/"
print ''.join([base[int(math.log(t,2)-1)] for t in text]).decode('base64')
```

Just Guessing, simple challenge!

# Flag
> ISITDTU{r1c3_che55b0ard_4nd_bs64}