async function getActiveTab() {
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    return tab;
  }
  
  document.getElementById("analyze").addEventListener("click", async () => {
    const status = document.getElementById("status");
    status.textContent = "Calling backend…";
  
    try {
      const res = await fetch("http://localhost:4000/", { method: "GET" });
      const text = await res.text();
  
      status.textContent = `Backend replied (${res.status}): ${text}`;
    } catch (e) {
      status.textContent = `Backend error: ${e.message}`;
    }
  });
  
  