const params = new URLSearchParams(window.location.search);
const imgUrl = params.get("img");

const preview = document.getElementById("preview");
const processed = document.getElementById("processed");
const removeBgBtn = document.getElementById("removeBgBtn");
const downloadBtn = document.getElementById("downloadBtn");
const loading = document.getElementById("loading");
const processedBox = document.getElementById("processed-box");

let processedUrl = null;

if (imgUrl) preview.src = imgUrl;

// Remove BG
removeBgBtn.onclick = async () => {
  try {
    loading.hidden = false;
    removeBgBtn.disabled = true;

    const res = await fetch("http://127.0.0.1:8000/remove_bg", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ url: imgUrl })
    });

    if (!res.ok) throw new Error("Server error");

    const blob = await res.blob();
    processedUrl = URL.createObjectURL(blob);
    processed.src = processedUrl;

    // Reveal processed card
    processedBox.setAttribute("aria-hidden", "false");
    downloadBtn.disabled = false;

  } catch (e) {
    alert("Failed: " + e.message);
  } finally {
    loading.hidden = true;
    removeBgBtn.disabled = false;
  }
};

// Download
downloadBtn.onclick = () => {
  const urlToDownload = processedUrl || imgUrl;
  chrome.downloads.download({ url: urlToDownload, saveAs: true });
};
