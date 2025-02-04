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

#  [SystemInfo](SystemInfo.html).deviceUniqueIdentifier

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

public static string deviceUniqueIdentifier;

### Description

A unique device identifier. It's guaranteed to be unique for every device
(Read Only).

**iOS** : Uses [UIDevice.identifierForVendor
](https://developer.apple.com/documentation/uikit/uidevice/1620059-identifierforvendor)
to generate a unique device identifier.  
  
**macOS** : Uses
[kIOPlatformUUIDKey](https://developer.apple.com/documentation/iokit/kioplatformuuidkey)
to generate a unique device identifier.  
  
**Android:** [SystemInfo.deviceUniqueIdentifier](SystemInfo-
deviceUniqueIdentifier.html) always returns the md5 of ANDROID_ID. (See
<https://developer.android.com/reference/android/provider/Settings.Secure.html#ANDROID_ID>).
Note that since Android 8.0 (API level 26) ANDROID_ID depends on the app
signing key. That means "unsigned" builds (which are by default signed with a
debug keystore) will have a **different value** than signed builds (which are
signed with a key provided in the player settings). Also when [allowing Google
Play to sign your app](https://developer.android.com/studio/publish/app-
signing#app-signing-google-play), this value will be different when testing
locally built app which is signed with the upload key and app downloaded from
the Google Play which will be signed with the "final" key.  
  
**Windows Store Apps** : uses AdvertisingManager::AdvertisingId for returning
unique device identifier, if option in 'PC Settings -> Privacy -> Let apps use
my advertising ID for experiences across apps (turning this off will reset
your ID)' is disabled, Unity will fallback to
HardwareIdentification::GetPackageSpecificToken().Id.  
  
**Windows Standalone** : returns a hash from the concatenation of strings
taken from **Computer System Hardware Classes**
(https://msdn.microsoft.com/en-
us/library/windows/desktop/aa389273(v=vs.85).aspx):  
Win32_BaseBoard::SerialNumber  
Win32_BIOS::SerialNumber  
Win32_Processor::UniqueId  
Win32_DiskDrive::SerialNumber  
Win32_OperatingSystem::SerialNumber  
  
Will return [SystemInfo.unsupportedIdentifier](SystemInfo-
unsupportedIdentifier.html) on platforms which don't support this property.

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

