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

#
[BuildPlayerWindow](BuildPlayerWindow.html).RegisterGetBuildPlayerOptionsHandler

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
RegisterGetBuildPlayerOptionsHandler(Func<BuildPlayerOptions,BuildPlayerOptions>
func);

### Parameters

func | Delegate System.Func that takes a [BuildPlayerOptions](BuildPlayerOptions.html) parameter. The value passed into the delegate will represent default options. The return value will be passed to the default build player handler, or to a custom handler set with [BuildPlayerWindow.RegisterBuildPlayerHandler](BuildPlayerWindow.RegisterBuildPlayerHandler.html).  
---|---  
  
### Description

Register a delegate method to calculate
[BuildPlayerOptions](BuildPlayerOptions.html) that are passed to the build
player handler. Registering a null value will restore default behavior, which
is the equivalent of calling
[BuildPlayerWindow.DefaultBuildMethods.GetBuildPlayerOptions](BuildPlayerWindow.DefaultBuildMethods.GetBuildPlayerOptions.html).

If this delegate is registered and used in conjunction with the default build
player handler, be sure to set [BuildPlayerOptions.scenes](BuildPlayerOptions-
scenes.html), [BuildPlayerOptions.locationPathName](BuildPlayerOptions-
locationPathName.html), and [BuildPlayerOptions.target](BuildPlayerOptions-
target.html) before exiting for the build process to proceed correctly.

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

