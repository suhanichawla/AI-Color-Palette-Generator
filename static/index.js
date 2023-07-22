const form = document.querySelector("#form");
form.addEventListener("submit", async (e) => {
  e.preventDefault();
  let query = form.elements.query.value;
  let data = await fetch("/palette", {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: new URLSearchParams({
      query,
    }),
  });
  data = await data.json();
  console.log(data);
  const container = document.querySelector(".container");
  container.innerHTML = "";
  for (let color of data.colors) {
    const div = document.createElement("div");
    const span = document.createElement("span");
    div.classList.add("color");
    div.style.backgroundColor = color;
    div.style.width = `calc(100%/ ${data.colors.length})`;
    div.addEventListener("click", () => {
      navigator.clipboard.writeText(color);
    });

    span.innerText = color;
    div.appendChild(span);
    container.appendChild(div);
  }
});
