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

# PlayableBinding

struct in UnityEngine.Playables

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

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

Struct that holds information regarding an output of a PlayableAsset.

PlayableAssets specify the type of outputs it supports using PlayableBindings.  
  
Do not create PlayableBinding objects directly. Use the provided built-in
methods to create the corresponding
[PlayableOutput](Playables.PlayableOutput.html). For example, to create a
PlayableBinding for an
[AnimationPlayableOutput](Animations.AnimationPlayableOutput.html), use
[AnimationPlayableBinding.Create](Animations.AnimationPlayableBinding.Create.html).
To create a PlayableBinding for a
[ScriptPlayableOutput](Playables.ScriptPlayableOutput.html), use
[ScriptPlayableBinding.Create](Playables.ScriptPlayableBinding.Create.html).

### Static Properties

[DefaultDuration](Playables.PlayableBinding.DefaultDuration.html)| The default
duration used when a PlayableOutput has no fixed duration.  
---|---  
[None](Playables.PlayableBinding.None.html)| A constant to represent a
PlayableAsset has no bindings.  
  
### Properties

[outputTargetType](Playables.PlayableBinding-outputTargetType.html)| The type
of target required by the PlayableOutput for this PlayableBinding.  
---|---  
[sourceObject](Playables.PlayableBinding-sourceObject.html)| A reference to a
UnityEngine.Object that acts a key for this binding.  
[streamName](Playables.PlayableBinding-streamName.html)| The name of the
output or input stream.  
  
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

