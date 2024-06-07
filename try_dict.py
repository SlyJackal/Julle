i = {'price': {'regular': {'amount': 945, 'currency': 'RUB', 'denominator': 1}, 'discount': {'amount': 510, 'currency': 'RUB', 'denominator': 1}, 'viewOptions': {'priceFrom': False, 'crossPrice': True, 'useDiscount': True, 'discountPercent': 46}, 'old': {'currency': 'RUB', 'amount': 945, 'denominator': 1}, 'actual': {'currency': 'RUB', 'amount': 510, 'denominator': 1}, 'hasLoyalty': False}, 'itemId': '3155900010', 'mainVariantItemId': '3155900010', 'name': 'Hyper Easy', 'productType': 'Лайнер для глаз', 'type': 'Product', 'brand': 'Maybelline New York', 'imageUrls': [{'url': 'https://pcdn.goldapple.ru/p/p/3155900010/web/696d674d61696e8dc021cbdf8ca0e${screen}.${format}', 'format': ['webp', 'jpg'], 'screen': ['fullhd', 'tablet', 'mobile']}, {'url': 'https://pcdn.goldapple.ru/p/p/3155900010/web/696d67416464318dc021cc11f697e${screen}.${format}', 'format': ['webp', 'jpg'], 'screen': ['fullhd', 'tablet', 
'mobile']}, {'url': 'https://pcdn.goldapple.ru/p/p/3155900010/web/696d67416464328dc021cc417614d${screen}.${format}', 'format': ['webp', 'jpg'], 'screen': ['fullhd', 'tablet', 'mobile']}, {'url': 'https://pcdn.goldapple.ru/p/p/3155900010/web/696d67416464338dc021cc7050d20${screen}.${format}', 'format': ['webp', 'jpg'], 'screen': ['fullhd', 'tablet', 'mobile']}], 'favourite': False, 



'attributes': {'units': {'count': 2, 'values': ['0.6', '2,55'], 'currentUnitValue': '2,55', 'name': 'гр'}, 'colors': {'count': 2, 'values': [{'url': 'https://pcdn.goldapple.ru/p/p/3155900010/web/746f6e658dc021cca0d6aae${screen}.${format}', 'format': ['webp', 'jpg'], 'screen': ['fullhd', 'tablet', 
'mobile']}, {'url': 'https://pcdn.goldapple.ru/p/p/19000007296/web/746f6e658dad1e443f43e1c${screen}.${format}', 'format': ['webp', 'jpg'], 'screen': ['fullhd', 'tablet', 'mobile']}], 'name': '800'}}, 'labels': [{'id': 'discount', 'group': 'standard', 'backgroundColor': '#EC003D', 'text': '46%', 'textColor': '#FFFFFF', 'textGravity': ['bottom', 'middle']}], 'isAdult': False, 'inStock': False, 'url': '/3155900010-hyper-easy', 'configurable': True, 'needOnlineConsultation': False}


# название бренда
print(i.get('brand'))
# название продукта
print(i.get('name'))

#не требуется
#print(i.get('attributes').get('units').get('currentUnitValue'))
# название едениц измерения
print(i.get('attributes').get('units').get('name'))
# значения размеров
print(i.get('attributes').get('units').get('values'))
for j in i.get('attributes').get('units').get('values'):
    j = j.replace(',', '.')
    print(i.get('brand'), i.get('name'), j, i.get('attributes').get('units').get('name'))