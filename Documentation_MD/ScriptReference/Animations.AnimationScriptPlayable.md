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

# AnimationScriptPlayable

struct in UnityEngine.Animations

/

Implemented in:[UnityEngine.AnimationModule](UnityEngine.AnimationModule.html)

Leave feedback

  

Implements
interfaces:[IAnimationJobPlayable](Animations.IAnimationJobPlayable.html),
[IPlayable](Playables.IPlayable.html)

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

A [Playable](Playables.Playable.html) that can run a custom, multi-threaded
animation job.

This playable allows to create a custom C# job that will give read and write
access to the [AnimationStream](Animations.AnimationStream.html) during the
animation process pass in the [PlayableGraph](Playables.PlayableGraph.html).
The C# job must implement the interface
[IAnimationJob](Animations.IAnimationJob.html).  
  
NOTE: You can use [PlayableExtensions](Playables.PlayableExtensions.html)
methods with AnimationScriptPlayable objects.  
  
Additional resources: [IAnimationJob](Animations.IAnimationJob.html), and
[AnimationScriptPlayable.Create](Animations.AnimationScriptPlayable.Create.html).

### Public Methods

[GetJobData](Animations.AnimationScriptPlayable.GetJobData.html)| Gets the job
data contained in the playable.  
---|---  
[GetProcessInputs](Animations.AnimationScriptPlayable.GetProcessInputs.html)|
Returns whether the playable inputs will be processed or not.  
[SetJobData](Animations.AnimationScriptPlayable.SetJobData.html)| Sets a new
job data in the playable.  
[SetProcessInputs](Animations.AnimationScriptPlayable.SetProcessInputs.html)|
Sets the new value for processing the inputs or not.  
  
### Static Methods

[Create](Animations.AnimationScriptPlayable.Create.html)| Creates an
AnimationScriptPlayable in the PlayableGraph.  
---|---  
  
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

