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

# BaseAnimValueNonAlloc<T0>

class in UnityEditor.AnimatedValues

/

Inherits
from:[AnimatedValues.BaseAnimValue_1](AnimatedValues.BaseAnimValue_1.html)

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

Abstract base class that provides an allocation free version of BaseAnimValue.

Abstract base class that provides an allocation free version of BaseAnimValue.
See BaseAnimValue.

### Inherited Members

### Properties

[isAnimating](AnimatedValues.BaseAnimValue_1-isAnimating.html)| Is the value
currently animating.  
---|---  
[speed](AnimatedValues.BaseAnimValue_1-speed.html)| Speed of the tween.  
[target](AnimatedValues.BaseAnimValue_1-target.html)| Target to tween towards.  
[value](AnimatedValues.BaseAnimValue_1-value.html)| Current value of the
animation.  
[valueChanged](AnimatedValues.BaseAnimValue_1-valueChanged.html)| Callback
while the value is changing.  
  
### Protected Methods

[BeginAnimating](AnimatedValues.BaseAnimValue_1.BeginAnimating.html)| Begin an
animation moving from the start value to the target value.  
---|---  
[GetValue](AnimatedValues.BaseAnimValue_1.GetValue.html)| Abstract function to
be overridden in derived types. Should return the current value of the
animated value.  
[StopAnim](AnimatedValues.BaseAnimValue_1.StopAnim.html)| Stop the animation
and assign the given value.  
  
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

