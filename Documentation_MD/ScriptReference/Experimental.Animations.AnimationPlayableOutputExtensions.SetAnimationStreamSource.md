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
[AnimationPlayableOutputExtensions](Experimental.Animations.AnimationPlayableOutputExtensions.html).SetAnimationStreamSource

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
SetAnimationStreamSource([Animations.AnimationPlayableOutput](Animations.AnimationPlayableOutput.html)
output,
[Experimental.Animations.AnimationStreamSource](Experimental.Animations.AnimationStreamSource.html)
streamSource);

### Parameters

output | The [AnimationPlayableOutput](Animations.AnimationPlayableOutput.html) instance that calls this method.  
---|---  
streamSource | The [AnimationStreamSource](Experimental.Animations.AnimationStreamSource.html) to apply on this output.  
  
### Description

Sets the stream source for the specified
[AnimationPlayableOutput](Animations.AnimationPlayableOutput.html).

When setting the
[AnimationStreamSource](Experimental.Animations.AnimationStreamSource.html) of
the output to
[AnimationStreamSource.DefaultValues](Experimental.Animations.AnimationStreamSource.DefaultValues.html),
the [AnimationStream](Animations.AnimationStream.html) of this output
initalizes every frame with the default values of the
[Animator](Animator.html).  
  
When setting the
[AnimationStreamSource](Experimental.Animations.AnimationStreamSource.html) of
the output to
[AnimationStreamSource.PreviousInputs](Experimental.Animations.AnimationStreamSource.PreviousInputs.html),
the [AnimationStream](Animations.AnimationStream.html) of this output
initalizes every frame with the result of any previously evaluated outputs on
the same [Animator](Animator.html).  
  
If you use the graph connected to an
[AnimationPlayableOutput](Animations.AnimationPlayableOutput.html) to post-
process the result of other Animation graphs connected to the same
[Animator](Animator.html), you should use
[AnimationStreamSource.PreviousInputs](Experimental.Animations.AnimationStreamSource.PreviousInputs.html).
For example, if you use the [AnimationStream](Animations.AnimationStream.html)
to build an Inverse Kinematics constraint to post-process the built-in
[AnimatorController](Animations.AnimatorController.html), your
[AnimationPlayableOutput](Animations.AnimationPlayableOutput.html) should be
set to
[AnimationStreamSource.PreviousInputs](Experimental.Animations.AnimationStreamSource.PreviousInputs.html).  
  
In order to start the [AnimationStream](Animations.AnimationStream.html) from
a blank slate, you should use
[AnimationStreamSource.DefaultValues](Experimental.Animations.AnimationStreamSource.DefaultValues.html).
For example, to build a custom animation source starting from the default
pose, the [AnimationPlayableOutput](Animations.AnimationPlayableOutput.html)
should be set to
[AnimationStreamSource.DefaultValues](Experimental.Animations.AnimationStreamSource.DefaultValues.html).  
  
Additional resources:
[AnimationStreamSource](Experimental.Animations.AnimationStreamSource.html).

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

