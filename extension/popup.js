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
