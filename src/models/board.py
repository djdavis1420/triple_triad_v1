class Board:
    positions = {
        'top_left': {'card': None, 'original_owner': None, 'current_owner': None},
        'top_center': {'card': None, 'original_owner': None, 'current_owner': None},
        'top_right': {'card': None, 'original_owner': None, 'current_owner': None},
        'mid_left': {'card': None, 'original_owner': None, 'current_owner': None},
        'mid_center': {'card': None, 'original_owner': None, 'current_owner': None},
        'mid_right': {'card': None, 'original_owner': None, 'current_owner': None},
        'bot_left': {'card': None, 'original_owner': None, 'current_owner': None},
        'bot_center': {'card': None, 'original_owner': None, 'current_owner': None},
        'bot_right': {'card': None, 'original_owner': None, 'current_owner': None}
    }

    def __repr__(self):
        top_lines = [Board.__represent_card(v) for k, v in self.positions.items() if 'top' in k]
        mid_lines = [Board.__represent_card(v) for k, v in self.positions.items() if 'mid' in k]
        bot_lines = [Board.__represent_card(v) for k, v in self.positions.items() if 'bot' in k]
        return f'{top_lines}\n{mid_lines}\n{bot_lines}'

    @staticmethod
    def __represent_card(v):
        if v['card'] is None:
            return 'No Card'
        else:
            x = v['card']['name']
            y = v['current_owner']
            z = f'{x} - {y}'
            return z
