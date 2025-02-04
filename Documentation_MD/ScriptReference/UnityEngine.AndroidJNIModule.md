[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

# UnityEngine.AndroidJNIModule

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[ ]()

### Description

AndroidJNI module allows you to call Java code.

### Classes

[AndroidApplication](Android.AndroidApplication.html)| Use this class to
access the runtime data of your Android application.  
---|---  
[AndroidAssetPackInfo](Android.AndroidAssetPackInfo.html)| Represents the
download progress of a single Android asset pack.  
[AndroidAssetPacks](Android.AndroidAssetPacks.html)| Provides methods for
handling Android asset packs.  
[AndroidAssetPackState](Android.AndroidAssetPackState.html)| Represents the
state of a single Android asset pack.  
[AndroidAssetPackUseMobileDataRequestResult](Android.AndroidAssetPackUseMobileDataRequestResult.html)|
Represents the choice of an end user that indicates if your application can
use mobile data to download Android asset packs.  
[AndroidConfiguration](Android.AndroidConfiguration.html)| Use this class to
retrieve device specific configuration information.  
[AndroidDevice](Android.AndroidDevice.html)| Interface into Android specific
functionality.  
[AndroidGame](Android.AndroidGame.html)| Provides methods and properties for
accessing different Android game APIs.  
[AndroidJavaClass](AndroidJavaClass.html)| AndroidJavaClass is the Unity
representation of a generic instance of java.lang.Class.  
[AndroidJavaObject](AndroidJavaObject.html)| AndroidJavaObject is the Unity
representation of a generic instance of java.lang.Object.  
[AndroidJavaProxy](AndroidJavaProxy.html)| This class can be used to implement
any java interface. Any java vm method invocation matching the interface on
the proxy object will automatically be passed to the c# implementation.  
[AndroidJNI](AndroidJNI.html)| 'Raw' JNI interface to Android Java VM from
Unity scripting (C#).Note: Using raw JNI functions requires advanced knowledge
of the Android Java Native Interface (JNI). Please take note.  
[AndroidJNIHelper](AndroidJNIHelper.html)| Helper interface for JNI
interaction; signature creation and method lookups.Note: Using raw JNI
functions requires advanced knowledge of the Android Java Native Interface
(JNI). Please take note.  
[AndroidLocale](Android.AndroidLocale.html)| Use this class to retrieve the
language and region preferences set on the device.  
[ApplicationExitInfoProvider](Android.ApplicationExitInfoProvider.html)|
Access point to get the list of ApplicationExitInfo records with the reasons
for the most recent application terminations.  
[DiagnosticsReporting](Android.DiagnosticsReporting.html)| Class with options
for reporting diagnostics information to the Android system.  
[DownloadAssetPackAsyncOperation](Android.DownloadAssetPackAsyncOperation.html)|
Represents an asynchronous Android asset pack download operation.
AndroidAssetPacks.DownloadAssetPackAsync returns an instance of this class.  
[GetAssetPackStateAsyncOperation](Android.GetAssetPackStateAsyncOperation.html)|
Represents an asynchronous Android asset pack state request operation.
AndroidAssetPacks.GetAssetPackStateAsync returns an instance of this class.  
[PermissionCallbacks](Android.PermissionCallbacks.html)| Contains callbacks
invoked when permission request is executed using
Permission.RequestUserPermission.  
[RequestToUseMobileDataAsyncOperation](Android.RequestToUseMobileDataAsyncOperation.html)|
Represents an asynchronous operation that requests to use mobile data to
download Android asset packs.  
  
### Structs

[JNINativeMethod](JNINativeMethod.html)| Defines a single method to
beregistered using AndroidJNI.RegisterNatives.  
---|---  
[Permission](Android.Permission.html)| Structure describing a permission that
requires user authorization.  
  
### Enumerations

[AndroidAssetPackError](Android.AndroidAssetPackError.html)| Values that
indicate the type of Android asset pack error when the status is either
AndroidAssetPackStatus.Failed or AndroidAssetPackStatus.Unknown.  
---|---  
[AndroidAssetPackStatus](Android.AndroidAssetPackStatus.html)| Values that
indicate the status of an Android asset pack.  
[AndroidColorModeHdr](Android.AndroidColorModeHdr.html)| Options to indicate
whether the screen can display a wide range brightness levels.  
[AndroidColorModeWideColorGamut](Android.AndroidColorModeWideColorGamut.html)|
Options to indicate whether the screen can display wide range of color gamut
or not.  
[AndroidGameMode](Android.AndroidGameMode.html)| Options for the available
game modes that AndroidGame.GameMode can return.  
[AndroidGameState](Android.AndroidGameState.html)| Options for the available
game states that you can pass to AndroidGame.SetGameState or you can set as a
current game state mode to be used for Automated game state hinting in Unity
using AndroidGame.Automatic.SetGameState method.  
[AndroidHardwareKeyboardHidden](Android.AndroidHardwareKeyboardHidden.html)|
Options to indicate whether the physical keyboard is available.  
[AndroidHardwareType](Android.AndroidHardwareType.html)| AndroidHardwareType
describes the type of Android device on which the app is running.  
[AndroidKeyboard](Android.AndroidKeyboard.html)| Options to indicate the type
of keyboard the device is using.  
[AndroidKeyboardHidden](Android.AndroidKeyboardHidden.html)| Options to
indicate whether any keyboard is available for use on the device.  
[AndroidNavigation](Android.AndroidNavigation.html)| Options to indicate the
type of navigation methods used on the device.  
[AndroidNavigationHidden](Android.AndroidNavigationHidden.html)| Options to
indicate whether the 5-way or DPAD navigation methods are available on the
device.  
[AndroidOrientation](Android.AndroidOrientation.html)| Options to indicate the
orientation of the screen.  
[AndroidScreenLayoutDirection](Android.AndroidScreenLayoutDirection.html)|
Options to indicate the screen layout direction.  
[AndroidScreenLayoutLong](Android.AndroidScreenLayoutLong.html)| Options to
indicate whether the aspect ratio of the screen is taller or wider than
normal.  
[AndroidScreenLayoutRound](Android.AndroidScreenLayoutRound.html)| Options to
indicate whether the screen shape is rounded or not.  
[AndroidScreenLayoutSize](Android.AndroidScreenLayoutSize.html)| Options to
indicate the size of the device screen.  
[AndroidTouchScreen](Android.AndroidTouchScreen.html)| Options to indicate
whether the device supports touchscreen.  
[AndroidUIModeNight](Android.AndroidUIModeNight.html)| Options to indicate
whether the device screen is in a special mode, such as a night mode.  
[AndroidUIModeType](Android.AndroidUIModeType.html)| Options to indicate the
user interface mode of the device.  
[ExitReason](Android.ExitReason.html)| The reason code for termination of the
process.  
[ProcessImportance](Android.ProcessImportance.html)| Indicates the relative
importance level that the system assigns to the process. These levels are
represented by constants. The constants are numbered in such a way that more
important values are always smaller than the less important values.  
  
Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

