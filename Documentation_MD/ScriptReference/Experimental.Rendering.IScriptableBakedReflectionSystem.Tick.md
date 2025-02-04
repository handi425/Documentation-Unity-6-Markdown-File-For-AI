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

**Experimental** : this API is experimental and might be changed or removed in
the future.

#
[IScriptableBakedReflectionSystem](Experimental.Rendering.IScriptableBakedReflectionSystem.html).Tick

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

public void
Tick([Experimental.Rendering.SceneStateHash](Experimental.Rendering.SceneStateHash.html)
sceneStateHash,
[Experimental.Rendering.IScriptableBakedReflectionSystemStageNotifier](Experimental.Rendering.IScriptableBakedReflectionSystemStageNotifier.html)
handle);

### Parameters

sceneStateHash | Current Scene state hash.  
---|---  
handle | A handle to receive notifications about the status of the stages of the baking process.  
  
### Description

This method is called every Editor update until the
ScriptableBakedReflectionSystem indicates that the baking is complete, with
`handle.SetIsDone(true)`. (See
[IScriptableBakedReflectionSystemStageNotifier.SetIsDone](Experimental.Rendering.IScriptableBakedReflectionSystemStageNotifier.SetIsDone.html)).

You should use this to check if a bake is required by comparing the provided
hashes (or your own hashes) with the baked data.  
  
If you detect any changes, then this is the place to prepare and launch baking
jobs. While the jobs are running, you can indicate their progress with the
`handle.EnterStage(stage, progressMessage, progress)` call. See
[IScriptableBakedReflectionSystemStageNotifier.EnterStage](Experimental.Rendering.IScriptableBakedReflectionSystemStageNotifier.EnterStage.html).  
  
See
[IScriptableBakedReflectionSystem](Experimental.Rendering.IScriptableBakedReflectionSystem.html)
for examples.

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

