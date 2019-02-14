from view.button import Button

# A subclass of Button, describing the buttons used to bet on a pocket
class PocketButton(Button):
    def __init__(self, x, y, width, height,
                 image_normal, image_hover,
                 image_down, pocketNumber):

        super().__init__(x, y, width, height,
                 image_normal, image_hover,
                 image_down)
        
        self.pocketNumber = pocketNumber

    def update_picture(self, model):
        if model.pocket == self.pocketNumber:
            self.image = self.image_down
        else:
            self.image = self.image_normal