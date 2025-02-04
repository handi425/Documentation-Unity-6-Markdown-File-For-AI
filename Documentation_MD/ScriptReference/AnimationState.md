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

# AnimationState

class in UnityEngine

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

The AnimationState gives full control over animation blending.

In most cases the [Animation](Animation.html) interface is sufficient and
easier to use. Use the AnimationState if you need full control over the
animation blending any playback process.  
  
The AnimationState interface allows you to modify speed, weight, time and
layers while any animation is playing. You can also setup animation mixing and
wrapMode.  
  
The Animation.

### Properties

[blendMode](AnimationState-blendMode.html)| Which blend mode should be used?  
---|---  
[clip](AnimationState-clip.html)| The clip that is being played by this
animation state.  
[enabled](AnimationState-enabled.html)| Enables / disables the animation.  
[length](AnimationState-length.html)| The length of the animation clip in
seconds.  
[name](AnimationState-name.html)| The name of the animation.  
[normalizedSpeed](AnimationState-normalizedSpeed.html)| The normalized
playback speed.  
[normalizedTime](AnimationState-normalizedTime.html)| Normalized time of the
State.  
[speed](AnimationState-speed.html)| The playback speed of the animation. 1 is
normal playback speed.  
[time](AnimationState-time.html)| The current time of the animation.  
[weight](AnimationState-weight.html)| The weight of animation.  
[wrapMode](AnimationState-wrapMode.html)| Wrapping mode of the animation.  
  
### Public Methods

[AddMixingTransform](AnimationState.AddMixingTransform.html)| Adds a transform
which should be animated. This allows you to reduce the number of animations
you have to create.  
---|---  
[RemoveMixingTransform](AnimationState.RemoveMixingTransform.html)| Removes a
transform which should be animated.  
  
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

