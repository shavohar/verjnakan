def upload_about_us(instance, filename):
    return f"pizzas/{instance.title}/{filename}"


def upload_why_choose_us(instance, filename):
    return f"why_choose_us/{instance.title}/{filename}"


def upload_chef(instance, filename):
    return f"chef/{instance.name}/{filename}"


def upload_user_images(instance, filename):
    return f"user/{instance.name}/{filename}"
