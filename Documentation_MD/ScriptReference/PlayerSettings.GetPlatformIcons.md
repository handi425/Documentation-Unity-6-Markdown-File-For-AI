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

#  [PlayerSettings](PlayerSettings.html).GetPlatformIcons

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

public static PlatformIcon[]
GetPlatformIcons([Build.NamedBuildTarget](Build.NamedBuildTarget.html)
buildTarget, [PlatformIconKind](PlatformIconKind.html) kind);

### Parameters

buildTarget | The [NamedBuildTarget](Build.NamedBuildTarget.html).  
---|---  
kind | Each platform supports a different set of [icon kinds](PlatformIconKind.html). These can be found in the specific platform namespace (for example [iOSPlatformIconKind](iOS.iOSPlatformIconKind.html).  
  
### Description

Gets the list of available icon slots for the specified build target and
[kind](PlatformIconKind.html).

If you use
[PlayerSettings.SetPlatformIcons](PlayerSettings.SetPlatformIcons.html) to set
icons, Unity needs to retrieve each icon's build target and [icon
kind](PlatformIconKind.html)."

* * *

**Obsolete** Use GetPlatformIcons(NamedBuildTarget , PlatformIconKind)
instead.

## Declaration

public static PlatformIcon[]
GetPlatformIcons([BuildTargetGroup](BuildTargetGroup.html) platform,
[PlatformIconKind](PlatformIconKind.html) kind);

### Parameters

platform | The full list of platforms that support this API and the supported icon kinds can be found in [icon kinds](PlatformIconKind.html).  
---|---  
kind | Each platform supports a different set of [icon kinds](PlatformIconKind.html). These can be found in the specific platform namespace (for example [iOSPlatformIconKind](iOS.iOSPlatformIconKind.html)).  
  
### Description

BuildTargetGroup is marked for deprecation in the future. Use
[NamedBuildTarget](Build.NamedBuildTarget.html) instead.

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

