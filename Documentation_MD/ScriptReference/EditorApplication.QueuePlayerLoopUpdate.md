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

#  [EditorApplication](EditorApplication.html).QueuePlayerLoopUpdate

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

public static void QueuePlayerLoopUpdate();

### Description

Normally, a player loop update will occur in the editor when the Scene has
been modified. This method allows you to queue a player loop update regardless
of whether the Scene has been modified.

When the Scene is modified it forces a repaint of any window that has
[autoRepaintOnSceneChange](EditorWindow-autoRepaintOnSceneChange.html) set to
true. Additionally, the player loop will run and consequently update any
scripts that are marked with [ExecuteInEditMode](ExecuteInEditMode.html) or
MonoBehaviours that have [runInEditMode](MonoBehaviour-runInEditMode.html) set
to true.  
  
Sometimes you may want more consistent updates even when the Scene has not
been modified, so you can call this method to queue an update.  
  
Additional resources: [ExecuteInEditMode](ExecuteInEditMode.html),
[MonoBehaviour.runInEditMode](MonoBehaviour-runInEditMode.html),
[EditorWindow.autoRepaintOnSceneChange](EditorWindow-
autoRepaintOnSceneChange.html).

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

