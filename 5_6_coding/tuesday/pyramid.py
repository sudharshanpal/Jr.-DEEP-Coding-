# you can change this to whatever you want
height = 5

# Right-side pyramid
print("Right-side Pyramid:")
for i in range(1, height + 1):
    print('*' * i)

print("\nLeft-side Pyramid:")
# Left-side pyramid
for i in range(1, height + 1):
    print(' ' * (height - i) + '*' * i)

print("\nFull Pyramid:")
# Full centered pyramid
for i in range(1, height + 1):
    print(' ' * (height - i) + '*' * (2 * i - 1))
