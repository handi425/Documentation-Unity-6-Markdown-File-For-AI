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

# WSAImageType

enumeration

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

[Switch to Manual](../Manual/class-PlayerSettings.html "Go to PlayerSettings
Component in the Manual")

### Description

Options for the icon and logo image types that represent the application. For
example, images to display within the Microsoft Store, start menu, or taskbar.

A Universal Windows Platform application must specify [icon and logo
images](PlayerSettings.WSAImageType.html) as part of the package before you
can submit it to the Microsoft Store. Unity exposes a subset of these image
types through the Player Settings and automatically adds any set values to the
package manifest file it generates. You can add images and edit these images
later, either within Visual Studio or by directly editing the package manifest
file. To display the image, the device combines the image type value with an
[image scale](PlayerSettings.WSAImageScale.html) which allows multiple
versions of a given icon/logo to accommodate different screen sizes and
resolutions.  
  
Unity deliberately does not provide a complete set of default images, and the
application fails certification until you supply images. This ensures that you
do not submit your application to the Microsoft Store with placeholder images.  
These image types are Windows-specific and different from the [Splash Screen
setting](../Manual/class-PlayerSettingsSplashScreen.html), which displays
logos that run within the application.  
  
For information on Universal Windows Platform application icons and logos, see
[Microsoft's documentation](https://docs.microsoft.com/en-
us/windows/uwp/design/style/app-icons-and-logos).  
**Important:** Unity writes image types to the package manifest when it builds
Universal Windows Platform for the first time. Building into an existing
Universal Windows Platform build folder does not update the package manifest
and does not apply any changes.

### Properties

[PackageLogo](PlayerSettings.WSAImageType.PackageLogo.html)| The image that
represents your application within the Microsoft Store.  
---|---  
[SplashScreenImage](PlayerSettings.WSAImageType.SplashScreenImage.html)| The
image to display as the splash screen while the Universal Windows Platform
application opens.  
[UWPSquare44x44Logo](PlayerSettings.WSAImageType.UWPSquare44x44Logo.html)| The
image to display as the application icon within the start menu, taskbar, and
task manager.  
[UWPSquare71x71Logo](PlayerSettings.WSAImageType.UWPSquare71x71Logo.html)| The
image to display as the small tile in the start menu.  
[UWPSquare150x150Logo](PlayerSettings.WSAImageType.UWPSquare150x150Logo.html)|
The image to display as the medium tile in the start menu and Microsoft Store.  
[UWPSquare310x310Logo](PlayerSettings.WSAImageType.UWPSquare310x310Logo.html)|
The image to display as the large tile in the start menu and Microsoft Store.  
[UWPWide310x150Logo](PlayerSettings.WSAImageType.UWPWide310x150Logo.html)| The
image to display as the wide tile in the start menu and Microsoft Store.  
  
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

