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

# WSAApplicationShowName

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

Options for which [tile types](PlayerSettings.WSAImageType.html) to display
the application name on.

Tiles you exclude using the property do not display the application name and
only display the logo image. There are no options that include the
[small](PlayerSettings.WSAImageType.UWPSquare71x71Logo.html) tile size because
this size can't display the application name.  
**Note:** If you do not set logo images for the corresponding tiles
([medium](PlayerSettings.WSAImageType.UWPSquare150x150Logo.html),
[large](PlayerSettings.WSAImageType.UWPSquare310x310Logo.html), and
[wide](PlayerSettings.WSAImageType.UWPWide310x150Logo.html)), the platform
ignores the tiles and does not display the application name. **Important:**
Unity writes these settings to the package manifest when it builds Universal
Windows Platform for the first time. Building into an existing Universal
Windows Platform build folder does not update the package manifest and does
not apply any changes. Additional resources:
[tileShowName](PlayerSettings.WSA-tileShowName.html)

### Properties

[NotSet](PlayerSettings.WSAApplicationShowName.NotSet.html)| Indicates that
you have not set the application name and to use the default Universal Windows
Platform behavior.  
---|---  
[AllLogos](PlayerSettings.WSAApplicationShowName.AllLogos.html)| Displays the
application name on all tile sizes.  
[NoLogos](PlayerSettings.WSAApplicationShowName.NoLogos.html)| Doesn't display
the application name on any tile size.  
[StandardLogoOnly](PlayerSettings.WSAApplicationShowName.StandardLogoOnly.html)|
Displays the application name for medium and large tiles.  
[WideLogoOnly](PlayerSettings.WSAApplicationShowName.WideLogoOnly.html)|
Displays the application name for the wide tiles.  
  
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

