def add_time(start_time, duration, day = None):
  time, notation = start_time.split()
  hour, minute = time.split(':')
  hour=int(hour)
  minute=int(minute)
  dur_hr, dur_min = duration.split(':')
  dur_hr = int(dur_hr)
  dur_min = int(dur_min)
  day_in_week=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
  count=0
  if day==None:
    if notation == 'AM':
      if dur_hr % 24 == 0:
        final = (hour*60)+minute+dur_min+dur_hr*60
        days = (final//60)//24
        minute += dur_min
        final_time= (hour*60)+minute
        hr = (final_time//60)
        minute = (final_time%60)
        if minute>=60:
          minute-=60
        if minute<10:
          minute = '0' + str(minute)
        if days==0:
          if hr<12:
            return (str(hr)+':'+str(minute)+' AM')
          elif hr>12:
            hr-=12
            return (str(hr)+':'+str(minute)+' PM')
          else:
            hr=12
            return (str(hr)+':'+str(minute)+' PM') 
        elif days == 1:
          if hr<12:
            return (str(hr)+':'+str(minute)+' AM '+'(next day)')
          elif hr>12:
            hr-=12
            return (str(hr)+':'+str(minute)+' PM '+'(next day)')
          else:
            return (str(hr)+':'+str(minute)+' PM '+'(next day)')
        else:
          if hr<12:
            return (str(hr)+':'+str(minute)+' AM '+'('+str(days)+' days later)')
          elif hr>12:
            hr-=12
            return (str(hr)+':'+str(minute)+' PM '+'('+str(days)+' days later)')
          else:
            return (str(hr)+':'+str(minute)+' PM '+'('+str(days)+' days later)')
      else:
        final = (hour*60)+minute+(dur_hr*60)+dur_min
        days = (final//60)//24
        hr= (final//60)%24
        minute=minute+dur_min
        if minute>=60:
          minute-=60
        if minute<10:
          minute = '0' + str(minute)
        if days==0:
          if hr<12:
            return (str(hr)+':'+str(minute)+' AM')
          elif hr>12:
            hr-=12
            return (str(hr)+':'+str(minute)+' PM')
          else:
            return (str(hr)+':'+str(minute)+' PM')
        elif days==1:
          if hr<12:
            return (str(hr)+':'+str(minute)+' AM '+'(next day)')
          elif hr>12:
            hr-=12
            return (str(hr)+':'+str(minute)+' PM '+'(next day)')
          else:
            hr-=12
            return (str(hr)+':'+str(minute)+' PM '+'(next day)')
        else:
          if hr<12:
            return (str(hr)+':'+str(minute)+' AM '+'('+str(days)+' days later)')
          elif hr>12:
            hr-=12
            return (str(hr)+':'+str(minute)+' PM '+'('+str(days)+' days later)')
          else:
            return (str(hr)+':'+str(minute)+' PM '+'('+str(days)+'days later)')
    
    elif notation == 'PM':
      hour += 12
      if dur_hr % 24 == 0:
        final = (hour*60)+minute+(dur_hr*60)+dur_min
        days = (final//60)//24
        minute += dur_min
        final_time= (hour*60)+minute
        hr = (final_time//60)
        minute = (final_time%60)
        if minute>=60:
          minute-=60
        if minute<10:
          minute = '0' + str(minute)
        if days==0:
          if hr<12:
              return (str(hr)+':'+str(minute)+' AM')
          elif hr>=24:
              hr-=24
              if hr==0:
                hr=12
                return (str(hr)+':'+str(minute)+' AM')
              else:
                return (str(hr)+':'+str(minute)+' AM')
          else:
            hr-=12
            return (str(hr)+':'+str(minute)+' PM')
        elif days == 1:
          if hr<12:
            return (str(hr)+':'+str(minute)+' AM '+'(next day)')
          elif hr>=24:
            hr-=12
            return (str(hr)+':'+str(minute)+' AM '+'(next day)')
          else:
            hr-=12
            return (str(hr)+':'+str(minute)+' PM '+'(next day)')
        else:
          if hr<12:
            return (str(hr)+':'+str(minute)+' AM '+'('+str(days)+' days later)')
          elif hr>=24:
            hr-=12
            return (str(hr)+':'+str(minute)+' AM '+'('+str(days)+' days later)')
          else:
            hr-=12
            return (str(hr)+':'+str(minute)+' PM '+'('+str(days)+' days later)')
      else:
        final = (hour*60)+minute+(dur_hr*60)+dur_min
        days = (final//60)//24
        hr= (final//60)%24
        minute=minute+dur_min
        if minute>=60:
          minute-=60
        if minute<10:
          minute = '0' + str(minute)
        if days==0:
          if hr<12:
            return (str(hr)+':'+str(minute)+' AM')
          elif hr>=24:
            hr-=24
            if hr==0:
              hr=12
              return (str(hr)+':'+str(minute)+' AM')
            else:
              return (str(hr)+':'+str(minute)+' AM')
          else:
            hr-=12
            return (str(hr)+':'+str(minute)+' PM')
        elif days==1:
          if hr<12:
            return (str(hr)+':'+str(minute)+' AM '+'(next day)')
          elif hr>=24:
            hr-=24
            if hr==0:
                hr=12
                return (str(hr)+':'+str(minute)+' AM '+'(next day)')
            else:
                return (str(hr)+':'+str(minute)+' AM '+'(next day)')
          else:
            hr-=12
            return (str(hr)+':'+str(minute)+' PM '+'(next day)')
        else:
          if hr<12:
            return (str(hr)+':'+str(minute)+' AM '+'('+str(days)+' days later)')
          elif hr>=24:
            hr-=24
            if hr==0:
              hr=12
              return (str(hr)+':'+str(minute)+' AM '+'('+str(days)+' days later)')
            else:
              return(str(hr)+':'+str(minute)+' AM '+'('+str(days)+' days later)')
          else:
            hr-=12
            return(str(hr)+':'+str(minute)+' PM '+'('+str(days)+'days later)')           

  else:
    for i in day_in_week:
      if day.casefold()==i.casefold():
        day=i
        key=count
      count+=1
      #print(i)
      #print(day)
    if notation == 'AM':
      if dur_hr % 24 == 0:
        final = (hour*60)+minute+dur_min+dur_hr*60
        days = (final//60)//24
        minute += dur_min
        final_time= (hour*60)+minute
        hr = (final_time//60)
        minute = (final_time%60)
        if minute>=60:
          minute-=60
        if minute<10:
          minute = '0' + str(minute)
        if days==0:
          if hr<12:
            return (str(hr)+':'+str(minute)+' AM, '+day)
          elif hr>12:
            hr-=12
            return (str(hr)+':'+str(minute)+' PM, '+day)
          else:
            hr=12
            return (str(hr)+':'+str(minute)+' PM, '+day)

        elif days == 1:
          key= (key + days)%7
          day_updated = day_in_week[key]
          if hr<12:
            return (str(hr)+':'+str(minute)+' AM, '+day_updated+' (next day)')
          elif hr>12:
            hr-=12
            return (str(hr)+':'+str(minute)+' PM, '+day_updated+' (next day)')
          else:
            return (str(hr)+':'+str(minute)+' PM, '+day_updated+' (next day)')
        else:
          key= (key + days)%7
          day_updated = day_in_week[key]
          if hr<12:
            return (str(hr)+':'+str(minute)+' AM, '+day_updated+' ('+str(days)+' days later)')
          elif hr>12:
            hr-=12
            return (str(hr)+':'+str(minute)+' PM, '+day_updated+' ('+str(days)+' days later)')
          else:
            return (str(hr)+':'+str(minute)+' PM, '+day_updated+' ('+str(days)+' days later)')
      else:
        final = (hour*60)+minute+(dur_hr*60)+dur_min
        days = (final//60)//24
        hr= (final//60)%24
        minute=minute+dur_min
        if minute>=60:
          minute-=60
        if minute<10:
          minute = '0' + str(minute)
        if days==0:
          if hr<12:
            return (str(hr)+':'+str(minute)+' AM, '+day)
          elif hr>12:
            hr-=12
            return (str(hr)+':'+str(minute)+' PM, '+day)
          else:
            return (str(hr)+':'+str(minute)+' PM, '+day)
        elif days==1:
          key= (key + days)%7
          day_updated = day_in_week[key]
          if hr<12:
            return (str(hr)+':'+str(minute)+' AM, '+day_updated+' (next day)')
          elif hr>12:
            hr-=12
            return (str(hr)+':'+str(minute)+' PM, '+day_updated+' (next day)')
          else:
            hr-=12
            return (str(hr)+':'+str(minute)+' PM, '+day_updated+' (next day)')
        else:
          key= (key + days)%7
          day_updated = day_in_week[key]
          if hr<12:
            return (str(hr)+':'+str(minute)+' AM, '+day_updated+' ('+str(days)+' days later)')
          elif hr>12:
            hr-=12
            return (str(hr)+':'+str(minute)+' PM, '+day_updated+' ('+str(days)+' days later)')
          else:
            return (str(hr)+':'+str(minute)+' PM, '+day_updated+' ('+str(days)+'days later)')

    elif notation == 'PM':
      hour += 12
      if dur_hr % 24 == 0:
        final = (hour*60)+minute+(dur_hr*60)+dur_min
        days = (final//60)//24
        minute += dur_min
        final_time= (hour*60)+minute
        hr = (final_time//60)
        minute = (final_time%60)
        if minute>=60:
          minute-=60
        if minute<10:
          minute = '0' + str(minute)
        if days==0:
          if hr<12:
            return (str(hr)+':'+str(minute)+' AM, '+day)
          elif hr>=24:
            hr-=24
            if hr==0:
              hr=12
              return (str(hr)+':'+str(minute)+' AM, '+day)
            else:
              return (str(hr)+':'+str(minute)+' AM, '+day)
          else:
            hr-=12
            return (str(hr)+':'+str(minute)+' PM, '+day)
        elif days == 1:
          key= (key + days)%7
          day_updated = day_in_week[key]
          if hr<12:
            return (str(hr)+':'+str(minute)+' AM, '+day_updated+' (next day)')
          elif hr>=24:
            hr-=12
            return (str(hr)+':'+str(minute)+' AM, '+day_updated+' (next day)')
          else:
            hr-=12
            return (str(hr)+':'+str(minute)+' PM, '+day_updated+' (next day)')
        else:
          key= (key + days)%7
          day_updated = day_in_week[key]
          if hr<12:
            return (str(hr)+':'+str(minute)+' AM, '+day_updated+' ('+str(days)+' days later)')
          elif hr>=24:
            hr-=12
            return (str(hr)+':'+str(minute)+' AM, '+day_updated+' ('+str(days)+' days later)')
          else:
            hr-=12
            return (str(hr)+':'+str(minute)+' PM, '+day_updated+' ('+str(days)+' days later)')
      else:
        final = (hour*60)+minute+(dur_hr*60)+dur_min
        days = (final//60)//24
        hr= (final//60)%24
        minute=minute+dur_min
        if minute>=60:
          minute-=60
        if minute<10:
          minute = '0' + str(minute)
        if days==0:
          if hr<12:
            return (str(hr)+':'+str(minute)+' AM, '+day)
          elif hr>=24:
            hr-=24
            if hr==0:
              hr=12
              return (str(hr)+':'+str(minute)+' AM, '+day)
            else:
              return (str(hr)+':'+str(minute)+' AM, '+day)
          else:
            hr-=12
            return (str(hr)+':'+str(minute)+' PM, '+day)
        elif days==1:
          key= (key + days)%7
          day_updated = day_in_week[key]
          if hr<12:
            return (str(hr)+':'+str(minute)+' AM, '+day_updated+' (next day)')
          elif hr>=24:
            hr-=24
            if hr==0:
              hr=12
              return (str(hr)+':'+str(minute)+' AM, '+day_updated+' (next day)')
            else:
              return (str(hr)+':'+str(minute)+' AM, '+day_updated+' (next day)')
          else:
            hr-=12
            return (str(hr)+':'+str(minute)+' PM,'+day_updated+' (next day)')
        else:
          key= (key + days)%7
          day_updated = day_in_week[key]
          if hr<12:
            return (str(hr)+':'+str(minute)+' AM, '+day_updated+' ('+str(days)+' days later)')
          elif hr>=24:
            hr-=24
            if hr==0:
              hr=12
              return (str(hr)+':'+str(minute)+' AM, '+day_updated+' ('+str(days)+' days later)')
            else:
              return (str(hr)+':'+str(minute)+' AM, '+day_updated+' ('+str(days)+' days later)')
          else:
            hr-=12
            return (str(hr)+':'+str(minute)+' PM '+day_updated+' ('+str(days)+'days later)')
              
