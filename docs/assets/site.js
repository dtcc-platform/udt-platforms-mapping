(function () {
  function cellValue(row, index) {
    var cell = row.children[index];
    return cell ? cell.textContent.trim() : "";
  }

  function compareValues(a, b) {
    var aNumber = Number(a.replace(/,/g, ""));
    var bNumber = Number(b.replace(/,/g, ""));

    if (a !== "" && b !== "" && !Number.isNaN(aNumber) && !Number.isNaN(bNumber)) {
      return aNumber - bNumber;
    }

    return a.localeCompare(b, undefined, { numeric: true, sensitivity: "base" });
  }

  function enhanceTable(table, index) {
    var thead = table.tHead;
    var tbody = table.tBodies[0];

    if (!thead || !tbody || !thead.rows.length || !tbody.rows.length) {
      return;
    }

    var headers = Array.prototype.slice.call(thead.rows[0].cells);
    if (!headers.length) {
      return;
    }

    var wrapper = document.createElement("div");
    wrapper.className = "table-tools";

    var label = document.createElement("label");
    label.className = "table-filter";

    var labelText = document.createElement("span");
    labelText.textContent = "Filter table";

    var input = document.createElement("input");
    input.type = "search";
    input.placeholder = "Type to filter rows";
    input.setAttribute("aria-label", "Filter table " + (index + 1));

    label.append(labelText, input);
    wrapper.appendChild(label);
    table.parentNode.insertBefore(wrapper, table);

    input.addEventListener("input", function () {
      var query = input.value.trim().toLowerCase();
      Array.prototype.forEach.call(tbody.rows, function (row) {
        row.hidden = query !== "" && !row.textContent.toLowerCase().includes(query);
      });
    });

    headers.forEach(function (header, columnIndex) {
      var button = document.createElement("button");
      button.type = "button";
      button.className = "table-sort";
      button.textContent = header.textContent.trim() || "Column " + (columnIndex + 1);
      button.setAttribute("aria-label", "Sort by " + button.textContent);

      header.textContent = "";
      header.appendChild(button);

      button.addEventListener("click", function () {
        var currentDirection = header.dataset.sortDirection === "asc" ? "desc" : "asc";
        var rows = Array.prototype.slice.call(tbody.rows);

        headers.forEach(function (otherHeader) {
          delete otherHeader.dataset.sortDirection;
        });
        header.dataset.sortDirection = currentDirection;

        rows.sort(function (left, right) {
          var comparison = compareValues(cellValue(left, columnIndex), cellValue(right, columnIndex));
          return currentDirection === "asc" ? comparison : -comparison;
        });

        rows.forEach(function (row) {
          tbody.appendChild(row);
        });
      });
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    Array.prototype.forEach.call(document.querySelectorAll("table"), enhanceTable);
  });
})();
