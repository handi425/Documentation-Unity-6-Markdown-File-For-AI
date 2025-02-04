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

#  [PlayerSettings.WSA](PlayerSettings.WSA.html).GetTargetDeviceFamily

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

## Declaration

public static bool
GetTargetDeviceFamily([PlayerSettings.WSATargetFamily](PlayerSettings.WSATargetFamily.html)
family);

### Parameters

family |  [Device Family type](PlayerSettings.WSATargetFamily.html) to check.  
---|---  
  
### Returns

**bool** Returns true if the project targets the device family. Otherwise,
returns false.

### Description

Checks if your project targets the specified [device
family](PlayerSettings.WSATargetFamily.html).

In the Editor, Unity displays this as a list of checkboxes under **Supported
Device Families** in [UWP Player Settings](../Manual/class-
PlayerSettingsWSA.html). If you do not indicate that your Universal Windows
Platform application supports any device family type, it defaults to the
Windows.Universal family.  
**Important:** Unity writes these settings to the package manifest when it
builds Universal Windows Platform for the first time. Building into an
existing Universal Windows Platform build folder does not update the package
manifest and does not apply any changes.

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

