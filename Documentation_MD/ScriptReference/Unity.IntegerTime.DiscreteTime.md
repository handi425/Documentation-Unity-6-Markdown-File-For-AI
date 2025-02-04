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

# DiscreteTime

struct in Unity.IntegerTime

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

Data-type representing a discrete time value.

### Static Properties

[MaxValue](Unity.IntegerTime.DiscreteTime.MaxValue.html)| The maximum
representable time.  
---|---  
[MaxValueSeconds](Unity.IntegerTime.DiscreteTime.MaxValueSeconds.html)| The
maximum representable time in seconds.  
[MinValue](Unity.IntegerTime.DiscreteTime.MinValue.html)| The minimum
representable time.  
[MinValueSeconds](Unity.IntegerTime.DiscreteTime.MinValueSeconds.html)| The
minimum representable time in seconds.  
[Tick](Unity.IntegerTime.DiscreteTime.Tick.html)| The duration in seconds of a
tick (the smallest representable unit of time).  
[Zero](Unity.IntegerTime.DiscreteTime.Zero.html)| The zero value.  
  
### Properties

[Value](Unity.IntegerTime.DiscreteTime.Value.html)| The underlying discrete
time value, which represents the number of discrete ticks.  
---|---  
  
### Constructors

[DiscreteTime](Unity.IntegerTime.DiscreteTime-ctor.html)| Constructs a
discrete time from either seconds (float/double) or ticks (int/long).  
---|---  
  
### Public Methods

[ToString](Unity.IntegerTime.DiscreteTime.ToString.html)| Returns a string
representation of the time.  
---|---  
  
### Static Methods

[FromTicks](Unity.IntegerTime.DiscreteTime.FromTicks.html)| Explicitly
converts a tick value to a DiscreteTime value.  
---|---  
  
### Operators

[operator -](Unity.IntegerTime.DiscreteTime-operator_subtract.html)| Returns
the substraction of two time values.  
---|---  
[operator !=](Unity.IntegerTime.DiscreteTime-operator_ne.html)| Returns
whether two time values are different.  
[operator *](Unity.IntegerTime.DiscreteTime-operator_multiply.html)| Returns
the multiplication of two time values.  
[operator /](Unity.IntegerTime.DiscreteTime-operator_divide.html)| A time
value divided by a floating point amount.  
[operator +](Unity.IntegerTime.DiscreteTime-operator_add.html)| Returns the
addition of two time values.  
[operator <](Unity.IntegerTime.DiscreteTime-operator_lt.html)| Returns whether
the left-hand time value is less than the right-hand one.  
[operator ==](Unity.IntegerTime.DiscreteTime-operator_eq.html)| Returns true
if the time is equal to a given time, false otherwise.  
[operator >](Unity.IntegerTime.DiscreteTime-operator_gt.html)| Returns whether
left-hand time value is greater than the right-hand one.  
[RationalTime](Unity.IntegerTime.DiscreteTime-operator_DiscreteTime.html)|
Converts a DiscreteTime to a RationalTime representation. This conversion is
always lossless.  
[Unknown operator](Unity.IntegerTime.DiscreteTime-operator_.html)| Returns
whether the left-hand time value is less than or equal to the right-hand one.  
[Unknown operator](Unity.IntegerTime.DiscreteTime-operator_.html)| Returns
whether the left-hand time value is greater than or equal to the right-hand
one.  
[Unknown operator](Unity.IntegerTime.DiscreteTime-operator_.html)| Returns the
modulus of two time values.  
  
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

