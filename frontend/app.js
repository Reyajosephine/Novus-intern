const apiUrl = "http://localhost:8000/query";
const questionInput = document.getElementById("question");
const runBtn = document.getElementById("run-btn");
const loading = document.getElementById("loading");
const sqlBlock = document.getElementById("sql-block");
const resultsTable = document.getElementById("results-table");
const resultsEmpty = document.getElementById("results-empty");
const statusBadge = document.getElementById("status-badge");
const confidence = document.getElementById("confidence");
const explanation = document.getElementById("explanation");

function setLoading(isLoading) {
  loading.style.display = isLoading ? "block" : "none";
  runBtn.disabled = isLoading;
}

function renderSQL(sql) {
  sqlBlock.textContent = sql || "";
}

function renderResults(data) {
  if (!data || data.length === 0) {
    resultsTable.innerHTML = "";
    resultsEmpty.textContent = "Fetching data...";
    return;
  }
  resultsEmpty.textContent = "";
  const headers = Object.keys(data[0]);
  let thead = "<tr>" + headers.map(h => `<th>${h}</th>`).join("") + "</tr>";
  let tbody = data.map(row =>
    "<tr>" + headers.map(h => `<td>${row[h]}</td>`).join("") + "</tr>"
  ).join("");
  resultsTable.innerHTML = `<thead>${thead}</thead><tbody>${tbody}</tbody>`;
}

function renderVerification(verification, data) {
  statusBadge.textContent = verification.status.charAt(0).toUpperCase() + verification.status.slice(1);
  statusBadge.className = "badge " + verification.status;
  confidence.textContent = `Confidence: ${verification.confidence.toFixed(2)}`;
  explanation.textContent = verification.reason;
  // Render relevant data table in verification panel
  const container = document.getElementById("verification-data-table-container");
  if (!data || data.length === 0) {
    container.innerHTML = "<div class='empty-state'>No relevant data.</div>";
    return;
  }
  const headers = Object.keys(data[0]);
  let thead = "<tr>" + headers.map(h => `<th>${h}</th>`).join("") + "</tr>";
  let tbody = data.map(row =>
    "<tr>" + headers.map(h => `<td>${row[h]}</td>`).join("") + "</tr>"
  ).join("");
  container.innerHTML = `<table class='verification-data-table'><thead>${thead}</thead><tbody>${tbody}</tbody></table>`;
}

function renderError(msg) {
  renderSQL("");
  renderResults([]);
  statusBadge.textContent = "Error";
  statusBadge.className = "badge invalid";
  confidence.textContent = "";
  explanation.textContent = msg;
}

runBtn.addEventListener("click", async () => {
  const question = questionInput.value.trim();
  if (!question) return;
  setLoading(true);
  renderSQL("");
  renderResults([]);
  statusBadge.textContent = "-";
  statusBadge.className = "badge";
  confidence.textContent = "";
  explanation.textContent = "";
  document.getElementById("verification-data-table-container").innerHTML = "";
  try {
    const res = await fetch(apiUrl, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question })
    });
    if (!res.ok) {
      const err = await res.json();
      throw new Error(err.detail || "Unknown error");
    }
    const { sql, data, verification } = await res.json();
    renderSQL(sql);
    renderResults(data);
    renderVerification(verification, data);
  } catch (e) {
    renderError(e.message);
  } finally {
    setLoading(false);
  }
});
