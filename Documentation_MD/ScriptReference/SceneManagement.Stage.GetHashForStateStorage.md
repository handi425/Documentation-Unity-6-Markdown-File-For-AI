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

#  [Stage](SceneManagement.Stage.html).GetHashForStateStorage

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

protected [Hash128](Hash128.html) GetHashForStateStorage();

### Returns

**Hash128** The hash code identifying this stage.

### Description

Unity calls this method to get a hash code that is used to save the state of
the Stage to disk.

The state includes Scene view settings and the Camera position. Some Stage
types may store additional state data such as the scroll position in the
Hierarchy window. Saving the state ensures that, if you close a stage and
later open it, Scene view settings, the Camera position, and other stored
objects are in the same state you left them in when you closed the Stage.  
  
For stages that use the [assetPath](SceneManagement.Stage-assetPath.html)
property, the hash code is by default based on the Asset GUID, meaning the
state is saved individually per Asset. For stages that don't use the
[assetPath](SceneManagement.Stage-assetPath.html) property, the hash code is
by default shared for all stages of that type. Custom stage types can override
this method to use different logic to determine in which way stage state
should be reused.

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

