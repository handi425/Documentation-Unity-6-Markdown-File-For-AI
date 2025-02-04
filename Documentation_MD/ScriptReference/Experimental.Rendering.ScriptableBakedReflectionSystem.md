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

# ScriptableBakedReflectionSystem

class in UnityEditor.Experimental.Rendering

Leave feedback

  

Implements
interfaces:[IScriptableBakedReflectionSystem](Experimental.Rendering.IScriptableBakedReflectionSystem.html)

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

Empty implementation of
[IScriptableBakedReflectionSystem](Experimental.Rendering.IScriptableBakedReflectionSystem.html).

Use this class as a base class and override its methods to implement your own
ScriptableBakedReflectionSystem.

### Properties

[stageCount](Experimental.Rendering.ScriptableBakedReflectionSystem-
stageCount.html)| Number of stages of the baking process.  
---|---  
[stateHashes](Experimental.Rendering.ScriptableBakedReflectionSystem-
stateHashes.html)| The hashes of the current baked state of the
ScriptableBakedReflectionSystem.  
  
### Public Methods

[BakeAllReflectionProbes](Experimental.Rendering.ScriptableBakedReflectionSystem.BakeAllReflectionProbes.html)|
Implement this method to bake all of the loaded reflection probes.  
---|---  
[Cancel](Experimental.Rendering.ScriptableBakedReflectionSystem.Cancel.html)|
Cancel the running bake jobs.  
[Clear](Experimental.Rendering.ScriptableBakedReflectionSystem.Clear.html)|
Clear the state of ScriptableBakedReflectionSystem.  
[SynchronizeReflectionProbes](Experimental.Rendering.ScriptableBakedReflectionSystem.SynchronizeReflectionProbes.html)|
Synchronize the baked data with the actual components and rendering settings.  
[Tick](Experimental.Rendering.ScriptableBakedReflectionSystem.Tick.html)| This
method is called during the Editor update until the
ScriptableBakedReflectionSystem indicates that the baking is complete, with
handle.SetIsDone(true). (See
IScriptableBakedReflectionSystemStageNotifier.SetIsDone).  
  
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

