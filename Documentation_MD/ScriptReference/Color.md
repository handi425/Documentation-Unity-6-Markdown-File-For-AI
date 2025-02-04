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

# Color

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

[ ]()

### Description

Representation of RGBA colors.

This structure is used throughout Unity to pass colors around. Each color
component is a floating point value with a range from 0 to 1.  
  
Components ([r](Color-r.html),[g](Color-g.html),[b](Color-b.html)) define a
color in RGB color space. Alpha component ([a](Color-a.html)) defines
transparency - alpha of one is completely opaque, alpha of zero is completely
transparent.

### Static Properties

[black](Color-black.html)| Solid black. RGBA is (0, 0, 0, 1).  
---|---  
[blue](Color-blue.html)| Solid blue. RGBA is (0, 0, 1, 1).  
[clear](Color-clear.html)| Completely transparent. RGBA is (0, 0, 0, 0).  
[cyan](Color-cyan.html)| Cyan. RGBA is (0, 1, 1, 1).  
[gray](Color-gray.html)| Gray. RGBA is (0.5, 0.5, 0.5, 1).  
[green](Color-green.html)| Solid green. RGBA is (0, 1, 0, 1).  
[grey](Color-grey.html)| English spelling for gray. RGBA is the same (0.5,
0.5, 0.5, 1).  
[magenta](Color-magenta.html)| Magenta. RGBA is (1, 0, 1, 1).  
[red](Color-red.html)| Solid red. RGBA is (1, 0, 0, 1).  
[white](Color-white.html)| Solid white. RGBA is (1, 1, 1, 1).  
[yellow](Color-yellow.html)| Yellow. RGBA is (1, 0.92, 0.016, 1), but the
color is nice to look at!  
  
### Properties

[a](Color-a.html)| Alpha component of the color (0 is transparent, 1 is
opaque).  
---|---  
[b](Color-b.html)| Blue component of the color.  
[g](Color-g.html)| Green component of the color.  
[gamma](Color-gamma.html)| A version of the color that has had the gamma curve
applied.  
[grayscale](Color-grayscale.html)| The grayscale value of the color. (Read
Only)  
[linear](Color-linear.html)| A linear value of an sRGB color.  
[maxColorComponent](Color-maxColorComponent.html)| Returns the maximum color
component value: Max(r,g,b).  
[r](Color-r.html)| Red component of the color.  
[this[int]](Color.Index_operator.html)| Access the r, g, b,a components using
[0], [1], [2], [3] respectively.  
  
### Constructors

[Color](Color-ctor.html)| Constructs a new Color with given r,g,b,a
components.  
---|---  
  
### Public Methods

[ToString](Color.ToString.html)| Returns a formatted string of this color.  
---|---  
  
### Static Methods

[HSVToRGB](Color.HSVToRGB.html)| Creates an RGB colour from HSV input.  
---|---  
[Lerp](Color.Lerp.html)| Linearly interpolates between colors a and b by t.  
[LerpUnclamped](Color.LerpUnclamped.html)| Linearly interpolates between
colors a and b by t.  
[RGBToHSV](Color.RGBToHSV.html)| Calculates the hue, saturation and value of
an RGB input color.  
  
### Operators

[Color](Color-operator_Vector4.html)| Colors can be implicitly converted to
and from Vector4.  
---|---  
[operator -](Color-operator_subtract.html)| Subtracts color b from color a.
Each component is subtracted separately.  
[operator *](Color-operator_multiply.html)| Multiplies two colors together.
Each component is multiplied separately.  
[operator /](Color-operator_divide.html)| Divides color a by the float b. Each
color component is scaled separately.  
[operator +](Color-operator_add.html)| Adds two colors together. Each
component is added separately.  
[Vector4](Color-operator_Color.html)| Colors can be implicitly converted to
and from Vector4.  
  
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

