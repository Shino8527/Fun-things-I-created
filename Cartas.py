class Cartas:
    def __init__(self):
        self.naipe= 0
        #Copas: ♡
        #Ouros: ♢
        #Paus: ♧
        #Espadas: ♤
        self.nr= 0
        #1 a 10 ou "rei", "dama", "valete", "joker"

    def set_carta(self, naipe, nr):
        self.naipe= naipe
        self.nr= nr

    def comparar_semelhanca_carta(self, carta, o_q_comparar):
        if o_q_comparar == "naipe" or o_q_comparar == "nr":
            carta_compare= getattr(carta,o_q_comparar)
            self_compare= getattr(self,o_q_comparar)
            if carta_compare == self_compare:
                return True
            else:
                return False