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

#  [BuildProfile](Build.Profile.BuildProfile.html).SetActiveBuildProfile

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

## Declaration

public static void
SetActiveBuildProfile([Build.Profile.BuildProfile](Build.Profile.BuildProfile.html)
buildProfile);

### Parameters

buildProfile | The build profile to be set as the active build profile. When the value is null, Unity sets the classic platform as active.  
---|---  
  
### Description

Sets the active build profile.

When you switch to a build profile that targets a non-active platform, this
function reimports assets affected by the target platform settings and then
returns. All script files will be compiled on the next Editor update.  
  
**Note:** This method isn't available to set build profiles that target a non-
active platform when running the Editor in [batch
mode](../Manual/EditorCommandLineArguments.html). Changing the platform
requires recompiling script code for the given platform, which can't be done
while script code is executing. This isn't a problem in the Editor as the
operation is deferred to the next Editor update. However, in batch mode the
Editor will stop after executing the designated script code, so deferring the
operation isn't possible. To set a build profile that targets a non-active
platform in batch mode, use the
[activeBuildProfile](../Manual/EditorCommandLineArguments.html) command-line
argument.

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

