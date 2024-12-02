export async function showPokemon(pokemonId, pokeballElement, container) {
    const pokemonDisplay = document.getElementById('pokemon-display');
    const pokemonNameDisplay = document.getElementById('pokemon-name');
    const pokemonImage = document.getElementById('pokemon-image');
    const pokemonDescription = document.getElementById('pokemon-description');
  
    try {
      const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${pokemonId}`);
      const pokemonData = await response.json();
      const speciesResponse = await fetch(pokemonData.species.url);
      const speciesData = await speciesResponse.json();
  
      const descriptionEntry = speciesData.flavor_text_entries.find(
        (entry) => entry.language.name === 'en' || entry.language.name === 'pt'
      );
  
      pokemonNameDisplay.textContent = pokemonData.name.charAt(0).toUpperCase() + pokemonData.name.slice(1);
      pokemonImage.src = pokemonData.sprites.other['official-artwork'].front_default || pokemonData.sprites.front_default;
      pokemonDescription.textContent = descriptionEntry ? descriptionEntry.flavor_text.replace(/\n|\f/g, ' ') : 'Descrição não disponível.';
  
      pokeballElement.classList.add('large');
      setTimeout(() => {
        pokeballElement.classList.add('opened');
        pokemonDisplay.style.display = 'block';
      }, 500);
  
      document.addEventListener(
        'click',
        (event) => {
          if (!pokemonDisplay.contains(event.target) && !pokeballElement.contains(event.target)) {
            pokeballElement.classList.remove('large', 'opened');
            pokemonDisplay.style.display = 'none';
          }
        },
        { once: true }
      );
    } catch (error) {
      console.error('Erro ao buscar os dados do Pokémon:', error);
      alert('Não foi possível carregar os dados do Pokémon.');
    }
  }
  