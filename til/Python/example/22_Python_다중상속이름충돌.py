class Tiger:
    def jump(self):
        print("호랑이점프")
    def cry(self):
        print("호랑이")

class Lion:
    def bite(self):
        print("사자 꿀꺽")
    def cry(self):
        print("사자")

class Liger(Tiger,Lion):
    def play(self):
        print("라이거와 놀기")
    def cry(self):
        print("라이거")

i=Liger()
i.play()
i.jump()
i.bite()
i.cry()