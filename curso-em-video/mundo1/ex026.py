# Faça um programa que leia uma frase pelo teclado e mostre:
# 1. Quantas vezes aparece a letra "A"
# 2. Em que posição ela aparece a primeira vez
# 3. Em que posição ela aparece a última vez


def get_phrase(prompt: str) -> str:
    while True:
        phrase = input(prompt).strip()

        if not phrase:
            print("Phrase cannot be empty.")
            continue

        return phrase.upper()


def analyze_letter_a(phrase: str) -> tuple[int, int, int]:
    count = phrase.count("A")
    first = phrase.find("A")
    last = phrase.rfind("A")

    if first != -1:
        first += 1
        last += 1

    return count, first, last


def main() -> None:
    phrase = get_phrase("Enter a phrase: ")

    count, first, last = analyze_letter_a(phrase)

    print(f"The letter 'A' appears {count} times in the sentence.\n"
          f"The first letter 'A' appeared at position {first}.\n"
          f"The last letter 'A' appeared at position {last}.")

if __name__ == "__main__":
    main()
