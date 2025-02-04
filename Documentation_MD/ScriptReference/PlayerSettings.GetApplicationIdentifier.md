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

#  [PlayerSettings](PlayerSettings.html).GetApplicationIdentifier

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

public static string
GetApplicationIdentifier([Build.NamedBuildTarget](Build.NamedBuildTarget.html)
buildTarget);

### Parameters

buildTarget | The [NamedBuildTarget](Build.NamedBuildTarget.html).  
---|---  
  
### Returns

**string** Returns the application identifier associated with a
[NamedBuildTarget](Build.NamedBuildTarget.html).

### Description

Get the application identifier for the specified platform.

The location of the application identifier in the build output depends on the
platform build target. On iOS, tvOS and Mac OS X platforms, the identifier is
written to the 'CFBundleIdentifier' field in the info.plist file. This file is
created and placed in the build output folder when the Unity project is built.
Additionally, on Mac OS X, the bundle identifier can be found in the
info.plist file in the final .app file, after finishing the Xcode build
process. On Android the identifier is saved to the 'package' field in the
AndroidManifest.xml file.

* * *

**Obsolete** Use GetApplicationIdentifier(NamedBuildTarget buildTarget)
instead.

## Declaration

public static string
GetApplicationIdentifier([BuildTargetGroup](BuildTargetGroup.html)
targetGroup);

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

