[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/android-RequestingPermissions.html)
  * [中文](/cn/current/Manual/android-RequestingPermissions.html)
  * [日本語](/ja/current/Manual/android-RequestingPermissions.html)
  * [한국어](/kr/current/Manual/android-RequestingPermissions.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/android-RequestingPermissions.html)
  * [中文](/cn/current/Manual/android-RequestingPermissions.html)
  * [日本語](/ja/current/Manual/android-RequestingPermissions.html)
  * [한국어](/kr/current/Manual/android-RequestingPermissions.html)

  * [Platform development ](PlatformSpecific.html)
  * [Android](android.html)
  * [Developing for Android](android-developing.html)
  * [Device features and permissions](android-device-features-and-permissions.html)
  * Request runtime permissions

[](android-permissions-declare.html)

Declare permissions for an application

[](android-handle-crashes.html)

Handle Android crashes

# Request runtime permissions

This page explains how to request the user’s permission for your application
to access data on the device or use a device feature such as a built-in camera
or microphone.

Google’s guideline for requesting permissions recommends that, if the user
denies a permission request once, you should display the reason for the
request and present the request again.

For more information on when and how to request permissions on an Android
device, refer to [App permissions best
practices](https://developer.android.com/training/permissions/usage-notes) in
the Android developer guide.

## Prerequisites

The runtime permissions API requires Android version 6 (API level 23). To
change your application’s target API:

  1. Select **Edit** > **Project Settings**.
  2. In the Project settings window, select the **Player** tab, then open [Android Player Settings](class-PlayerSettingsAndroid.html):  
![](../uploads/Main/android-player-settings-tab.png)

  3. In the **Other Settings** > **Identification** section, set **Target API Level** to at least level 23.

Before the application requests permission to use restricted data or a
particular device feature, it must declare the permission in its [Android App
Manifest](android-manifest.html). For more information, refer to [Declare
permissions for an application](android-permissions-declare.html).

## Request permission at runtime

The [Android.Permission](../ScriptReference/Android.Permission.html) API
provides functionality that you can use to check what permissions the
application currently has and request permissions that the application
requires but doesn’t have.

An overview of the process to request permission at runtime is as follows:

  1. Check whether the user has already granted the application permission. If they have, you don’t need to request it again.
  2. If the user hasn’t granted the permission, check if you need to display the rationale for requesting the permission. If the rationale isn’t necessary, directly send a request for permission to access the data or use the device feature that the application requires.
  3. If the user denies the application permission, disable the application’s functionality that requires the specific permission. If the application can’t work without this functionality, inform the user.
  4. If the user still denies the application permission, it’s best practice to provide a method that lets the user manually trigger the permission request again from inside the application.

### Check if the application has permission

Use
[Permission.HasUserAuthorizedPermission](../ScriptReference/Android.Permission.HasUserAuthorizedPermission.html)
to check if the user has already granted permission for the data or feature
the application requires.

For a code example that shows how to use this API, refer to
[Permission.HasUserAuthorizedPermission](../ScriptReference/Android.Permission.HasUserAuthorizedPermission.html).

### Check whether to display the rationale for permission request

Use
[Permission.ShouldShowRequestPermissionRationale](../ScriptReference/Android.Permission.ShouldShowRequestPermissionRationale.html)
to check whether you need to display the rationale for a specific permission
request.

If the rationale is necessary, display a message with reason why your
application requires access to specific device features. After you display the
message, send a request for permission.

If the rationale isn’t necessary, directly proceed to send a request for
permission.

For a code example that shows how to use this API, refer to
[Permission.ShouldShowRequestPermissionRationale](../ScriptReference/Android.Permission.ShouldShowRequestPermissionRationale.html).

### Send a request for permission

Use
[Permission.RequestUserPermission](../ScriptReference/Android.Permission.RequestUserPermission.html)
to request permission to use the data or feature. When you call this method,
Android opens the system permission dialog that the user can use to grant or
deny the permission.

For a code example that shows how to use this API, refer to
[Permission.RequestUserPermission](../ScriptReference/Android.Permission.RequestUserPermission.html).

Use
[Permission.RequestUserPermissions](../ScriptReference/Android.Permission.RequestUserPermissions.html)
to request permissions to access multiple resources on the user’s device at
once. This method uses an array of strings with each string representing a
specific permission to access a particular resource such as the device’s
camera , microphone, or location.

These methods can accept a [PermissionCallbacks
object](../ScriptReference/Android.PermissionCallbacks.html) that you can use
to specify code to run after the user grants or denies the permission. You can
use this to start using a device feature as soon as the user grants the
permission request. For example, you can start recording from the microphone.

**Tip** : When you request permission, it’s best practice to show the user a
message that explains why the application requires the feature.

**Note** : If the user has enabled the **Do not ask me again** option on the
system permission dialog, or has denied the permission more than once,
`RequestUserPermission()` doesn’t open the system dialog. In this case, the
user must go into the application permission settings and manually enable the
permission.

### Provide a way to manually trigger the permission request

If the user denies the permission that the application requires, provide a way
for the user to manually display the permission request dialog. How to do this
depends on the application, but one solution is to provide a button that calls
[Permission.RequestUserPermission](../ScriptReference/Android.Permission.RequestUserPermission.html).

[](android-permissions-declare.html)

Declare permissions for an application

[](android-handle-crashes.html)

Handle Android crashes

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

