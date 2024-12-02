import { showPokemon } from '/src/componets/pokemon-display';

const pokeballContainer = document.getElementById('pokeball-container');

function createPokeballs() {
    for (let i = 1; i <= 151; i++) {
        const pokeball = document.createElement('div');
        pokeball.classList.add('pokeball');
        pokeball.dataset.pokemonId = i;

        pokeball.addEventListener('click', () => {
            showPokemon(i, pokeball);
        });

        pokeballContainer.appendChild(pokeball);
    }
}

createPokeballs();
