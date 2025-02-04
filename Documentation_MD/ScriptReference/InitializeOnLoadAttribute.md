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

# InitializeOnLoadAttribute

class in UnityEditor

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

Allows you to initialize an Editor class when Unity loads, and when your
scripts are recompiled.

Static constructors with this attribute are called when scripts in the project
are recompiled (also known as a [Domain Reload](../Manual/domain-
reloading.html)). This happens when Unity first loads your project, but also
when Unity detects modifications to scripts (depending on your [Auto Refresh
preferences](../Manual/Preferences.html)), and when you enter Play Mode
(depending on your [Play Mode configuration](../Manual/configurable-enter-
play-mode.html)).  
  
Asset operations such as asset loading should be avoided in InitializeOnLoad
methods. InitializeOnLoad methods are called before asset importing is
completed and therefore the asset loading can fail resulting in a null object.
To do initialization after a domain reload which requires asset operations use
the
[AssetPostprocessor.OnPostprocessAllAssets](AssetPostprocessor.OnPostprocessAllAssets.html)
callback. This callback supports all asset operations and has a parameter
signaling if there was a domain reload.  
  
Additional resources: [running editor code on launch](../Manual/running-
editor-code-on-launch.html).

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

