from view.button import Button

# A subclass of Button, describing the buttons used to bet on a pocket
class BetButton(Button):
    def __init__(self, x, y, width, height, 
                 image_normal, image_hover,
                 image_down, betValue):

        super().__init__(x, y, width, height,
                 image_normal, image_hover,
                 image_down)
        
        self.betValue = betValue

    def update_picture(self, model):
        if model.bet == self.betValue:
            self.image = self.image_down
        else:
            self.image = self.image_normal