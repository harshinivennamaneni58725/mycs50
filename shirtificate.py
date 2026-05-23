from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # Setting font and title
        self.set_font("Helvetica", "B", 45)
        self.cell(0, 50, "CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")


def main():
    name = input("Name: ")
    generate_shirtificate(name)


def generate_shirtificate(name):
    # Instantiate portrait A4 PDF layout
    pdf = PDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # Place the t-shirt image horizontally centered
    pdf.image("shirtificate.png", x=15, y=70, w=180)

    # Configure styling for the text overlay on top of the shirt
    pdf.set_font("Helvetica", "B", 24)
    pdf.set_text_color(255, 255, 255)  # White text

    # Set text coordinate placement on top of the shirt image
    pdf.set_y(140)
    pdf.cell(0, 10, f"{name} took CS50", align="C")

    # Output file
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
