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

# WSAImageScale

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

Options for the set of sizing values to apply to the Universal Windows
Platform logo and icon images. These options specify variations for different
screen sizes and resolutions.

A Universal Windows Platform application must specify [icon and logo
images](PlayerSettings.WSAImageType.html) as part of the package before you
can submit it to the Microsoft Store. Since these images are bitmaps, they do
not scale well on different display types. Because of this, applications
should include different versions of these images at different scales and
sizes so the icon/logo always displays correctly. Unity exposes two sets of
sizing values to use:

  * Scaling values: Indicates that an image asset is scaled by a certain factor from the base image size.
  * Target size: Indicates that the application icon is for a specific pixel size. This is only applicable for the Square44x44Logo type.

Target size assets are for surfaces that don't use the scaling plateau system:

  * Start jump list (desktop).
  * Start in the lower corner of the tile (desktop).
  * Shortcuts (desktop).
  * Control Panel (desktop).

For information on Universal Windows Platform application icons and logos, see
[Microsoft's documentation](https://docs.microsoft.com/en-
us/windows/uwp/design/style/app-icons-and-logos).  
**Important:** Unity writes image types to the package manifest when it builds
Universal Windows Platform for the first time. Building into an existing
Universal Windows Platform build folder does not update the package manifest
and does not apply any changes.

### Properties

[_100](PlayerSettings.WSAImageScale.100.html)| Uses a scale factor of 100%.  
---|---  
[_125](PlayerSettings.WSAImageScale.125.html)| Uses a scale factor of 125%.  
[_150](PlayerSettings.WSAImageScale.150.html)| Uses a scale factor of 150%.  
[_200](PlayerSettings.WSAImageScale.200.html)| Uses a scale factor of 200%.  
[_400](PlayerSettings.WSAImageScale.400.html)| Uses a scale factor of 400%.  
[Target16](PlayerSettings.WSAImageScale.Target16.html)| Targets a size of
16x16 pixels.  
[Target24](PlayerSettings.WSAImageScale.Target24.html)| Targets a size of
24x24 pixels.  
[Target32](PlayerSettings.WSAImageScale.Target32.html)| Targets a size of
32x32 pixels.  
[Target48](PlayerSettings.WSAImageScale.Target48.html)| Targets a size of
48x48 pixels.  
[Target256](PlayerSettings.WSAImageScale.Target256.html)| Targets a size of
256x256 pixels.  
  
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

