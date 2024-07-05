from django_q.tasks import schedule

schedule('currency.tasks.parse_xml_task',
         q_options={'timeout': 30}, minutes=1)
