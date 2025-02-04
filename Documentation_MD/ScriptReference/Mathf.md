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

# Mathf

struct in UnityEngine

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

[Switch to Manual](../Manual/class-Mathf.html "Go to Mathf Component in the
Manual")

### Description

A collection of common math functions.

### Static Properties

[Deg2Rad](Mathf.Deg2Rad.html)| Degrees-to-radians conversion constant (Read
Only).  
---|---  
[Epsilon](Mathf.Epsilon.html)| A tiny floating point value (Read Only).  
[Infinity](Mathf.Infinity.html)| A representation of positive infinity (Read
Only).  
[NegativeInfinity](Mathf.NegativeInfinity.html)| A representation of negative
infinity (Read Only).  
[PI](Mathf.PI.html)| The well-known 3.14159265358979... value (Read Only).  
[Rad2Deg](Mathf.Rad2Deg.html)| Radians-to-degrees conversion constant (Read
Only).  
  
### Static Methods

[Abs](Mathf.Abs.html)| Returns the absolute value of f.  
---|---  
[Acos](Mathf.Acos.html)| Returns the arc-cosine of f - the angle in radians
whose cosine is f.  
[Approximately](Mathf.Approximately.html)| Compares two floating point values
and returns true if they are similar.  
[Asin](Mathf.Asin.html)| Returns the arc-sine of f - the angle in radians
whose sine is f.  
[Atan](Mathf.Atan.html)| Returns the arc-tangent of f - the angle in radians
whose tangent is f.  
[Atan2](Mathf.Atan2.html)| Returns the angle in radians whose Tan is y/x.  
[Ceil](Mathf.Ceil.html)| Returns the smallest integer greater than or equal to
f.  
[CeilToInt](Mathf.CeilToInt.html)| Returns the smallest integer greater to or
equal to f.  
[Clamp](Mathf.Clamp.html)| Clamps the given value between the given minimum
float and maximum float values. Returns the given value if it is within the
minimum and maximum range.  
[Clamp01](Mathf.Clamp01.html)| Clamps value between 0 and 1 and returns value.  
[ClosestPowerOfTwo](Mathf.ClosestPowerOfTwo.html)| Returns the closest power
of two value.  
[CorrelatedColorTemperatureToRGB](Mathf.CorrelatedColorTemperatureToRGB.html)|
Convert a color temperature in Kelvin to RGB color.  
[Cos](Mathf.Cos.html)| Returns the cosine of angle f.  
[DeltaAngle](Mathf.DeltaAngle.html)| Calculates the shortest difference
between two angles.  
[Exp](Mathf.Exp.html)| Returns e raised to the specified power.  
[FloatToHalf](Mathf.FloatToHalf.html)| Encode a floating point value into a
16-bit representation.  
[Floor](Mathf.Floor.html)| Returns the largest integer smaller than or equal
to f.  
[FloorToInt](Mathf.FloorToInt.html)| Returns the largest integer smaller to or
equal to f.  
[GammaToLinearSpace](Mathf.GammaToLinearSpace.html)| Converts the given value
from gamma (sRGB) to linear color space.  
[HalfToFloat](Mathf.HalfToFloat.html)| Convert a half precision float to a
32-bit floating point value.  
[InverseLerp](Mathf.InverseLerp.html)| Determines where a value lies between
two points.  
[IsPowerOfTwo](Mathf.IsPowerOfTwo.html)| Returns true if the value is power of
two.  
[Lerp](Mathf.Lerp.html)| Linearly interpolates between a and b by t.  
[LerpAngle](Mathf.LerpAngle.html)| Same as Lerp but makes sure the values
interpolate correctly when they wrap around 360 degrees.  
[LerpUnclamped](Mathf.LerpUnclamped.html)| Linearly interpolates between a and
b by t with no limit to t.  
[LinearToGammaSpace](Mathf.LinearToGammaSpace.html)| Converts the given value
from linear to gamma (sRGB) color space.  
[Log](Mathf.Log.html)| Returns the logarithm of a specified number in a
specified base.  
[Log10](Mathf.Log10.html)| Returns the base 10 logarithm of a specified
number.  
[Max](Mathf.Max.html)| Returns the largest of two or more values. When
comparing negative values, values closer to zero are considered larger.  
[Min](Mathf.Min.html)| Returns the smallest of two or more values.  
[MoveTowards](Mathf.MoveTowards.html)| Moves a value current towards target.  
[MoveTowardsAngle](Mathf.MoveTowardsAngle.html)| Same as MoveTowards but makes
sure the values interpolate correctly when they wrap around 360 degrees.  
[NextPowerOfTwo](Mathf.NextPowerOfTwo.html)| Returns the next power of two
that is equal to, or greater than, the argument.  
[PerlinNoise](Mathf.PerlinNoise.html)| Generate 2D Perlin noise.  
[PerlinNoise1D](Mathf.PerlinNoise1D.html)| Generates a 1D pseudo-random
pattern of float values across a 2D plane.  
[PingPong](Mathf.PingPong.html)| PingPong returns a value that increments and
decrements between zero and the length. It follows the triangle wave formula
where the bottom is set to zero and the peak is set to length.  
[Pow](Mathf.Pow.html)| Returns f raised to power p.  
[Repeat](Mathf.Repeat.html)| Loops the value t, so that it is never larger
than length and never smaller than 0.  
[Round](Mathf.Round.html)| Returns f rounded to the nearest integer.  
[RoundToInt](Mathf.RoundToInt.html)| Returns f rounded to the nearest integer.  
[Sign](Mathf.Sign.html)| Returns the sign of f.  
[Sin](Mathf.Sin.html)| Returns the sine of angle f.  
[SmoothDamp](Mathf.SmoothDamp.html)| Gradually moves the current value towards
a target value, over a specified time and at a specified velocity.  
[SmoothDampAngle](Mathf.SmoothDampAngle.html)| Gradually changes an angle
given in degrees towards a desired goal angle over time.  
[SmoothStep](Mathf.SmoothStep.html)| Interpolates between from and to with
smoothing at the limits.  
[Sqrt](Mathf.Sqrt.html)| Returns square root of f.  
[Tan](Mathf.Tan.html)| Returns the tangent of angle f in radians.  
  
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

