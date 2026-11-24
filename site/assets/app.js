// Gypsos Loutraki: menu and the quote form (POST /api/lead through the site's Worker; WhatsApp, Viber and email as fallbacks).
(function () {
  var en = document.documentElement.lang === "en";
  var WA = "306906838669";
  var EMAIL = "info@handyman24.com";

  // menu: close on link click, outside tap or Escape
  var menu = document.querySelector(".dd");
  if (menu) {
    menu.addEventListener("click", function (e) { if (e.target.closest(".dd-p a")) menu.open = false; });
    document.addEventListener("click", function (e) { if (menu.open && !menu.contains(e.target)) menu.open = false; });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") menu.open = false; });
  }

  document.querySelectorAll(".lf").forEach(function (form) {
    var res = form.querySelector(".lf-res");
    var btn = form.querySelector("button[type=submit]");
    var L = en
      ? { name: "Name", phone: "Phone", area: "Area", type: "Work", msg: "Message",
          need: "Please fill in your name and phone.", sending: "Sending…",
          ok: "Thank you! We received your request and will call you soon.",
          fail: "The form could not be sent right now. Please send the same message with one tap:", hi: "Hello, I would like a quote for drywall work." }
      : { name: "Όνομα", phone: "Τηλέφωνο", area: "Περιοχή", type: "Εργασία", msg: "Μήνυμα",
          need: "Συμπληρώστε όνομα και τηλέφωνο.", sending: "Αποστολή…",
          ok: "Ευχαριστούμε! Λάβαμε το αίτημά σας και θα σας καλέσουμε σύντομα.",
          fail: "Η αποστολή δεν έγινε αυτή τη στιγμή. Στείλτε το ίδιο μήνυμα με ένα πάτημα:", hi: "Γεια σας, θα ήθελα προσφορά για εργασίες γυψοσανίδας." };
    function val(n) { var el = form.elements[n]; return String((el || {}).value || "").trim(); }
    function text() {
      var lines = [L.hi];
      ["name", "phone", "area", "type", "msg"].forEach(function (k) { if (val(k)) lines.push(L[k] + ": " + val(k)); });
      return lines.join("\n");
    }
    function link(via) {
      var t = encodeURIComponent(text());
      if (via === "wa") return "https://wa.me/" + WA + "?text=" + t;
      if (via === "viber") return "viber://chat?number=%2B" + WA + "&draft=" + t;
      return "mailto:" + EMAIL + "?subject=" + encodeURIComponent(en ? "Drywall quote request" : "Αίτημα προσφοράς γυψοσανίδας") + "&body=" + t;
    }
    function say(html, err) { res.hidden = false; res.className = "lf-res" + (err ? " err" : ""); res.innerHTML = html; }
    form.querySelectorAll("[data-via]").forEach(function (b) {
      b.addEventListener("click", function () { window.location.href = link(b.dataset.via); });
    });
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!val("name") || !val("phone")) { say("<p>" + L.need + "</p>", true); return; }
      var d = new FormData();
      // keys are the labels the owner reads in the email (worker.js expects Όνομα and Τηλέφωνο)
      d.append("Όνομα", val("name"));
      d.append("Τηλέφωνο", val("phone"));
      if (val("area")) d.append("Περιοχή", val("area"));
      if (val("type")) d.append("Εργασία", val("type"));
      if (val("msg")) d.append("Μήνυμα", val("msg"));
      d.append("Γλώσσα", en ? "English" : "Ελληνικά");
      d.append("Σελίδα", location.href);
      d.append("_honey", val("_honey"));
      btn.disabled = true;
      var old = btn.innerHTML;
      btn.textContent = L.sending;
      fetch("/api/lead", { method: "POST", body: d })
        .then(function (r) { return r.json().catch(function () { return {}; }).then(function (j) { if (!r.ok || !j.success) throw 0; }); })
        .then(function () { say("<p>" + L.ok + "</p>"); form.reset(); })
        .catch(function () {
          say("<p>" + L.fail + "</p><a class=\"btn btn-sm\" href=\"" + link("wa") + "\">WhatsApp</a>" +
              "<a class=\"btn btn-sm btn-ghost\" href=\"" + link("viber") + "\">Viber</a>" +
              "<a class=\"btn btn-sm btn-ghost\" href=\"" + link("mail") + "\">Email</a>", true);
        })
        .then(function () { btn.disabled = false; btn.innerHTML = old; });
    });
  });
})();
