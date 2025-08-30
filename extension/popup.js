<<<<<<< HEAD
document.getElementById("removeBtn").addEventListener("click", async () => {
  const urlInput = document.getElementById("urlInput").value;
  if (!urlInput) return alert("Please enter an image URL");

  try {
    const res = await fetch("http://127.0.0.1:8000/remove_bg", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ url: urlInput })  // ✅ matches FastAPI model
    });

    if (!res.ok) throw new Error("Failed to process image");

    const blob = await res.blob();
    const outUrl = URL.createObjectURL(blob);

    document.getElementById("output").innerHTML = `<img src="${outUrl}" />`;

  } catch (err) {
    console.error(err);
    alert("Error removing background");
  }
});
=======
const params = new URLSearchParams(window.location.search);
const imgUrl = params.get("img");

if (imgUrl) {
  document.getElementById("container").innerHTML = `
    <img id="preview" src="${imgUrl}" width="300" /><br/>
    <button id="removeBgBtn">Remove Background</button>
    <button id="saveBtn">Save Original</button>
  `;

  // Remove Background button
  document.getElementById("removeBgBtn").onclick = async () => {
    try {
      const res = await fetch("http://127.0.0.1:8000/remove_bg", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url: imgUrl }) // ✅ matches backend
      });

      if (!res.ok) throw new Error("Server error");

      const blob = await res.blob();
      const outUrl = URL.createObjectURL(blob);

      document.getElementById("preview").src = outUrl;
    } catch (err) {
      alert("Failed: " + err.message);
    }
  };

  // Save original
  document.getElementById("saveBtn").onclick = () => {
    chrome.downloads.download({ url: imgUrl, saveAs: true });
  };
}
>>>>>>> origin/sam-backend
