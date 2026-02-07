function countWords(text) {
    return (text || "").trim().split(/\s+/).filter(Boolean).length;
  }
  
  chrome.runtime.onMessage.addListener((msg, sender, sendResponse) => {
    if (msg?.type === "ANALYZE_PAGE") {
      const title = document.title;
      const url = location.href;
      const wordCount = countWords(document.body?.innerText);
  
      sendResponse({ title, url, wordCount });
    }
  });
  