class Time:
    """Egyszeru osztaly eltelt ido modellezesere
    """

    def __init__(self, seconds:int=0):
        """Inicializalja az idot a megadott masodpercekkel

        Args:
            seconds (int): a masodpercek szama
        """
        self.seconds = seconds
        
    def to_seconds(self) -> int:
        """Adja vissza egy `int`-ben, hogy masodpercben kifejezve mennyi az ido

        Returns:
            int: a tarolt ido masodpercekben

        >>> Time(12).to_seconds()
        12
        >>> Time(345).to_seconds()
        345
        """
        secs = self.seconds
        return secs

    def _ss(self)->int:
        """Visszaadja, hogy mennyit mutat a "masodpercmutato"

        Returns:
            int: egesz perceket leszamitva a masodpercek szama

        >>> Time(12)._ss()
        12
        >>> Time(72)._ss()
        12
        >>> Time(1234)._ss()
        34
        """
        seconds = self.to_seconds()
        return seconds % 60

    
    def _mm(self) -> int:
        """Visszaadja, hogy mennyit mutat a "percmutato"

        Returns:
            int: egesz orakat leszamitva az egesz percek szma

        >>> Time(12)._mm()
        0
        >>> Time(72)._mm()
        1
        >>> Time(1234)._mm()
        20
        """
        seconds = self.to_seconds()
        return seconds // 60

        
    
    def _hh(self) -> int:
        """Visszaadja, hogy mennyit mutat az "oramutato", amely sosem nullazodik.

        Returns:
            int: az egesz letelt orak szama, 24 fole is mehet
        
        >>> Time(12)._hh()
        0
        >>> Time(72)._hh()
        0
        >>> Time(1234)._hh()
        0
        >>> Time(3600)._hh()
        1
        >>> Time(12345)._hh()
        3
        """
        seconds = self.to_seconds()
        return seconds // 3600
    
    def pretty_format(self) -> str:
        """Visszaadja az idot szep modon
         - `s` vagy `ss` egy perc alatt
         - `m:ss` vagy `mm:ss` egy perc felett es egy ora alatt
         - `h:mm:ss` egy ora felett. (Az orak szama tetszolegesen nagy lehet)

        Returns:
            str: a szepen formazott ido

        >>> Time(12).pretty_format()
        '12'
        >>> Time(72).pretty_format()
        '1:12'
        >>> Time(3600).pretty_format()
        '1:00:00'
        >>> Time(12345).pretty_format()
        '3:25:45'
        >>> Time(123456).pretty_format()
        '34:17:36'
        """

        seconds = self.to_seconds()
        if seconds < 60:
            return "{}".format(self._ss())
        elif seconds >= 60 and seconds < 3600:
            minutes = self._mm()
            self.seconds -= (minutes * 60)
            seconds = str(self.seconds)
            if minutes != 0 and len(seconds) == 1:
                return "{}:{}{}".format(minutes,0,self.seconds)
            else:
                return "{}:{}".format(minutes,self.seconds)
        else:
            hours = self._hh()
            self.seconds -= hours * 3600
            minutes = self._mm()
            self.seconds -= minutes * 60
            hours = str(hours)
            minutes = str(minutes)
            seconds = str(self.seconds)
            if len(minutes) == 1:
                minutes = "{}{}".format(0,minutes)
            if len(seconds) == 1:
                seconds = "{}{}".format(0,seconds)
            return "{}:{}:{}".format(hours,minutes,seconds)

    def set_from_string(self, time:str) -> int:
        """Beallitja az idot egy string alapjan, melynek a formatuma olyan mint a `pretty_format` eseteben.

        Returns:
            int: a beallitott ido masodpercekben

        Args:
            time (str): az ido szoveg formaban
        
        >>> Time().set_from_string('12')
        12
        >>> Time().set_from_string('1:12')
        72
        >>> Time().set_from_string('1:00:00')
        3600
        >>> Time().set_from_string('3:25:45')
        12345
        >>> Time().set_from_string('111:01:23')
        399683
        """
        timelist = time.split(':') 
        if len(timelist) == 1:
            return int(timelist[0])
        if len(timelist) == 2:
            return int(timelist[0])*60 + int(timelist[1])
        if len(timelist) == 3:
            return int(timelist[0])*3600 + int(timelist[1]) * 60 + int(timelist[2])



                    
        
            


                
                


        

