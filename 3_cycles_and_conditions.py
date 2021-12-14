currencies= [
{"Cur_ID":440,
"Date":"2021-10-04T00:00:00",
"Cur_Abbreviation":"AUD",
"Cur_Scale":1,
"Cur_Name":"Австралийский доллар",
"Cur_OfficialRate":1.8195},
{"Cur_ID":510,
"Date":"2021-10-04T00:00:00",
"Cur_Abbreviation":"AMD",
"Cur_Scale":1000,
"Cur_Name":"Армянских драмов",
"Cur_OfficialRate":5.1269},
{"Cur_ID":441,
"Date":"2021-10-04T00:00:00",
"Cur_Abbreviation":"BGN",
"Cur_Scale":1,
"Cur_Name":"Болгарский лев",
"Cur_OfficialRate":1.4888},
{"Cur_ID":449,
"Date":"2021-10-04T00:00:00",
"Cur_Abbreviation":"UAH",
"Cur_Scale":100,
"Cur_Name":"Гривен",
"Cur_OfficialRate":9.4427},
{"Cur_ID":450,
"Date":"2021-10-04T00:00:00",
"Cur_Abbreviation":"DKK",
"Cur_Scale":10,
"Cur_Name":"Датских крон",
"Cur_OfficialRate":3.9156},
]


# for curr in currencies:
# 	print(curr)


print([x for x in (1,2,3,4)])
print((x for x in (1,2,3,4)))

for x in (x for x in (1,2,3,4)):
	print(x)