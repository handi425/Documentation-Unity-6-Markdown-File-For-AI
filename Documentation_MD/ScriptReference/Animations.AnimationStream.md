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

# AnimationStream

struct in UnityEngine.Animations

/

Implemented in:[UnityEngine.AnimationModule](UnityEngine.AnimationModule.html)

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

The stream of animation data passed from one
[Playable](Playables.Playable.html) to another.

The AnimationStream structure is passed through the animation
[Playable](Playables.Playable.html) structures, like
[AnimationClipPlayable](Animations.AnimationClipPlayable.html) and
[AnimationMixerPlayable](Animations.AnimationMixerPlayable.html). They can be
modified when used with an
[IAnimationJobPlayable](Animations.IAnimationJobPlayable.html), like the
[AnimationScriptPlayable](Animations.AnimationScriptPlayable.html).  
  
The Playables implementing
[IAnimationJobPlayable](Animations.IAnimationJobPlayable.html) take a custom
C# job, which must implement [IAnimationJob](Animations.IAnimationJob.html),
and the AnimationStream is then passed to its callbacks during the animation
processing pass.  
  
Additional resources: [IAnimationJob](Animations.IAnimationJob.html),
[AnimationScriptPlayable](Animations.AnimationScriptPlayable.html),
[TransformStreamHandle](Animations.TransformStreamHandle.html),
[PropertyStreamHandle](Animations.PropertyStreamHandle.html),
[TransformSceneHandle](Animations.TransformSceneHandle.html), and
[PropertySceneHandle](Animations.PropertySceneHandle.html).

### Properties

[angularVelocity](Animations.AnimationStream-angularVelocity.html)| Gets or
sets the avatar angular velocity for the evaluated frame.  
---|---  
[deltaTime](Animations.AnimationStream-deltaTime.html)| Gets the delta time
for the evaluated frame. (Read Only)  
[inputStreamCount](Animations.AnimationStream-inputStreamCount.html)| Gets the
number of input streams. (Read Only)  
[isHumanStream](Animations.AnimationStream-isHumanStream.html)| Returns true
if the stream is from a humanoid avatar; false otherwise. (Read Only)  
[isValid](Animations.AnimationStream-isValid.html)| Returns true if the stream
is valid; false otherwise. (Read Only)  
[rootMotionPosition](Animations.AnimationStream-rootMotionPosition.html)| Gets
the root motion position for the evaluated frame. (Read Only)  
[rootMotionRotation](Animations.AnimationStream-rootMotionRotation.html)| Gets
the root motion rotation for the evaluated frame. (Read Only)  
[velocity](Animations.AnimationStream-velocity.html)| Gets or sets the avatar
velocity for the evaluated frame.  
  
### Public Methods

[AsHuman](Animations.AnimationStream.AsHuman.html)| Gets the same stream, but
as an AnimationHumanStream.  
---|---  
[CopyAnimationStreamMotion](Animations.AnimationStream.CopyAnimationStreamMotion.html)|
Deep copies motion from a source animation stream to the current animation
stream.  
[GetInputStream](Animations.AnimationStream.GetInputStream.html)| Gets the
AnimationStream of the playable input at index.  
[GetInputWeight](Animations.AnimationStream.GetInputWeight.html)| Gets the
weight of the Playable connected at a specific input index.  
  
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

