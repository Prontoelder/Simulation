def show_menu(
    title: str, options: dict[str, str], prompt: str = "Select action: "
) -> str:
    """Shows a menu with the given options."""
    print(f"\n{title}")
    for key, description in options.items():
        print(f"{key}. {description}")
    return input(prompt)


def show_main_menu() -> str:
    """Shows the main menu and returns the user's choice."""
    options = {
        "1": "Start automatic simulation",
        "2": "Start step-by-step simulation",
        "0": "Exit",
    }
    return show_menu("Menu:", options)


def show_step_menu() -> str:
    """Shows the step menu and returns the user's choice."""
    options = {
        "1": "Next turn (press Enter)",
        "2": "Stop simulation",
    }
    return show_menu("Select action:", options, "> ")


def show_pause_menu() -> str:
    """Shows the pause menu and returns the user's choice."""
    options = {
        "1": "Continue simulation",
        "2": "Stop simulation",
    }
    return show_menu("Pause:", options, "> ")
