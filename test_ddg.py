import ddg

presidents = ['Lincoln', 'Jackson', 'Johnson', 'Obama', 'Harrison',
              'Clinton', 'Coolidge', 'Arthur', 'Trump', 'Eisenhower',
              'Roosevelt', 'Pierce', 'Bush', 'Washington', 'Ford',
              'Cleveland', 'Truman', 'Hoover', 'Taft', 'Buchanan',
              'Garfield', 'Polk', 'Madison', 'Monroe', 'Carter', 'Adams',
              'Kennedy', 'Tyler', 'Buren', 'Fillmore', 'Nixon', 'Reagan',
              'Hayes', 'Roosevelt', 'Jefferson', 'Grant', 'Harding',
              'Harrison', 'McKinley', 'Wilson', 'Taylor']

def test_ddg():
    text_list = []
    for item in ddg.json_data:
        text_list.append(item['Text'].split('-')[0].split()[-1])
    for president in presidents:
        assert president in text_list
