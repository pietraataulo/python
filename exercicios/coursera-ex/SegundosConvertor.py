segundos_str = input("Por favor, entre com o número de segundos que deseja converter: ")
total_segs = int(segundos_str)

dias = total_segs // (3600 * 24)
segs_restantes = total_segs % (3600 * 24)
horas = segs_restantes // 3600
segs_restantes2 = segs_restantes % 3600
minutos = segs_restantes2 // 60
segs_restantes_final = segs_restantes2 % 60

print(dias,"dias,",horas,"horas,",minutos,"minutos e",segs_restantes_final,"segundos.")