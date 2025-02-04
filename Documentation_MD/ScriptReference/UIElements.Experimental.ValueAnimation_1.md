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

# ValueAnimation<T0>

class in UnityEngine.UIElements.Experimental

/

Implemented
in:[UnityEngine.UIElementsModule](UnityEngine.UIElementsModule.html)

Leave feedback

  

Implements
interfaces:[IValueAnimation](UIElements.Experimental.IValueAnimation.html)

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

Implementation object for transition animations.

### Properties

[autoRecycle](UIElements.Experimental.ValueAnimation_1-autoRecycle.html)|
Returns true if this animation object will be automatically returned to the
instance pool after the animation has completed.  
---|---  
[durationMs](UIElements.Experimental.ValueAnimation_1-durationMs.html)|
Duration of the animation in milliseconds.  
[easingCurve](UIElements.Experimental.ValueAnimation_1-easingCurve.html)|
Smoothing function related to this animation. Default value is Easing.OutQuad.  
[from](UIElements.Experimental.ValueAnimation_1-from.html)|  The animation
start value.  
[initialValue](UIElements.Experimental.ValueAnimation_1-initialValue.html)|
Callback invoked when the from field has not been set, in order to retrieve
the starting state of this animation.  
[interpolator](UIElements.Experimental.ValueAnimation_1-interpolator.html)|
Value interpolation method.  
[isRunning](UIElements.Experimental.ValueAnimation_1-isRunning.html)|  Tells
if the animation is currently active.  
[onAnimationCompleted](UIElements.Experimental.ValueAnimation_1-onAnimationCompleted.html)|
Callback invoked when this animation has completed.  
[to](UIElements.Experimental.ValueAnimation_1-to.html)|  The animation end
value.  
[valueUpdated](UIElements.Experimental.ValueAnimation_1-valueUpdated.html)|
Callback invoked after every value interpolation.  
  
### Constructors

[ValueAnimation_1](UIElements.Experimental.ValueAnimation_1-ctor.html)|
Constructor.  
---|---  
  
### Public Methods

[Ease](UIElements.Experimental.ValueAnimation_1.Ease.html)|  Sets the easing
function.  
---|---  
[KeepAlive](UIElements.Experimental.ValueAnimation_1.KeepAlive.html)|  Will
not return the object to the instance pool when the animation has completed.  
[OnCompleted](UIElements.Experimental.ValueAnimation_1.OnCompleted.html)|
Sets a callback invoked when this animation has completed.  
[Recycle](UIElements.Experimental.ValueAnimation_1.Recycle.html)|  Returns
this animation object into its object pool.  
[Start](UIElements.Experimental.ValueAnimation_1.Start.html)|  Starts the
animation using this object's values.  
[Stop](UIElements.Experimental.ValueAnimation_1.Stop.html)|  Stops this
animation.  
  
### Static Methods

[Create](UIElements.Experimental.ValueAnimation_1.Create.html)|  Creates a new
ValueAnimation object or returns an available one from it's instance pool.  
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

