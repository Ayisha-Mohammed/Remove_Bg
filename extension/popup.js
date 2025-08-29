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
