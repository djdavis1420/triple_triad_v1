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
        top_positions = [Board.__represent_card(v) for k, v in self.positions.items() if 'top' in k]
        mid_positions = [Board.__represent_card(v) for k, v in self.positions.items() if 'mid' in k]
        bot_positions = [Board.__represent_card(v) for k, v in self.positions.items() if 'bot' in k]
        top_line = '|'.join(top_positions)
        mid_line = '|'.join(mid_positions)
        bot_line = '|'.join(bot_positions)
        divider = '-' * 50
        return f'{top_line}\n{divider}\n{mid_line}\n{divider}\n{bot_line}'

    @staticmethod
    def __represent_card(v):
        if v['card'] is None:
            return 'No Card'
        else:
            x = v['card']['name']
            y = v['current_owner']
            z = f'{x} - {y}'
            return z
