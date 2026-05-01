/* Minimal frontend auth helper skeleton. Adapt storage keys and permission source per project. */
(function attachFrontendAuth(global) {
  var rolePermissions = {
    admin: ["page.*", "action.*"],
    user: []
  };

  function normalizeToken(token) {
    return String(token || "").replace(/^Bearer\s+/i, "").trim();
  }

  function readUser() {
    try {
      return JSON.parse(global.localStorage.getItem("current_user") || "null") || {};
    } catch (error) {
      return {};
    }
  }

  function getPermissionSet(user) {
    var explicit = Array.isArray(user.permissions) ? user.permissions : [];
    var role = user.role || "user";
    var inherited = rolePermissions[role] || [];
    return explicit.concat(inherited);
  }

  function matchPermission(granted, wanted) {
    return granted === wanted || granted === "page.*" && wanted.indexOf("page.") === 0 || granted === "action.*" && wanted.indexOf("action.") === 0;
  }

  function hasPermission(wanted) {
    var user = readUser();
    return getPermissionSet(user).some(function canUse(granted) {
      return matchPermission(granted, wanted);
    });
  }

  global.FrontendAuth = {
    getActiveUser: readUser,
    getActiveAuthToken: function getActiveAuthToken() {
      return normalizeToken(global.localStorage.getItem("auth_token") || global.localStorage.getItem("token"));
    },
    isAuthenticated: function isAuthenticated() {
      return Boolean(this.getActiveAuthToken());
    },
    canAccess: hasPermission,
    canPerform: hasPermission,
    requirePage: function requirePage(permissionKey, options) {
      var config = options || {};
      if (hasPermission(permissionKey)) return true;
      if (config.redirectTo) global.location.href = config.redirectTo;
      return false;
    },
    guardAction: function guardAction(permissionKey, callback) {
      if (!hasPermission(permissionKey)) {
        global.alert("No permission for this action.");
        return false;
      }
      callback();
      return true;
    }
  };
})(window);
