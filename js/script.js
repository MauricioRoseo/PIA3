// script.js

// Selecionando elementos do DOM
const postForm = document.querySelector(".container");
const modal = document.querySelector(".modal");
const openModalButton = document.querySelector(".open-modal");
const closeModalButton = document.querySelector(".close-modal");

// Função para abrir a janela modal
function openModal() {
  modal.style.display = "block";
}

// Função para fechar a janela modal
function closeModal() {
  modal.style.display = "none";
}

// Evento para abrir a janela modal quando o botão for clicado
openModalButton.addEventListener("click", openModal);

// Evento para fechar a janela modal quando o botão de fechar for clicado
closeModalButton.addEventListener("click", closeModal);

// Evento para fechar a janela modal se o usuário clicar fora dela
window.addEventListener("click", (event) => {
  if (event.target === modal) {
    closeModal();
  }
});
