class Validator():

    def month_is_valid(self, month):
        if(month is None):
            return False
        if(int(month) not in range(1, 13)):
            return False
        return True

    def quarter_is_valid(self, quarter):
        if(int(quarter) in range(1, 5)):
            return True
        return False
