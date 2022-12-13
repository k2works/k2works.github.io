(function () {
  "use strict";

  Office.onReady().then(function () {
    // TODO1: Assign handler to the OK button.
    document.getElementById("ok-button").onclick = sendStringToParentPage;
  });

  // TODO2: Create the OK button handler
  function sendStringToParentPage() {
    const userName = document.getElementById("name-box").value;
    Office.context.ui.messageParent(userName);
  }
})();
