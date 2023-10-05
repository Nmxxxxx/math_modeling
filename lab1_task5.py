a = "Шляпка гриба, покрытая … кожиц..й, держится на … ножк.. . Снизу шляпка затянута … плёнкой. Когда её уберёшь, откроется нижняя … сторона шляпк..."

print(a)

first_word = input('Покрытая .. : ')
first_err = input('кожиц..й : ')
second_word = input('держится на ...?: ')
second_err = input(' ножк.. ?: ')
third_word = input('затянута ..?: ')
last_word = input('откроется нижняя..?: ')
last_err = input('шляпк..?: ')
b = f"Шляпка гриба, покрытая {first_word} кожиц{first_err}й, держится на {second_word} ножк{second_err} . Снизу шляпка затянута {third_word} плёнкой. Когда её уберёшь, откроется нижняя {last_word} сторона шляпк{last_err}"
print(b)