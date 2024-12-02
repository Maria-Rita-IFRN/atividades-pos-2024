import { showPokemon } from '/src/componets/pokemon-display';

export function createPokeballs(container) {
  for (let i = 1; i <= 151; i++) {
    const pokeball = document.createElement('div');
    pokeball.classList.add('pokeball');
    pokeball.dataset.pokemonId = i;

    pokeball.addEventListener('click', () => {
      showPokemon(i, pokeball, container);
    });

    container.appendChild(pokeball);
  }
}
