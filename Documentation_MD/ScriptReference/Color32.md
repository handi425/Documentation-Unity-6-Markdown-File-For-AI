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

# Color32

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

Representation of RGBA colors in 32 bit format.

Each color component is a byte value with a range from 0 to 255.  
  
Components ([r](Color32-r.html),[g](Color32-g.html),[b](Color32-b.html))
define a color in RGB color space. Alpha component ([a](Color32-a.html))
defines transparency - alpha of 255 is completely opaque, alpha of zero is
completely transparent.

### Properties

[a](Color32-a.html)| Alpha component of the color.  
---|---  
[b](Color32-b.html)| Blue component of the color.  
[g](Color32-g.html)| Green component of the color.  
[r](Color32-r.html)| Red component of the color.  
[this[int]](Color32.Index_operator.html)| Access the red (r), green (g), blue
(b), and alpha (a) color components using [0], [1], [2], [3] respectively.  
  
### Constructors

[Color32](Color32-ctor.html)| Constructs a new Color32 with given r, g, b, a
components.  
---|---  
  
### Public Methods

[ToString](Color32.ToString.html)| Returns a formatted string for this color.  
---|---  
  
### Static Methods

[Lerp](Color32.Lerp.html)| Linearly interpolates between colors a and b by t.  
---|---  
[LerpUnclamped](Color32.LerpUnclamped.html)| Linearly interpolates between
colors a and b by t.  
  
### Operators

[Color](Color32-operator_Color32.html)| Color32 can be implicitly converted to
and from Color.  
---|---  
[Color32](Color32-operator_Color.html)| Color32 can be implicitly converted to
and from Color.  
  
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

