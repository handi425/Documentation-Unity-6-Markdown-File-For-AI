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

# AnimationCurve

class in UnityEngine

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

Store a collection of Keyframes that can be evaluated over time.

### Properties

[keys](AnimationCurve-keys.html)| All keys defined in the animation curve.  
---|---  
[length](AnimationCurve-length.html)| The number of keys in the curve. (Read
Only)  
[postWrapMode](AnimationCurve-postWrapMode.html)| The behaviour of the
animation after the last keyframe.  
[preWrapMode](AnimationCurve-preWrapMode.html)| The behaviour of the animation
before the first keyframe.  
[this[int]](AnimationCurve.Index_operator.html)| Retrieves the key at index.
(Read Only)  
  
### Constructors

[AnimationCurve](AnimationCurve-ctor.html)| Creates an animation curve from an
arbitrary number of keyframes.  
---|---  
  
### Public Methods

[AddKey](AnimationCurve.AddKey.html)| Add a new key to the curve.  
---|---  
[ClearKeys](AnimationCurve.ClearKeys.html)| Erases all KeyFrame from this
instance of the AnimationCurve.  
[CopyFrom](AnimationCurve.CopyFrom.html)| Copies the keys and properties of
the specified AnimationCurve object into this instance of the AnimationCurve
class.  
[Evaluate](AnimationCurve.Evaluate.html)| Evaluate the curve at time.  
[GetHashCode](AnimationCurve.GetHashCode.html)| A HashCode for the animation
curve, computed using all individual Keyframe.  
[MoveKey](AnimationCurve.MoveKey.html)| Moves the key at index to key.time and
key.value.  
[RemoveKey](AnimationCurve.RemoveKey.html)| Removes a key.  
[SmoothTangents](AnimationCurve.SmoothTangents.html)| Smooth the in and out
tangents of the keyframe at index.  
  
### Static Methods

[Constant](AnimationCurve.Constant.html)| Creates a constant "curve" starting
at timeStart, ending at timeEnd, and set to the value value.  
---|---  
[EaseInOut](AnimationCurve.EaseInOut.html)| Creates an ease-in and out curve
starting at timeStart, valueStart and ending at timeEnd, valueEnd.  
[Linear](AnimationCurve.Linear.html)| A straight Line starting at timeStart,
valueStart and ending at timeEnd, valueEnd.  
  
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

