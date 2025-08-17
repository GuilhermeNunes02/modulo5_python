

import emoji

# Lista de emojis disponíveis
print("Emojis disponíveis:")
print("❤️  - :red_heart:")
print("👍  - :thumbs_up:")
print("🤔  - :thinking_face:")
print("🥳  - :partying_face:")

# Solicita uma frase com códigos de emoji
frase = input("\nDigite uma frase e ela será emojizada:\n")

# Converte os códigos para emojis
frase_emojizada = emoji.emojize(frase, language='alias')

# Exibe resultado
print("\nFrase emojizada:")
print(frase_emojizada)
