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

# AnimationClip

class in UnityEngine

/

Inherits from:[Motion](Motion.html)

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

[Switch to Manual](../Manual/class-AnimationClip.html "Go to AnimationClip
Component in the Manual")

### Description

Stores keyframe based animations.

AnimationClip is used by [Animation](Animation.html) to play back animations.

### Properties

[empty](AnimationClip-empty.html)| Returns true if the animation clip has no
curves and no events.  
---|---  
[events](AnimationClip-events.html)| Animation Events for this animation clip.  
[frameRate](AnimationClip-frameRate.html)| Frame rate at which keyframes are
sampled. (Read Only)  
[hasGenericRootTransform](AnimationClip-hasGenericRootTransform.html)| Returns
true if the Animation has animation on the root transform.  
[hasMotionCurves](AnimationClip-hasMotionCurves.html)| Returns true if the
AnimationClip has root motion curves.  
[hasMotionFloatCurves](AnimationClip-hasMotionFloatCurves.html)| Returns true
if the AnimationClip has editor curves for its root motion.  
[hasRootCurves](AnimationClip-hasRootCurves.html)| Returns true if the
AnimationClip has root Curves.  
[humanMotion](AnimationClip-humanMotion.html)| Returns true if the animation
contains curve that drives a humanoid rig.  
[legacy](AnimationClip-legacy.html)| Set to true if the AnimationClip will be
used with the Legacy Animation component ( instead of the Animator ).  
[length](AnimationClip-length.html)| Animation length in seconds. (Read Only)  
[localBounds](AnimationClip-localBounds.html)| AABB of this Animation Clip in
local space of Animation component that it is attached too.  
[wrapMode](AnimationClip-wrapMode.html)| Sets the default wrap mode used in
the animation state.  
  
### Constructors

[AnimationClip](AnimationClip-ctor.html)| Creates a new animation clip.  
---|---  
  
### Public Methods

[AddEvent](AnimationClip.AddEvent.html)| Adds an animation event to the clip.  
---|---  
[ClearCurves](AnimationClip.ClearCurves.html)| Clears all curves from the
clip.  
[EnsureQuaternionContinuity](AnimationClip.EnsureQuaternionContinuity.html)|
Realigns quaternion keys to ensure shortest interpolation paths.  
[SampleAnimation](AnimationClip.SampleAnimation.html)| Samples an animation at
a given time for any animated properties.  
[SetCurve](AnimationClip.SetCurve.html)| Assigns the curve to animate a
specific property.  
  
### Inherited Members

### Properties

[hideFlags](Object-hideFlags.html)| Should the object be hidden, saved with
the Scene or modifiable by the user?  
---|---  
[name](Object-name.html)| The name of the object.  
  
### Public Methods

[GetInstanceID](Object.GetInstanceID.html)| Gets the instance ID of the
object.  
---|---  
[ToString](Object.ToString.html)| Returns the name of the object.  
  
### Static Methods

[Destroy](Object.Destroy.html)| Removes a GameObject, component or asset.  
---|---  
[DestroyImmediate](Object.DestroyImmediate.html)| Destroys the object obj
immediately. You are strongly recommended to use Destroy instead.  
[DontDestroyOnLoad](Object.DontDestroyOnLoad.html)| Do not destroy the target
Object when loading a new Scene.  
[FindAnyObjectByType](Object.FindAnyObjectByType.html)| Retrieves any active
loaded object of Type type.  
[FindFirstObjectByType](Object.FindFirstObjectByType.html)| Retrieves the
first active loaded object of Type type.  
[FindObjectsByType](Object.FindObjectsByType.html)| Retrieves a list of all
loaded objects of Type type.  
[Instantiate](Object.Instantiate.html)| Clones the object original and returns
the clone.  
[InstantiateAsync](Object.InstantiateAsync.html)| Captures a snapshot of the
original object (that must be related to some GameObject) and returns the
AsyncInstantiateOperation.  
  
### Operators

[bool](Object-operator_Object.html)| Does the object exist?  
---|---  
[operator !=](Object-operator_ne.html)| Compares if two objects refer to a
different object.  
[operator ==](Object-operator_eq.html)| Compares two object references to see
if they refer to the same object.  
  
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

