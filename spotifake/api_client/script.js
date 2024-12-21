const apiBaseUrls = {
    albuns: "http://127.0.0.1:8000/albuns/",
    artistas: "http://127.0.0.1:8000/artistas/",
    musicas: "http://127.0.0.1:8000/musicas/",
};

document.addEventListener("DOMContentLoaded", () => {
    const fetchButton = document.getElementById("fetchItems");
    const artistaList = document.getElementById("artistaList");
    const albumList = document.getElementById("albumList");
    const musicaList = document.getElementById("musicaList");


    const createDeleteButton = (url, id, parentElement) => {
        const deleteButton = document.createElement("button");
        deleteButton.textContent = "Excluir";
        deleteButton.style.marginLeft = "10px";
        deleteButton.addEventListener("click", async () => {
            try {
                const response = await fetch(`${url}${id}/`, { method: "DELETE" });
                if (response.ok) {
                    parentElement.remove(); 
                } else {
                    console.error("Erro ao excluir:", response.statusText);
                }
            } catch (error) {
                console.error("Erro ao excluir:", error);
            }
        });
        return deleteButton;
    };

    fetchButton.addEventListener("click", async () => {
        try {
            const [albunsResponse, artistasResponse, musicasResponse] = await Promise.all([
                fetch(apiBaseUrls.albuns),
                fetch(apiBaseUrls.artistas),
                fetch(apiBaseUrls.musicas),
            ]);

            if (!albunsResponse.ok || !artistasResponse.ok || !musicasResponse.ok) {
                throw new Error("Erro ao buscar os dados");
            }

            const albuns = await albunsResponse.json();
            const artistas = await artistasResponse.json();
            const musicas = await musicasResponse.json();

  
            artistaList.innerHTML = "";
            albumList.innerHTML = "";
            musicaList.innerHTML = "";


            artistas.forEach((artista) => {
                const li = document.createElement("li");
                li.textContent = `${artista.nome} - Local: ${artista.local}, Ano de Criação: ${artista.ano_criacao}`;
                const deleteButton = createDeleteButton(apiBaseUrls.artistas, artista.id, li);
                li.appendChild(deleteButton);
                artistaList.appendChild(li);
            });


            albuns.forEach((album) => {
                const li = document.createElement("li");
                li.textContent = `Álbum: ${album.nome}, Ano: ${album.ano}, Artista: ${album.artista}`;
                const deleteButton = createDeleteButton(apiBaseUrls.albuns, album.id, li);
                li.appendChild(deleteButton);
                albumList.appendChild(li);
            });


            musicas.forEach((musica) => {
                const li = document.createElement("li");
                li.textContent = `Música: ${musica.nome}, Álbum: ${musica.album}, Duração: ${musica.segundos} segundos`;
                const deleteButton = createDeleteButton(apiBaseUrls.musicas, musica.id, li);
                li.appendChild(deleteButton);
                musicaList.appendChild(li);
            });
        } catch (error) {
            console.error("Erro:", error);
        }
    });
});
