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

#
[AnimatorJobExtensions](Animations.AnimatorJobExtensions.html).BindStreamProperty

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

public static
[Animations.PropertyStreamHandle](Animations.PropertyStreamHandle.html)
BindStreamProperty([Animator](Animator.html) animator,
[Transform](Transform.html) transform, Type type, string property);

## Declaration

public static
[Animations.PropertyStreamHandle](Animations.PropertyStreamHandle.html)
BindStreamProperty([Animator](Animator.html) animator,
[Transform](Transform.html) transform, Type type, string property, bool
isObjectReference = false);

### Parameters

animator | The [Animator](Animator.html) instance that calls this method.  
---|---  
transform | The [Transform](Transform.html) to target.  
type | The [Component](Component.html) type.  
property | The property to bind.  
isObjectReference | isObjectReference need to be set to true if the property to bind does animate an Object like [SpriteRenderer.sprite](SpriteRenderer-sprite.html).  
  
### Returns

**PropertyStreamHandle** Returns the PropertyStreamHandle that represents the
new binding.

### Description

Create a PropertyStreamHandle representing the new binding on the
[Component](Component.html) property of a [Transform](Transform.html) already
bound to the [Animator](Animator.html).

You can bind a property that doesn't exist yet. For example you can bind a
property on a [MonoBehaviour](MonoBehaviour.html) that will be added later
dynamically. In this case, you need to manually resolve the handle after
adding the [MonoBehaviour](MonoBehaviour.html) on the
[GameObject](GameObject.html), using
[ResolveAllStreamHandles](Animations.AnimatorJobExtensions.ResolveAllStreamHandles.html).

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

