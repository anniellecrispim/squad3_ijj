list_frutas = ['manga', 'coco', 'banana', 'cereja', 'laranja', 'uva']
list_alergia = ['coco', 'acerola']

for alergia in list_alergia:
    if alergia in list_frutas:
        print(f"{alergia} está presente na lista de frutas.")
