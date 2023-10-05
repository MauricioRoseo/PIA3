(function () {
  const bsModal = new bootstrap.Modal(document.getElementById("modal"));

  document.body.addEventListener("htmx:afterSwap", (e) => {
    // Response targeting #dialog => show the modal
    if (e.detail.target.id == "dialog") {
      bsModal.show();
    }
  });
  document.body.addEventListener("htmx:beforeSwap", (e) => {
    // Empty response targeting #dialog => hide the modal
    if (e.detail.target.id == "dialog" && !e.detail.xhr.response) {
      bsModal.hide();
      e.detail.shouldSwap = false;
    }
  });
  document.body.addEventListener("closeModal", (e) => {
    bsModal.hide();
  });
  document.getElementById("modal").addEventListener("hidden.bs.modal", (e) => {
    // call your method
    document.getElementById("dialog").innerHTML = "";
    if (!document.getElementById("modal").classList.contains("no-reload")) {
      location.reload();
    }
  });
})();
