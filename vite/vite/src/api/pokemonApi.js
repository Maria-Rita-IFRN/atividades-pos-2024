export async function fetchPokemonData(pokemonId) {
    const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${pokemonId}`);
    return response.json();
}

export async function fetchPokemonSpecies(url) {
    const response = await fetch(url);
    return response.json();
}
