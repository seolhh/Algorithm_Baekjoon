# # 값은 모두 15로 통
#
#
# # 10진수로 변환-> int(n진수)
# print(int(0b1111))
#
# # 2진수로 변환 -> bin(n진수)
# print(bin(0o17))
#
# # 8진수로 변환 -> oct(n진수)
# print(oct(0xf))
#
# # 16진수로 변환 -> hex(n진수)
# print(hex(15))

a=int(input(),8)
print(bin(a)[2:])