const params = new URLSearchParams(window.location.search);
const imgUrl = params.get("img");

const preview = document.getElementById("preview");
const removeBgBtn = document.getElementById("removeBgBtn");
const downloadBtn = document.getElementById("downloadBtn");

let processedUrl = null; // store background-removed image URL

if (imgUrl) {
  preview.src = imgUrl;
  preview.style.display = "block";
}

// Remove Background
removeBgBtn.onclick = async () => {
  try {
    const res = await fetch("http://127.0.0.1:8000/remove_bg", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ url: imgUrl })
    });

    if (!res.ok) throw new Error("Server error");

    const blob = await res.blob();
    processedUrl = URL.createObjectURL(blob);

    preview.src = processedUrl;
  } catch (err) {
    alert("Failed: " + err.message);
  }
};

// Download processed image
downloadBtn.onclick = () => {
  const urlToDownload = processedUrl || imgUrl; // download processed if available
  chrome.downloads.download({ url: urlToDownload, saveAs: true });
};

