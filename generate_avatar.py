from avatar_generator import AvatarGenerator


def generate_avatar():
    generator = AvatarGenerator("./images")
    generator.generate_avatar(500)


# name of script so if user invoked this file directly then we call function
if __name__ == "__main__":
    generate_avatar()
