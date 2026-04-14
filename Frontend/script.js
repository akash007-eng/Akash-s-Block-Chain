let storedHash = null;


// ✅ Upload File (CONNECTED TO BACKEND)
async function uploadFile() {

  const fileInput = document.getElementById("uploadFile");
  const status = document.getElementById("uploadStatus");
  const hashDisplay = document.getElementById("hashDisplay");

  if (!fileInput.files.length) {
    status.textContent = "❌ Select a file";
    status.style.color = "red";
    return;
  }

  const file = fileInput.files[0];

  const formData = new FormData();
  formData.append("file", file);

  const response = await fetch("http://127.0.0.1:5000/upload", {
    method: "POST",
    body: formData
  });

  const data = await response.json();

  if (data.error) {
    status.textContent = "❌ " + data.error;
    status.style.color = "red";
    return;
  }

  storedHash = data.hash;

  status.textContent = "✅ Stored in Blockchain";
  status.style.color = "green";

  hashDisplay.textContent = "Hash: " + storedHash;
}


// ✅ Verify File (CONNECTED TO BACKEND)
async function verifyFile() {

  const fileInput = document.getElementById("verifyFile");
  const status = document.getElementById("verifyStatus");

  if (!fileInput.files.length) {
    status.textContent = "❌ Select file";
    status.style.color = "red";
    return;
  }

  const file = fileInput.files[0];

  const formData = new FormData();
  formData.append("file", file);

  const response = await fetch("http://127.0.0.1:5000/verify", {
    method: "POST",
    body: formData
  });

  const data = await response.json();

  if (data.error) {
    status.textContent = "❌ " + data.error;
    status.style.color = "red";
    return;
  }

  if (data.status === "Authentic") {
    status.textContent = "✅ File is Authentic";
    status.style.color = "green";
  } else {
    status.textContent = "❌ File is Tampered";
    status.style.color = "red";
  }
}


// ✅ Download File (CONNECTED TO BACKEND - FIXED)
async function downloadFile() {

  const inputHash = document.getElementById("fileHash").value;
  const status = document.getElementById("downloadStatus");

  if (!inputHash) {
    status.textContent = "❌ Enter file hash";
    status.style.color = "red";
    return;
  }

  try {
    const response = await fetch("http://127.0.0.1:5000/download", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ hash: inputHash })
    });

    if (!response.ok) {
      const err = await response.json();
      status.textContent = "❌ " + (err.error || "Download failed");
      status.style.color = "red";
      return;
    }

    // Convert response to blob
    const blob = await response.blob();
    const url = window.URL.createObjectURL(blob);

    // Create download link
    const a = document.createElement("a");
    a.href = url;
    a.download = "downloaded_file";
    document.body.appendChild(a);
    a.click();
    a.remove();

    status.textContent = "✅ File downloaded successfully";
    status.style.color = "green";

  } catch (error) {
    status.textContent = "❌ Server error";
    status.style.color = "red";
  }
}