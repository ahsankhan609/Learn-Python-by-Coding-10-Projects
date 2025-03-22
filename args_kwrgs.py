# https://youtu.be/JjHEhJqOimQ?si=Wjm_tUi2MOTtqKUc

# let's learn *args and **kwargs
# we can use any descriptive word for *args and **kwargs

def multiply(*numbers) -> float:
    total = 1
    for num in numbers:
        total *= num
    return total


# let's learn **kwargs

def user_info(**kwargs):
    for key, value in kwargs.items():
        return ", ".join(f"{key}: {value}" for key, value in kwargs.items())


if __name__ == '__main__':
    print(f"{multiply(1, 2, 8, 6, 85, 45):,.2f}")

    print(user_info(name="Essah", age=23, country="Nigeria", state="Lagos", education="Bachelors",
                    marital_status="Single"))
