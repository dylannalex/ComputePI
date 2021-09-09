from screen import Screen
import colors


def main():
    # Settings
    circle_radius = 200
    screen_color = colors.BLACK
    circle_color = colors.ORANGE
    dot_color = colors.BLUE
    screen = Screen(circle_radius, screen_color, circle_color, dot_color)
    total_dots = 20_000

    # Compute PI
    screen.start_simulation(total_dots)
    print(f"PI is approximately: {screen.compute_pi()}")
    screen.wait(4000)


if __name__ == "__main__":
    main()
