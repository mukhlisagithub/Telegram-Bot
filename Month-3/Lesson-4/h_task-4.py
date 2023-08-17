# task-4: MinuteConverter classini tuzing. U quyida berilgan parameterlar va methodlarga ega bolsin.
# parameter: minutes
# methods: ToHours(), toSeconds(), toDays()
# Tuzilgan class asosida obyekt yasang. toHours() metodi chaqirilgan payt, classdagi minutes soatlarga,
# toSeconds() chaqirilganda sekundlarga va toDays chaqirilgan payt kunlarga otkazilsin!


class MinuteConverter:
    def __init__(self, minutes):
        self.minutes =  minutes

    def toHours(self):
        return self.minutes / 60

    def toSeconds(self):
        return self.minutes * 60

    def toDays(self):
        return self.minutes / (60*24)


minconv = MinuteConverter(15)
# print(minconv)
print(minconv.toHours())
print(minconv.toSeconds())
print(minconv.toDays())