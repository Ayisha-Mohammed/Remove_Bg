chrome.runtime.onInstalled.addListener(() => {
  chrome.contextMenus.create({
    id: "removeBg",
    title: "Remove Background",
    contexts: ["image"],
  });

  chrome.contextMenus.create({
    id: "saveNormal",
    title: "Save Normal Image",
    contexts: ["image"],
  });
});

chrome.contextMenus.onClicked.addListener((info, tab) => {
  if (info.menuItemId === "removeBg") {
    const imageUrl = info.srcUrl;
    if (imageUrl) {
      chrome.windows.create({
        url: `popup.html?img=${encodeURIComponent(imageUrl)}`,
        type: "popup",
        width: 600,
        height: 500,
      });
    }
  } else if (info.menuItemId === "saveNormal") {
    if (info.srcUrl) {
      chrome.downloads.download({ url: info.srcUrl, saveAs: true });
    }
  }
});
