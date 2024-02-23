# ввід
xx = int(input("Для сну потрібно(хвилини):"))
hh = int(input("Година, о котрій засинає:"))
mm = int(input("і хвилин: "))

total_minutes = hh * 60 + mm 
wake_up_time = total_minutes + xx 
wake_up_hours = wake_up_time // 60
wake_up_minutes = wake_up_time % 60 

# Виводимо результат
print(wake_up_hours)
print(wake_up_minutes)
