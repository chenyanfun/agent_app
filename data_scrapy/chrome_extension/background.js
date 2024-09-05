chrome.webRequest.onBeforeSendHeaders.addListener(
  function(details) {
    details.requestHeaders.push({
      "name": "Authorization",
      "value": "Bearer YOUR_ACCESS_TOKEN"
    },{
      "name": ":authority",
      "value": "acelab-dev-api.idiscoverdev.apps.jnj.com"
    },{
      "name": "Accept",
      "value": "application/json, text/plain, */*"
    },{
      "name": "Origin",
      "value": "https://acelab-dev.idiscoverdev.apps.jnj.com"
    },{
      "name": "Referer",
      "value": "https://acelab-dev.idiscoverdev.apps.jnj.com/"
    });
    return {requestHeaders: details.requestHeaders};
  },
  {urls: ["<all_urls>"]},
  ["blocking", "requestHeaders"]
);
